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



RESTful API 原则:
1. URL定位资源，用HTTP动词（GET,POST,DELETE,DETC）描述操作
    GET     用来获取资源
    POST    用来新建资源(也可以用于更新资源)
    PUT     用来更新资源
    DELETE  用来删除资源

2. 用 HTTP Status Code传递Server的状态信息:
    比如最常用的 200 表示成功，500 表示Server内部错误等。
