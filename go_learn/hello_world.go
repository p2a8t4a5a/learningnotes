package main
import "fmt"
import "unsafe"
import (
    // "math"
)

var (
    a int = 66
    b bool
)

const(
    C = 999
    D = "aaa"
    DLEN = len(D)
    CLEN = unsafe.Sizeof(C)
    E = iota
    F
    FF = 100
    FFF
    G = iota

)
const(
    H = 1<<iota
    I = 3<<iota
    J
    K
)

func test3(a float32,b int)(float32,float32){
    return a,float32(b)
}


type Circle struct{
    radius float64
}
func(a Circle) getArea() float64{return a.radius*a.radius}


func my_func(par []int,size int){
    for i:=0;i<size;i++{
        fmt.Println(i)
    }
}

// http://www.runoob.com/go/go-pointers.html
func main(){
    var arr= [4]int{1,2,3,4}
    my_func(arr,3)
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
        
        fmt.Println(H,I,J,K)
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
        switch(3){
            case 1:
                fmt.Println(111)
                break
            case 3:
                fmt.Println(333)
        }
        fmt.Println(E,F,FF,FFF,G)
        fmt.Println(C,CLEN,D,DLEN)
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
