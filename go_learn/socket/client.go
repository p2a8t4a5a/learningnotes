package main

import (
    "fmt"
    "time"
    "net"
)

const RECV_BUF_LEN = 1024

func main(){
    conn, err := net.Dial("tcp", "127.0.0.1:6666")
    if err != nil {
        panic(err.Error())
    }
    defer conn.Close()
    buf := make([]byte, RECV_BUF_LEN)
    for i := 0; i<5; i++{
        msg := fmt.Sprintf("Hello, %03d", i) 
        n, err := conn.Write([]byte(msg))
        if err != nil {
            fmt.Println(err.Error())
            break
        }
        fmt.Println("send success:" + msg)

        n, err = conn.Read(buf)
        if err != nil {
            fmt.Println(err.Error())
            break
        }
        fmt.Println("receive success:" + string(buf[0:n]))

        time.Sleep(time.Second * 1)
    }

}
