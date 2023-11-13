import socket
import pickle


def run_server():
    global client_socket, client_address, server
    # create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = ""
    port = 8000

    # bind the socket to a specific address and port
    server.bind((server_ip, port))
    # listen for incoming connections
    server.listen(0)
    print(f"Listening on {server_ip}:{port}")

    # accept incoming connections
    client_socket, client_address = server.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

    # receive data from the client
    
    request = client_socket.recv(1024)
    request = pickle.loads(request)# convert bytes to string
        
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
