from socket import socket, AF_INET, SOCK_DGRAM
import sys

def main(argv):
	if (len(argv)!=2):
		exit(1)

	s = socket(AF_INET, SOCK_DGRAM)
	dest_ip = argv[0]
	dest_port = int(argv[1])
	msg = raw_input()
	while not msg == 'quit':
		s.sendto(msg, (dest_ip, dest_port))
		data, sender_info = s.recvfrom(2048)
		print(data)
		msg = raw_input()
	s.close()

if __name__ == "__main__":
	main(sys.argv[1:])


