from socket import *
import sys

def main(argv):
  # Parameter Check
  if len(argv) < 4:
    print('Incorrect command line arguments')
    sys.exit(0)

  serverAddress = argv[0]
  try:
    n_port = int(argv[1])
  except ValueError:
    print("server_port is not an integer")
    sys.exit(0)

  req_code = argv[2]
  msg_count = len(argv) - 3

  # TCP Connection
  clientSocket = socket(AF_INET, SOCK_STREAM)
  clientSocket.connect((serverAddress, n_port))
  clientSocket.send(req_code.encode())

  r_port = clientSocket.recv(1024).decode()

  # If r_port is successfully received
  if r_port and r_port != '':

    # UDP Socket
    udpSocket = socket(AF_INET, SOCK_DGRAM)
    limitReached = False

    for i in range (0, msg_count):

      udpSocket.sendto(argv[i + 3].encode(), ('', int(r_port)))
      message, clientAddress = udpSocket.recvfrom(1024)

      modifiedMessage = message.decode()

      if modifiedMessage != 'LIMIT':
        if i:
          print('', end=', ')

        print(modifiedMessage, end='')
      else: 
        limitReached = True
        if i:
          print('', end=', ')

        print('Request limit reached')
        break

    if limitReached == False:
      print('')
      udpSocket.sendto('EXIT'.encode(), ('', int(r_port)))
  
  clientSocket.close()
    
if __name__ == '__main__':
  main(sys.argv[1::])