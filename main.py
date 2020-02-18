import random
from Topologia import topo01
from GeracaoChamadas import Call


def main():
    topologia = input('Informe a topologia de rede: ')    
    if topologia == 'topo01':
            n_nodes = len(topo01)
            #print(n_nodes)
    else:
            print('Erro: A topologia de rede informada é inválida.')
            
    tipo_de_rede = input('Informe o tipo de rede (WDM ou EON): ')
    if tipo_de_rede == 'WDM' or tipo_de_rede == 'EON':
            quant_fib = input('Informe a quantidade de fibras: ')
            quant_nuc = input('Informe a quantidade de núcleos: ')
            quant_mod = input('Informe a quantidade de modos: ')

            dados_da_rede = open('arq01.txt', 'w')
            dados_da_rede.write('Tipo de rede: ' + tipo_de_rede)
            dados_da_rede.write('\nQuantidade de fibras: ' + quant_fib)
            dados_da_rede.write('\nQuantidade de núcleos: ' + quant_nuc)
            dados_da_rede.write('\nQuantidade de modos: ' + quant_mod)
            dados_da_rede.close()
    else:
            print('Erro: O tipo de rede informado é inválido.')

    tipo_de_trafego = input('Informe o tipo de tráfego (Estático, Incremental ou Dinâmico): ')
    if tipo_de_trafego == 'Estático' or tipo_de_trafego == 'Incremental' or tipo_de_trafego == 'Dinâmico':
            dados_da_rede = open('arq01.txt', 'r')
            tipo_trafego = dados_da_rede.readlines()
            tipo_trafego.append('\nTipo de tráfego: ' + tipo_de_trafego)
            dados_da_rede = open('arq01.txt', 'w')
            dados_da_rede.writelines(tipo_trafego)
            dados_da_rede.close()
    else:
            print('Erro: O tipo de tráfego informado é inválido.')

    # --------------- Solicitação de chamada ------------------
    nodes = range(1, n_nodes+1, 1)        
    #print(list(nodes))
    src_node = nodes[random.randint(1,len(nodes))]           # Randomly assign src node from list
    dst_node = nodes[random.randint(1,len(nodes))]
    while(dst_node == src_node):                             # Ensure dst node is not equal to source
        dst_node = nodes[random.randint(1, len(nodes))]      # Randomly assign dest node from list         
    bit_rate = random.randint(10,500)                        # Randomly assign bit rate

    chamada = Call(src_node, dst_node, bit_rate) 

    print('Source node:', chamada.GetSrc())
    print('Destination node:', chamada.GetDst())
    print('Bit rate:', chamada.GetBitRate(), 'Gbps')
   
   # --------------- Verficando se tem rota ------------------
   
if __name__ == '__main__':
    main()
