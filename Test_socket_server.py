from socket import *


def main():
    tcp_server_socket = socket(AF_INET, SOCK_STREAM)
    tcp_server_socket.bind(("", 30000))
    tcp_server_socket.listen(128)
    print("*" * 50)
    client_socket, client_addr = tcp_server_socket.accept()
    print("*" * 50)
    print(client_socket)
    print(client_addr)

    receive_data = client_socket.recv(1024)

    print(receive_data)

    client_socket.send("--OK--".encode("gbk"))


if __name__ == "__main__":
    main()

