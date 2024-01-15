# SocketPal: Socket Programming for Palindrome Detection

This repository contains the implementation of a client-server application, named **SocketPal**, developed for an assignment in the Computer Networks course (CS 456/CS 656) at the University of Waterloo. The application is designed to demonstrate introductory socket programming, showcasing the use of both TCP and UDP protocols in a client-server environment.

## Overview

**SocketPal** involves a client sending strings to a server to check if they are palindromes. The server limits the number of messages it processes per client. The communication happens in two stages: negotiation over TCP to obtain a transaction port, and then the actual data exchange over UDP.

### Features

- **TCP-based Negotiation**: Securely negotiate a random port for UDP communication.
- **UDP-based Transactions**: Efficient data transfer for palindrome checking.
- **Request Limiting**: Server-side control over the number of processed requests.
- **Palindromic Validation**: Server checks strings for palindromicity, ignoring case and punctuation.

## Getting Started

### Prerequisites

- Python 3.x or any other compatible programming language.
- Access to a Unix/Linux environment (tested on Ubuntu 20.04 Student CS Machines at the University of Waterloo)

## Usage

Server Setup: Start the server program with the required arguments.
```bash
./server.sh <req_code> <req_lim>
```
Example:
```bash
./server.sh 123 3
```

Client Execution: Run the client program with the necessary parameters.
```bash
./client.sh <server_address> <n_port> <req_code> <msg1> <msg2> ... <msgn>
```
Example:
```bash
./client.sh 127.0.0.1 50899 123 'level' 'hello'
```

The client will connect to the server, negotiate a random port for UDP communication, and then send the specified messages to check for palindromes. The server will respond with 'TRUE' or 'FALSE' for each message, and the client will print these responses.

## Documentation
server.py and client.py: Main server and client programs.
server.sh and client.sh: Shell scripts to run the server and client.
README: This document, detailing setup and usage instructions.

## Testing
Ensure to test both the client and server on different configurations:
Run client and server on two different student.cs machines.
Run both client and server on a single/same student.cs machine.
  
