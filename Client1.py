import socket
HOST = "192.168.56.103"
PORT = 8889

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
               data = b""
               while data != b"\n":
                     data = s.recv(1024)
               move = input('Say Something: ')
               s.sendall(str.encode(move))
               data = b""
               while not data:
                     data = s.recv(1024)
               opponent = data.decode('utf-8')
               print(type(opponent))
               print("Received:", opponent)
               if move == "Rocks":
                       if move == opponent:
                             print( "It's Tie")
                       elif move == 'Rocks' and opponent == 'Scissors':
                             print("You win")
                       elif move == 'Rocks' and opponent == 'Paper':
                             print("You lose")
                       else:
                             print("Invalid move Rocks")
               elif move == 'Paper':
                       if move == opponent:
                             print("It's a Tie")
                       elif move == 'Paper' and opponent == 'Scissors':
                             print("You lose")
                       elif move == 'Paper' and opponent == 'Rocks':
                             print("You win")
                       else:
                             print("Invalid move")
               elif move == 'Scissors':
                       if move == opponent:
                             print("It's a Tie")
                       elif move == 'Scissors' and opponent == 'Paper':
                             print("You win")
                       elif move == 'Scissors' and opponent == 'Rocks':
                             print("You lose")
                       else:
                             print("Invalid move")
               else:
                   print("Invalid Move")
