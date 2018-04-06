# 查看域名解析(MAC下)
$dig +noall +answer wantjr.com
wantjr.com.     464 IN  A   192.30.252.154
wantjr.com.     464 IN  A   192.30.252.153

# 反向查看域名
nslookup 10.0.0.5

# 查看端口情况
netstat -tulpn

# 查看80
lsof -i tcp:80
