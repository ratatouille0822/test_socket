# TCP 客户端的练习
import socket


def main():
    # 1. 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # tcp_socket.bind("", 3100)
    # 2. 连接服务器
    server_ip = input("请输入服务器ip： ")
    server_port = int(input("请输入端口： "))
    server_addr = (server_ip, server_port)
    tcp_socket.connect(server_addr)
    # 3. 收发信息
    while True:
        send_data = input("请输入要发送的数据： ")
        if send_data == "exit":
            break
        tcp_socket.send(send_data.encode("gbk"))

    # 4. 关闭套接字
    tcp_socket.close()


if __name__ == "__main__":
    main()
