package main

import (
    "net"
    "fmt"
    "io"
)

const RECV_BUF_LEN = 1024

func main() {
    listener, err := net.Listen("tcp", "0.0.0.0:6666")
    if err != nil {
        panic("err listen:" + err.Error())
    }
    fmt.Println("start server")

    for {
        conn, err := listener.Accept()
        if err != nil {
            panic("Error accept:" + err.Error())
        }
        fmt.Println("accept connection:", conn.RemoteAddr())
        go EchoServer(conn)
    }
}

func EchoServer(conn net.Conn) {
    buf := make([]byte, RECV_BUF_LEN)
    defer conn.Close()
    for {
        n,err := conn.Read(buf)
        switch err {
            case nil:
                conn.Write(buf[0:n])
            case io.EOF:
                fmt.Println("End of data:" +err.Error())
                return
            default:
                fmt.Println("Error reading data:" +err.Error())
                return
        }
    }
}

