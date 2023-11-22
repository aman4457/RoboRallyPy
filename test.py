#python
import socket
import pickle
import time
class ProgCard:
    def __init__(self, type, rule):
        self.type = type
        self.rule = rule
def run_client():
    #test = "testing"
    #data = pickle.dumps(test)
    # create a socket object
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    data = ""
    server_ip = "10.1.10.65"  # replace with the server's IP address
    server_port = 8000  # replace with the server's port number
    server_port2 = 8001
    # establish connection with server
    client.connect((server_ip, server_port2))
#    client2.connect((server_ip, server_port2))

    # input message and send it to the server
#    msg = input("Enter message: ")
#    data = pickle.dumps(msg)
    while data != "success":
        data = client.recv(10000000)
        data = pickle.loads(data)
        print(data)
        msg2 = input("enter point num:  ")
        data2 = pickle.dumps(msg2)
        client.send(data2[:1024])
        data3 = client.recv(10000000)
        data3 = pickle.loads(data3)
        msg3 = input(data3 + ":" )
        data4 = pickle.dumps(msg3)
        client.send(data4)
        data = client.recv(10000000)
        data = pickle.loads(data)
        print(data)
    data = client.recv(10000000)
    data = pickle.loads(data)
#    print(data)
    j = 0
    TMP = []
    while j < 5:
        for k in range(len(data)):
             print(str(k+1)+ ":", data[k].rule)
        try:
            inputy = int(input(" Which Program Card: "))
            test = data.pop(inputy - 1)
            print(test.rule)
            TMP.append(test)
            j += 1
        except:
            print("invalid")
    shutdown = 0
    input2 = input("shutdown? y/n")
    if input2 == 'y':
        shutdown = 1
    for k in range(len(TMP)):
        print(TMP[k].rule, end=" ")
        if shutdown == 1:
            TMP[k].rule = "Shutdown"

    print("")
    test =""
    while test =="": 
        test = client.recv(1024)
    client.send(pickle.dumps(TMP))
        # receive message from the server
  #  response = client.recv(1024)
   # response = response.decode("utf-8")

        # if server sent us "closed" in the payload, we break out of the loop and close our socket
  #  if response.lower() == "closed":
  #      endModule()
   #     return

   # print(f"Received: {response}")

    # close client socket (connection to the server)
def endModule():
    client.close()
    print("Connection to server closed")

run_client()


