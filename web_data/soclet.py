import socket
'''socket creation->connect to host,port->send command->recv data->decode->close'''

mysoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysoc.connect(('data.pr4e.org', 80))
# till now we have made a call but not data transfer
cm = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

mysoc.send(cm)
count = 0
while True:
    # 512 is the amount of cycle recieved in every cycle
    data = mysoc.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
    count += 1
mysoc.close()
# we know that 512 is the datat we recieve in one cycle
# ALSO the file we aare recieve has 536 bytes therefor count will be according
print(count)
