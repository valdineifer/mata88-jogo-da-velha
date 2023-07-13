import socket, pickle

HOST = ''
PORT = 1142
address = (HOST, PORT)

matrix = [
  [' ', ' ', ' '],
  [' ', ' ', ' '],
  [' ', ' ', ' ']
]

symbol = ''

def deserialize_matrix(data):
  return pickle.loads(data)


def print_matrix():
  global matrix

  print("+---+---+---+")
  for row in matrix:
    print('|{}|{}|{}|'.format(row[0].center(3, ' '), row[1].center(3, ' '), row[2].center(3, ' ')))
    print("+---+---+---+")


def play():
  print_matrix()

  position = ''

  while True:
    position = input('Qual será sua jogada (linha, coluna)? Ex: 1,2. ').split(',')
    
    if (len(position) != 2):
      continue
    
    x,y = [int(position[0]), int(position[1])]

    if matrix[x][y] != ' ':
      continue
  
    return x,y


def main():
  global matrix

  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  client.connect(address)

  data = client.recv(1024)
  symbol = data.decode("utf-8")
  
  print(f'Você jogará com o símbolo: {symbol}')
  
  
  while True:    
    data = client.recv(4096)

    if (len(data) == 1):
      winner = data.decode("utf-8")

      if winner == ' ':
        print('\nDeu empate!')
      else:
        print(f'\nO vencedor foi: {winner}')

      client.close()
      break

    matrix = deserialize_matrix(data)

    x,y = play()

    text = f"{x},{y}"
      
    client.send(text.encode('utf-8'))


main()