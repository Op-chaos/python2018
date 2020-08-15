import socket

def main():
    # 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定本地信息, 发送数据可以不先绑定端口
    udp_socket.bind(("", 7890))

    while True:

        # 从键盘获取数据
        send_data = input("请输入要发送的数据：")

        # 可以使用套接字收发数据
        # udp_socket.sendto("hahahah", 对方的ip以及port)
        # udp_socket.sendto(b"hahahah------1----", ("接收方ip：10.4.130.161", 8080))
        udp_socket.sendto(send_data.encode("utf-8"), ("192.168.34.169", 8080))


    # 关闭套接字
    udp_socket.close()
	

if __name__ == "__main__":
    main()