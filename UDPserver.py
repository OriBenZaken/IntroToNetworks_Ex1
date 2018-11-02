from socket import socket, AF_INET, SOCK_DGRAM
import sys

def main(argv):
	if (len(argv)!=4):
		exit(1)
	ips_file_name = argv[3]
	content = []
	with open(ips_file_name)as f:
		content = f.readlines()
	# you may also want to remove whitespace characters like `\n` at the end of each line
	content = [x.strip() for x in content]
	ips_dict = {}
	for line in content:
		url, ip = line.split(",")
		ips_dict[url] = ip
	my_port = int(argv[0])
	parent_ip = argv[1]
	parent_port = int(argv[2])
	s = socket(AF_INET, SOCK_DGRAM)
	source_ip = '127.0.0.1'
	source_port = my_port
	s.bind((source_ip, source_port))
	while True:
		url, sender_info = s.recvfrom(2048)
		if (url in ips_dict):
			ip = ips_dict[url]
		else:
			s.sendto(url, (parent_ip, parent_port))
			ip, parent_info = s.recvfrom(2048)
			#write to file
			with open(ips_file_name, 'a') as f:
				f.write("\n" + url + "," +ip)
			#add to dict
			ips_dict[url] =ip
		s.sendto(ip, sender_info)


if __name__ == "__main__":
	main(sys.argv[1:])


