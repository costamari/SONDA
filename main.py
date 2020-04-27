import random
from Topology import *
from CallGenerator import Call
from Dijkstra_RoutingAlgorithm import Dijkstra, ShortestDistance
from FirstFit_ResourceAlgorithm import *

def main():
        
        topology = input('Enter the network topology: ')    
        if topology == 'topo01':
                n_nodes = len(adj01) - 1 
                A = adj01
                n_links = len(links01)
                links = links01
        elif topology == 'European':        
                n_nodes = len(adjEuropean) - 1 
                A = adjEuropean
                n_links = len(linksEuropean)
                links = linksEuropean
        elif topology == 'Top1':
                n_nodes = len(adjTop1) - 1 
                A = adjTop1
                n_links = len(linksTop1)
                links = linksTop1
        else:
                raise ValueError('The network topology entered is invalid.')
            
        network_type = str(input('Enter the network type (WDM or EON): '))
        if network_type == 'WDM' or network_type == 'EON':

                n_fibers = int(input('Enter the number of fibers: '))
                n_cores = int(input('Enter the number of cores: '))
                n_modes = int(input('Enter the number of modes: '))
            
                network_data = open('arq01.txt', 'w')
                network_data.write('Network type: ' + str(network_type))
                network_data.write('\nNumber of fibers: ' + str(n_fibers))
                network_data.write('\nNumber of cores: ' + str(n_cores))
                network_data.write('\nNumber of modes: ' + str(n_modes))
                network_data.close()
        else:
                raise ValueError('The network type entered is invalid.')

        '''    
        tipo_de_trafego = input('Informe o tipo de tráfego (Estático, Incremental ou Dinâmico): ')
        if tipo_de_trafego == 'Estático' or tipo_de_trafego == 'Incremental' or tipo_de_trafego == 'Dinâmico':
                dados_da_rede = open('arq01.txt', 'r')
                tipo_trafego = dados_da_rede.readlines()
                dados_da_rede = open('arq01.txt', 'w')
                dados_da_rede.writelines(tipo_trafego)
                dados_da_rede.close()
        else:
                print('Erro: O tipo de tráfego informado é inválido.')
        '''

        # --------------- Solicitação de chamadas e verifição de rotas e de recursos ------------------

        n_calls = int(input('Enter the number of calls: '))             # Refers to the number of simulated calls in the program
        min_traffic_load = int(input('Enter the min. traffic load: '))    
        max_traffic_load = int(input('Enter the max. traffic load: '))
        step = int(input('Enter the step: '))                 
                
        wave, time = generate(n_nodes, links)
        blocked = []
        # print('Load - Blocking probability')        
        
        for load in range(min_traffic_load, max_traffic_load, step):
                
                # call requests arrival
                N = wave.copy()
                T = time.copy() # holding time
                count_block = 0                           

                random.seed(0)
                call = Call(n_nodes, load, 1)
                src_node = []
                dst_node = []
                bit_rate = []
                arrival_time = []
                duration_time = []
                current_time = [0] * n_calls
                # ending_time = [0] * n_calls
                interarrival = [0] * n_calls
                
                for gen in range(n_calls):
                        src_node.append(call.Src())
                        dst_node.append(call.Dst())
                        bit_rate.append(call.BitRate())
                        arrival_time.append(round(call.ArrivalTime(), 6))
                        duration_time.append(round(call.DurationTime(), 6))
                                                                
                        if gen == 0: 
                                current_time[gen] = arrival_time[gen]
                        else:        
                                current_time[gen] = current_time[gen-1] + arrival_time[gen]                     

                        # ending_time[gen] = round(current_time[gen] + duration_time[gen], 4)

                for gen in range(n_calls):

                        if gen == n_calls-1:
                                interarrival[gen] = 0
                        else:
                                interarrival[gen] = current_time[gen+1] - current_time[gen]
                        			
                        route = Dijkstra(A, src_node[gen], dst_node[gen])                
                
                        count_block += first_fit(N, T, route, duration_time[gen])

                        # Atualiza todos os canais que ainda estao sendo usados 
                        for link in links:
                                i, j = link
                                for w in range(num_channels):
					# Dijkstra + First-fit
                                        if T[i][j][w] > interarrival[gen]:
                                                T[i][j][w] -= interarrival[gen]
                                        else:
                                                T[i][j][w] = 0
                                                if not N[i][j][w]:
                                                        N[i][j][w] = 1 # free channel                                                                              	

                blocked.append(count_block/n_calls)               

        print(blocked)       

if __name__ == '__main__':
    main()
