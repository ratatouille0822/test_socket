from socket import *


def main():
    tcp_server_socket = socket(AF_INET, SOCK_STREAM)
    tcp_server_socket.bind(("", 30000))
    tcp_server_socket.listen(128)
    while True:
        print("等待一个新的客户到来： ")
        client_socket, client_addr = tcp_server_socket.accept()
        print("来了一个新客户")
        order = input("请输入： ")
        if order == "exit":
            break
        print(client_socket)
        print(client_addr)

        receive_data = client_socket.recv(1024)

        print(receive_data.decode("utf-8"))

        client_socket.send("--OK--".encode("gbk"))
        client_socket.close()

    tcp_server_socket.close()


if __name__ == "__main__":
    main()

