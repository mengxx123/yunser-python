# -- coding: utf-8 --

import ssl
import socket
from OpenSSL import crypto

web_url = 'https://app.yunser.com'
# 这是什么
context = ssl.SSLContext(ssl.PROTOCOL_TLS)
# 建立 socket 连接   
# socket.AF_INET 为 IPv4 网络协议的套接字类型
sock = socket.socket(socket.AF_INET)
# 设置超时时间 10s
sock.settimeout(10)
wrappedSocket = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=web_url

try:
    wrappedSocket.connect(web_url, 443))
    # 获取 ssl 证书公钥
    pem_cert = ssl.DER_cert_to_PEM_cert(wrappedSocket.getpeercert(True))
    wrappedSocket.close()
    # 解密公钥
    io_cert = crypto.load_certificate(crypto.FILETYPE_PEM, pem_cert)
    # 证书过期时间
    ssl_time = io_cert.get_notAfter().decode()[:-1]
    ssl_not_after = ssl_time[0:4] + '年' + ssl_time[4:6] + '月' + ssl_time[6:8] + '日' + ssl_time[8:10] + '时' + ssl_time[10:12] + '分' + ssl_time[12:14] + '秒'
    # 证书有效状态
    ssl_expired = io_cert.has_expired()
    
    return True;

except Exception as e:

    # 连接失败，输出错误原因
    print(e)
    return False;