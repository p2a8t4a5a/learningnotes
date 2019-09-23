package main
import "fmt"
import "unsafe"
import (
    // "math"
)

// global var
var (
    a int = 66
    b bool
    x int = 55
)

const(
    C = 999
    D = "aaa"
    DLEN = len(D)
    CLEN = unsafe.Sizeof(C)
    E = iota // 4
    F        // 5
    FF = 100
    FFF     // 也是100
    G = iota // 8 因为前面空了两个空格
)

const(
    // iota 自增长值
    H = 1<<iota // 1<<0
    I = 3<<iota // 3<<1 = 6
    J           // 3<<2 = 12
    K           // 3<<3 = 24
)

const(
    _ = iota // 0
    KB float64 = 1<<(10*iota)
    MB
    GB
    TB
    PB
    EB
    ZB
    YB
)

func showSize() {
    println(KB, MB, GB, TB)
    println(PB, EB, ZB, YB)
}

func showHIJK() {
    println("CLEN:", CLEN)

    println("E,F,FF,FFF,G")
    fmt.Println(E,F,FF,FFF,G)

    println("C,CLEN,D,DLEN")
    fmt.Println(C,CLEN,D,DLEN)
    println("H,I,J,K")
    fmt.Println(H,I,J,K)
}


func testSwitch() {
    switch(1){
        case 1:
            fmt.Println(111)
        case 3:
            fmt.Println(333)
    }
}

func my_func(par []int,size int){
    for i:=0;i<size;i++{
        fmt.Println(i)
    }
}



// ================================================


func test3(a float32,b int)(float32,float32){
    return a,float32(b)
}


type Circle struct{
    radius float64
}
func(a Circle) getArea() float64{return a.radius*a.radius}



// http://www.runoob.com/go/go-pointers.html
func main(){
    // var arr= []int{1,2,3,4}
    // my_func(arr,3)
    // showHIJK()
    // testSwitch()

    showSize()

    /* 
        Array := [3][2]int
        t := Array[1]
        fmt.Println(t)

        var a Circle
        a.radius=2.0
        fmt.Println(a.getArea())

        fmt.Println(test3(2,3))
        my_func := func()func()int{
            var i int=0
            return func() int{
                i+=1
                return i
            }
        }
        temp := my_func()
        fmt.Println(temp())
        fmt.Println(temp())
        fmt.Println(temp())
        fmt.Println(temp())

        numbers := [6]int{1,2,3,4}
        fmt.Println(numbers)
        for i:=range numbers{
            fmt.Printf("%d \n",i)
        }
        var i ,j int ="a",4
        for i<j{
            fmt.Println("123")
            i+=1
        }
        
        fmt.Printf("a,%d\n",123)
        var a int =2147483648
        fmt.Println(a)
        var b * int
        b= &a
        fmt.Printf("%T",b)
        if (1==2){
            fmt.Println(1)
        }else{
            fmt.Println(2)
        }
        if (1==1){
            fmt.Println(3)
        }
        fmt.Println("Hello,Wolrd")
        var age int =10
        var age2 uint8 = 255
        var age3 int64 = 256
        var age4 float64 = 256.0
        var age5 complex64 = 256+2i
        test()
        fmt.Println(a,age,age2,age3,age4,age5)
    */
}










func test(){
    var age byte = 128
    var age2 rune = -128
    var age3 int = -123
    const temp ="aaa"
    a := 10
    a = 100000000000
    fmt.Println(a,age,age2,age3,temp)
}

func test2(){
    var a string = "asd"
    fmt.Println(a)
}
