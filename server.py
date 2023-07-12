import socket, pickle

HOST = ''
PORT = 1142
address = (HOST, PORT)

server = None

matrix = [
  [' ', ' ', ' '],
  [' ', ' ', ' '],
  [' ', ' ', ' ']
]

symbol = ''
rounds = 0


def print_matrix():
  print("\n+---+---+---+")
  for row in matrix:
    print('|{}|{}|{}|'.format(row[0].center(3, ' '), row[1].center(3, ' '), row[2].center(3, ' ')))
    print("+---+---+---+")


def check_winner():
  global total_jogadas

  for s in ['X','O']:
    for i in range(0,3):
      if len(set(matrix[i])) == 1 and matrix[i][0] == s:
        return s
      
      if matrix[0][i] == matrix[1][i] == matrix[2][i] and matrix[0][i] == s:
        return s

    diagonal = matrix[0][0] == s and matrix[1][1] == s and matrix[2][2] == s
    diagonal = diagonal or (matrix[0][2] == s and matrix[1][1] == s and matrix[2][0] == s)   
    if diagonal:
      return s

    if rounds == 9:
      return None
    
  return ''


def check_endgame(connection: socket.socket):
  global server
  winner = check_winner()
  text = ''

  if (winner == ''):
    return None

  if winner is None:
    text = '\nDeu empate!'
  else:
    text = f'\nO vencedor foi: {winner}'

  print(text)
  connection.send(winner.encode('utf-8') if winner is not None else ' '.encode('utf-8'))
  connection.close()
  server.close() # type: ignore
  exit()


def play():
  print_matrix()

  global rounds
  position = ''

  while True:
    position = input('Qual será sua jogada (linha, coluna)? Ex: 1,2: ').split(',')
    
    if (len(position) != 2):
      continue
    
    x,y = [int(position[0]), int(position[1])]

    if matrix[x][y] != ' ':
      continue

    matrix[x][y] = symbol
    rounds += 1
    break


def serialize_matrix():
  global matrix

  return pickle.dumps(matrix)


def main():
  global symbol
  global rounds
  global server
  server_first = None
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  server.bind(address)
  server.listen(1)

  while symbol != 'X' and symbol != 'O':
    symbol = input('Escolha X ou O: ').upper()

  while server_first != 'S' and server_first != 'N':
    server_first = input('Deseja ser o primeiro a jogar? (S/N): ').upper()

  print('Aguardando conexão com o oponente...')

  connection, client = server.accept()

  print('Conectado com', client)

  connection.send(('X' if symbol == 'O' else 'O').encode('utf-8'))

  print('Iniciando partida...')

  if server_first == 'S':
    play()
  
  while True:
    print('Aguardando jogada do oponente...')

    connection.send(serialize_matrix())

    data = connection.recv(3)

    x,y = data.decode('utf-8').split(',')

    matrix[int(x)][int(y)] = 'O' if symbol == 'X' else 'X'
    rounds += 1

    print(f'O oponente jogou: {data.decode("utf-8")}.')

    check_endgame(connection)

    play()

    check_endgame(connection)


main()