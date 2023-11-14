import socket
import pickle
#server_ip = ""
startingPort = 8000
NumOfRobots = 1

for i in range(NumOfRobots):
    dynamic_var_name = "botServer" + str(i)
    port = startingPort + i
    server_ip = ""
    globals()[dynamic_var_name] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    globals()[dynamic_var_name].bind((server_ip, port))
    globals()[dynamic_var_name].listen(0) 
    print(f"Listening on {server_ip}:8000")
    # accept incoming connections
    client_socket, client_address = globals()[dynamic_var_name].accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
    request = pickle.dumps("test")
    client_socket.send(request[:10000000])


#for i in range(NumOfRobots):
#dynamic_var_name = "botServer" + str(i)
#botServer0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#port = startingPort + 0
#botServer0.bind((server_ip, port))
#print(port)
#botServer0.listen(0)
#client_socket, client_address = botServer0.accept()
#print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
#test = pickle.dumps("tests")
#botServer0.send(test[:10000000])