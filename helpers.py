from ipaddress import ip_address


def get_valid_ip():
    while True:
        try:
            ip = input('IP do servidor: ')
            ip_address(ip)  # verificando se o ip é valido, caso não, sobe o erro "ValueError"
            return ip       # retorna o ip se tiver tudo certo
        except ValueError:
            print('Endereço IP inválido.\nTente novamente.')    # tenta novamente caso esteja errado


def get_valid_port():
    while True:
        try:
            port = int(input('Porta: '))    # pede a porta para conexão
            if 1024 <= port <= 65535:
                return port
            else:
                print('A porta precisa estar entre 1024 e 65535.\nTente novamente.')                   
        except ValueError: 
            print('A porta tem que ser um número inteiro.\nTente novamente.')
