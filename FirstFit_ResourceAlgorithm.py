from Topology import links01
import numpy as np
import random
import sys
import importlib
importlib.reload(sys)

global num_channels
num_channels = 8

def generate(num_nodes, links): 
            
    # init wavelength availability matrix    
    dimension = (num_nodes+1, num_nodes+1, num_channels)
    wave = np.zeros(shape=dimension, dtype=np.uint8)
    for link in links:
        for w in range(num_channels):
            wave_availability = 1
            wave[link[0]][link[1]][w] = wave_availability
            wave[link[1]][link[0]][w] = wave_availability

    # init traffic matrix
    dimension = (num_nodes+1, num_nodes+1, num_channels)
    time = np.zeros(shape=dimension, dtype=np.float64)
    for link in links:
        for w in range(num_channels):
            time[link[0]][link[1]][w] = 0
            time[link[1]][link[0]][w] = 0

    return wave, time

def first_fit(N, T, route, holding_time):
    color = None
    rcurr, rnext = route[0], route[1]
    # Check whether each wavelength ...
    for w in range(num_channels):
        # ... is available on the first link of route R
        if N[rcurr][rnext][w]:        
            color = w
            break

    if color is not None:
        # LOCAL KNOWLEDGE check if the color chosen at the first link is
        # availble on all links of the route
        for r in range(len(route)-1):
            rcurr = route[r]
            rnext = route[r+1]

            # if not available in any of the next links, block
            if not N[rcurr][rnext][color]:            
                return 1  # blocked

        # if available on all links of the route, alloc net resources for the call
        for r in range(len(route)-1):
            rcurr = route[r]
            rnext = route[r+1]

            N[rcurr][rnext][color] = 0

            T[rcurr][rnext][color] = holding_time

        return 0  # allocated
    else:
        return 1  # blocked