import socket

ip = raw_input("Digite o Ip ou endereço:")

ports = []
count = 0

while count < 10:
    ports.append(int(raw_iput("Digite a porta:")))
    count += 1


for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeount(0.05)
    code = client.connect_ex((ip, port))

    if code == 0:
        print str(port) + " -> Porta Aberta"
    else:
        print str(port) + " -> Porta fechada"

print "Scan Finalizado"
