# Jogo da Adivinhação

Vamos brincar de adivinhar o animal! O servidor vai te fazer perguntas espertas para descobrir qual é o bicho que está na sua mente. Com cada pergunta, ele vai eliminando opções até chegar na resposta. O jogo utiliza sockets TCP em Python para estabelecer a conexão entre o cliente e o servidor. Quando a conexão é estabelecida, o servidor cria uma thread para cada jogador, garantindo que cada usuário jogue individualmente, sem interação com outros jogadores conectados.

## Instalação

Para realizar a instalação será necesário que você tenha o [Python](https://www.python.org/downloads/), [Git](https://git-scm.com/) e o Editor de código de sua preferencia(para facilitar a visualização e edição do ip do servidor, caso queira deixar ele acessivel para outros computadores poderem acessar) recomendamos [VScode](https://code.visualstudio.com/).

Ao final de tudo instalado, você deverá clonar o repositório.

Para facilitar, tudo estará nos comandos a seguir.

Os comandos deverão ser realizados no terminal do Git:

- $ mkdir JOGO

- $ cd JOGO

- $ git clone https://github.com/josaugusto/2-Projeto-de-Redes.git

- $ cd 2-Projeto-de-Redes

## Uso

Para jogar, é necessário que você tenha aberto a pasta do jogo no seu editor de código. Caso tenha o VScode instalado e tenha concluído o último passo da instrução de instalação, basta executar o seguinte comando.

- $ code .

e o projeto será aberto no VScode.

para rodar o jogo você deverá abrir dois terminais no VScode, sendo um para o servidor e um para o cliente, lembre-se, o terminal do servidor não deve ser fechado durante a partida, caso contrário o jogo será finalizado.

Ao abrir os dois terminais você deverá digitar o seguintes comandos

no primeiro terminal:

- $ python server.py

e no segundo terminal:

- $ python client.py

ao colocar a opção de logar no servidor, você deverá informar o IP do servidor que é o localhost sendo assim você deverá informar 

- $ IP: 127.0.0.1
- $ Porta: 50000

caso você deseje alterar o IP do servidor para jogar de outro pc dentro da própria rede é só alterar no código a linha 6, trocando o nome localhost pelo ip de sua máquina. porém deverá manter as aspas simples ''.
