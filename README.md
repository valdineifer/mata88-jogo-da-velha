# Jogo da Velha

## Visão Geral
O jogo consiste em uma abordagem cliente-servidor, com um jogador abrindo a partida, atuando como servidor, enquanto espera a entrada de outro jogador, que se junta como um cliente.

O servidor faz todo o gerenciamento do jogo, verificando vencedores (ou empate).


## Instalação
No desenvolvimento do projeto, foi utilizada o Python na versão `3.10`. É recomendada a mesma versão ou uma superior, para evitar problemas na execução.

## Estrutura do projeto:
- `client.py`:  
    Código que trata do jogo na visão do cliente e se comunica com o servidor.
- `server.py`:  
    Código que trata do servidor, que gerencia todo o estado do jogo e se comunica com o cliente.

## Fluxo de execução:
1. O host ou servidor deve abrir uma conexão com o comando:
`python3 server.py`
2. Após isso, ele escolher seu símbolo e definir se deseja começar jogando, então aguarda a conexão com um outro jogador, o cliente.
3. O cliente se conecta usando o mesmo endereço com o comando: `python3 client.py`
4. O cliente recebe a informação de qual símbolo deve jogar e uma matriz em branco caso seja o primeiro a jogar ou informando a primeira jogada do oponente.
5. Assim, o jogador deve informar sua jogada no tipo X,Y onde X e Y são números de 0 a 2 indicando, respectivamente, a linha e a coluna, até o jogo se completar com uma vitória para um dos jogadores ou empate.


## Funcionalidades

### Funcionalidades do cliente
O cliente fica apenas com a responsabilidade de pedir a jogada para o usuário e enviar para o servidor, ou seja, tem as seguintes funcionalidades:
- Ler jogada do usuário
- Enviar jogada para o servidor
- Receber dados, processar e mostrar para o usuário o estado atual do jogo

### Funcionalidades do servidor
O servidor faz todo o gerenciamento do jogo, verificando se há algum vencedor ou empate. As funcionalidades são:
- Definir símbolo dos jogadores a partir dos dados do servidor
- Definir quem vai ser o primeiro jogador a partir do dono da sala
- Ler e processar as jogadas do usuário-servidor
- Verificar o ganhador após cada jogada
- Mostrar para os usuários (do cliente e do servidor) o resultado final da partida

## TODO
* Ajustar fluxo do jogo quando o client começa a partida
* Adicionar lobby/salas