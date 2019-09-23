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

func test2() {
    a := []int{1,2,3}
    b := a[:]
    println(a[2])
    a[2] = 99
    println(b[2])
}

func test3() {
    a := make([]int, 2, 4)
    a = append(a, 2)
    for i:=0;i<100;i++ {
        a = append(a, 3)
    }
    for i:=0;i<len(a);i++ {
        println(a[i])
    }
    println(len(a))
    println(cap(a))
}

func test4() {
    a := 2
    println(a)
    switch a {
        case 1:
            println("aa")
        case 2:
            println("bb")

    }
}

func main() {
    // a,b := test()
    // fmt.Println(a, b)
    test4()
}
