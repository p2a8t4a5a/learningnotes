package main
import "fmt"
import "unsafe"

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


func main(){
    fmt.Println(H,I,J,K)
    /* 
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
