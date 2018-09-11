import socket;

# create socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

# get local machine name
host = socket.gethostname();

port = 9999;

# connection to host on port
sock.connect((host, port));

# Receive no more than 1024 bytes
mensagem = sock.recv(1024);

sock.close();
print(mensagem.decode('ascii'));
