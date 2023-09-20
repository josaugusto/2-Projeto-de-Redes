import socket
import threading
from time import sleep

HOST = 'localhost'  # 127.0.0.1
PORT = 50000

def handle_client(socket_client, client_address):
        print(f'Conectado em {client_address}')  # cliente conectado


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_server:  # criando um socket do tipo TCP
    socket_server.bind((HOST, PORT)) # associa um socket a um endereço e uma porta especifica
    socket_server.listen() # começa a "escutar" as conexões
    print('Aguardando conexão de um cliente...')

    while True:  # loop que fica sempre procurando conexões
        socket_client, client_address = socket_server.accept()  # aceitando a conexão do client
        print('\nNovo cliente conectado. Inicializando jogo...')
        client_thread = threading.Thread(target=handle_client, args=(socket_client, client_address)) # cria uma thread para cada cliente conectado
        client_thread.start()   # iniciando a thread do client
