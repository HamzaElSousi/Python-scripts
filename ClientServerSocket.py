import socket
import threading

class Server:
    def __init__(self, port):
        self.serverPort = port
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.bind(('localhost', self.serverPort))
        self.serverSocket.listen(1)
        print("Server listening on port", self.serverPort)
        
    def waitForConnection(self):
        self.connection, _ = self.serverSocket.accept()
        print("Connected to client")

    def getStream(self):
        self.input = self.connection.makefile('r')
        self.output = self.connection.makefile('w')

    def processConnection(self):
        while True:
            data = self.input.readline()
            if not data:
                break
            response = "Server received: " + data
            self.output.write(response)
            self.output.flush()
            
    def closeConnection(self):
        self.connection.close()

    def runServer(self):
        self.waitForConnection()
        self.getStream()
        self.processConnection()
        self.closeConnection()

class Client:
    def __init__(self, host, port):
        self.serverPort = port
        self.hostServer = host
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def connectToServer(self):
        self.connection.connect((self.hostServer, self.serverPort))
        print("Connected to server")

    def getStream(self):
        self.input = self.connection.makefile('r')
        self.output = self.connection.makefile('w')

    def processConnection(self):
        while True:
            message = input("Enter message: ")
            if not message:
                break
            self.output.write(message + "\n")
            self.output.flush()
            response = self.input.readline()
            print("Server response:", response)
            
    def closeConnection(self):
        self.connection.close()

    def runClient(self):
        self.connectToServer()
        self.getStream()
        self.processConnection()
        self.closeConnection()

def main():
    server = Server(12345)
    client = Client('localhost', 12345)
    
    server_thread = threading.Thread(target=server.runServer)
    client_thread = threading.Thread(target=client.runClient)
    
    server_thread.start()
    client_thread.start()

if __name__ == "__main__":
    main()
