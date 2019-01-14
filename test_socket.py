import socket


def udp_receive(socket_recv):
    receive_bytes = socket_recv.recvfrom(1024)
    print("%s" % receive_bytes[0].decode("gbk"))


def udp_send(socket_send):
    str_send = input("请输入： ")
    socket_send.sendto(str_send.encode("utf-8"), ("192.168.31.156", 6667))


def main():

    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    local_addr = ("", 6777)
    udp_socket.bind(local_addr)
    while True:
        udp_send(udp_socket)
        udp_receive(udp_socket)

# while True:
#     test_to_send = input("please input :")
#     udp_socket.sendto(test_to_send.encode("utf-8"), ("192.168.31.156", 6667))
#
#     if test_to_send == "exit":
#         exit()
# 套接字关闭


if __name__ == "__main__":
    main()

