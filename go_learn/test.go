package main

import "fmt"


func test() (num int, err error) {
    // fmt.Println("reached fmt.Println")
    //  会是倒序输出
    defer fmt.Println("defer reached fmt.Println 1")
    defer fmt.Println("defer reached fmt.Println 2")
    defer fmt.Println("defer reached fmt.Println 3")
    return
}

func main() {
    a,b := test()
    fmt.Println(a, b)
}
