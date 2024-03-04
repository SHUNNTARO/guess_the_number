import socket

# UNIXドメインソケットとデータグラム（非接続）ソケットを作成します
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

# サーバのアドレスを定義します。
# サーバはこのアドレスでメッセージを待ち受けます
server_address = '/upd_socket_file'

# このクライアントのアドレスを定義します。
# サーバはこのアドレスにメッセージを返します
address = '/upd_client_socket_file'

# サーバに送信するメッセージを定義します
message = input('Hello world!!\n')

# このクライアントのアドレスをソケットに紐付けます。
# これはUNIXドメインソケットの場合に限ります。
# このアドレスは、サーバによって送信元アドレスとして受け取られます。
sock.bind(address)

try:

    # サーバにメッセージを送信します
    print('sending {!r}'.format(message))
    sent = sock.sendto(message, server_address)

    # サーバからの応答を待ち受けます
    print('waiting to receive')

    # 最大4096バイトのデータを受け取ります
    data, sever = sock.recvfrom(4096)


    # サーバから受け取ったメッセージを表示します
    print('recive {!r}'.format(data))


    # 最後にソケットを閉じてリソースを解放します

finally:
    print('closing socket')
    sock.close()