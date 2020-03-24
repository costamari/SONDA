from Topology import topo01, adj01
from CallGenerator import Call
from Dijkstra_RoutingAlgorithm import dijkstra


def main():
        
        topology = input('Enter the network topology: ')    
        if topology == 'topo01':
                n_nodes = len(topo01) 
                A = adj01
        else:
                print('Error: The network topology entered is invalid.')
            
        network_type = input('Enter the network type (WDM or EON): ')
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
                print('Error: The network type entered is invalid.')

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

        # --------------- Solicitação de chamadas ------------------

        n_calls = int(input('Enter the number of calls: '))                 # Refers to the number of simulated calls in the program
        Lambda1 = float(input('Enter the average call arrival rate: '))     # Refers to the average arrival rate of calls according to a poissonian processo
        Lambda2 = float(input('Enter the average call duration rate: '))    # Refers to the average call duration rate according to exponential distribution
    
        call = Call(n_nodes, Lambda1, Lambda2)
        src_node = []
        dst_node = []
        bit_rate = []
        arrival_time = []
        duration_time = []
        current_time = [0] * n_calls
        ending_time = [0] * n_calls
        
        for i in range(n_calls): 
                src_node.append(call.Src())
                dst_node.append(call.Dst())
                bit_rate.append(call.BitRate())
                arrival_time.append(call.ArrivalTime())
                duration_time.append(call.DurationTime())
                                
                if i == 0: 
                        current_time[i] = arrival_time[i]
                else:        
                        current_time[i] = current_time[i-1] + arrival_time[i]                      

                ending_time[i] = current_time[i] + duration_time[i]                                            
                                                                
        print('Source nodes list:', src_node)           
        print('Destination nodes list:', dst_node)
        print('Bit rates list:', bit_rate)
        print('Arrival times list:', arrival_time)
        print('Duration times list:', duration_time)             
        print('Current times list:', current_time)
        print('Ending times list:', ending_time)    
   
        # --------------- Verificando se tem rota ------------------

        for i in range(n_calls):                         
                print('Route', i+1)
                dijkstra(A, src_node[i], dst_node[i])
                
if __name__ == '__main__':
    main()