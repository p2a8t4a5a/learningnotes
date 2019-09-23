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

func showArray() {
    // is ok
    // var Array [3][2]int
    // is ok
    // Array := [3][2] int{ [2]int{1, }, }
    Array := [3][2] int{}
    t := Array[0]
    fmt.Println(t)
}


func showCircle() {
    var a Circle
    a.radius=1.0
    fmt.Println(a.getArea())
}

type Circle struct{
    radius float64
}

func(a Circle) getArea() float64{return 3.14 * a.radius*a.radius}


// ================================================
func test3(a float32,b int)(float32,float32){
    return a,float32(b)
}

func showParse(){
    fmt.Println(test3(2,3))
}

func showFuncReturn(){
    my_func := func() func() int{
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
}


func showArray2() {
    numbers := [6]int{1,2,3,4}
    fmt.Println(numbers)
    for i:= range numbers{
        fmt.Printf("%d \n", i)
    }
}

func showFor(){
    var i ,j int = 0,4
    for i<j {
        fmt.Println("123")
        i+=1
    }
}

func showInt() {
    var a int = 2147483648
    fmt.Println(a)
    fmt.Println(unsafe.Sizeof(a))
    var b * int
    b= &a
    println(b) // value
    fmt.Printf("%T",b) // type
}
func showIf(){
    if (1==2){
        fmt.Println(1)
    }else{
        fmt.Println(2)
    }
}

func main(){
    // var arr= []int{1,2,3,4}
    // my_func(arr,3)
    // showHIJK()
    // testSwitch()
    // showSize()
    // showArray()
    // showCircle()
    // showParse()
    // showFuncReturn()
    // showArray2()
    // showFor()
    // showInt()
    showIf()

}
