import socket
import pickle


def run_server():
    global client_socket, client_address, server
    # create a socket object
    botserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    botserver2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = ""
    port1 = 8000
    port2 = 8001

    # bind the socket to a specific address and port
    server.bind((server_ip, port1))
    server2.bind((server_ip, port2))
    # listen for incoming connections
    server.listen(0) 
    print(f"Listening on {server_ip}:{port1}")

    # accept incoming connections
    client_socket, client_address = server.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

    server2.listen(0) 
    print(f"Listening on {server_ip}:{port2}")

    # accept incoming connections
    #client_socket2, client_address2 = server2.accept()
    #print(f"Accepted connection from {client_address2[0]}:{client_address2[1]}")
    # receive data from the client
    
    request = client_socket.recv(1024)
    request = pickle.loads(request)# convert bytes to string
    print(f"Received: {request}")
    
    #request = client_socket2.recv(1024)
    #request = pickle.loads(request)# convert bytes to string
    #print(f"Received: {request}")
        
        # if we receive "close" from the client, then we break
        # out of the loop and close the conneciton
    if request.lower() == "close":
            # send response to the client which acknowledges that the
            # connection should be closed and break out of the loop
        client_socket.send("closed".encode("utf-8"))
        closeSocket()
        return
    print(f"Received: {request}")

    response = "accepted".encode("utf-8") # convert string to bytes
        # convert and send accept response to the client
    client_socket.send(response)

def closeSocket():
        # close connection socket with the client
        client_socket.close()
        print("Connection to client closed")
        # close server socket
        server.close()


run_server()
