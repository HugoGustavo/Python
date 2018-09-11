import socket;

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

# get local machine name
host = socket.gethostname();

port = 9999

# bind to the port
server_socket.bind((host,port));

#queue up to 5 request
server_socket.listen(5);

while True:
    # estabilish a connection
    client_socket, address = server_socket.accept();

    print("Got a connection from", str(address));

    mensagem = 'Thank you for connecting ' + "\r\n";
    client_socket.send(mensagem.encode('ascii'));
    client_socket.close();
    