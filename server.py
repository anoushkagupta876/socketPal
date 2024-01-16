from socket import *
import sys
import string

def palindrome_checker(s):
   
  # Removes punctuation and converts to lower case
   s = s.translate(str.maketrans('', '', string.punctuation)).lower()

  # returns true if s and reversed string s are equal
   return s == s[::-1]

def main(argv):
  # Parameter Check
  if len(argv) != 2:
    print('Incorrect command line arguments')
    sys.exit(0)

  try:
    value = int(argv[0])
  except ValueError:
    print("Requested code is not an integer")
    sys.exit(0)

  req_code = argv[0]

  try:
    req_limit = int(argv[1])
  except ValueError:
    print("limit is not an integer")
    sys.exit(0)

  # server socket
  # serverPort = 54819
  serverPort = 0
  serverSocket = socket(AF_INET, SOCK_STREAM)
  serverSocket.bind(('', serverPort))
  n_port = serverSocket.getsockname()[1]
  serverSocket.listen(1)
  # print('The server is ready to receiver')
  
  print(f'SERVER_PORT={n_port}')

  while True:
      # New Request
      connectionSocket, addr = serverSocket.accept()
      recv_code = connectionSocket.recv(1024).decode()

      # Checks for code else close connection
      if recv_code == req_code:
        udpSocket = socket(AF_INET, SOCK_DGRAM)
        # udpSocket.bind(('', 50957))
        udpSocket.bind(('', 0))
        r_port = str(udpSocket.getsockname()[1])
        connectionSocket.send(r_port.encode())

        msg_count = 0
        while msg_count < req_limit:

          # new msg
          message,clientAddress = udpSocket.recvfrom(1024)

          modifiedMessage = message.decode()

          if modifiedMessage == 'EXIT':
             break

          result = 'TRUE' if palindrome_checker(modifiedMessage) else 'FALSE'

          udpSocket.sendto(result.encode(), clientAddress)

          msg_count += 1

        # if while loop stopped because of limit reached
        if msg_count >= req_limit:
          message,clientAddress = udpSocket.recvfrom(1024)
          udpSocket.sendto('LIMIT'.encode(), clientAddress)
      # Close the TCP Connection
      connectionSocket.close()

if __name__ == "__main__":
    main(sys.argv[1:])
    