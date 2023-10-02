import socket
import os
from helpers import get_valid_ip, get_valid_port
from time import sleep


def main():
    HOST = get_valid_ip()   # inserção do IP (localhost = 127.0.0.1)
    PORT = get_valid_port() # inserção da Porta (server rodando porta 50000)
    client((HOST, PORT))


def client(ADDR):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_client:
        socket_client.connect(ADDR)
        print(f'Conectado ao servidor em {ADDR[0]} {ADDR[1]}')

        while True:
            data = socket_client.recv(4096)
            data = data.decode() # recebe a resposta do servidor

            if data == 'Eu acho que o animal que você está pensando é um(a) {animals[animalsIdxAux[0]]}.' or data == 'Sério? Desculpa, não sei o que aconteceu. :(':
                data = socket_client.recv(4096)
                print(data)
                socket_client.sendall(input().strip())
                data = socket_client.recv(4096)
                print(data.decode())
                break
            else: 
                socket_client.sendall(data.encode())
    sleep(3)
    menu() 

def menu():
    if os.name == 'nt':
        clear_cmd = 'cls'
    else:
        clear_cmd = 'clear'

    os.system(clear_cmd)
    print('\tTela inicial do programa')
    print('-' * 40)
    print('Selecione uma das opções abaixo:\n')
    print('\t0 - Logar no servidor\n\t1 - Sair do programa\n')
    print('-' * 40)

    while True:
        op = input('-> ').strip()
        if op == '0':
            break
        elif op == '1':
            return
        else:
            print('Opção invalida!')

    os.system(clear_cmd)
    main()
menu()      
