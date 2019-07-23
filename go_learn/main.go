package main
import (
    "fmt"
    "io/ioutil"
)


func AppendByte(slice []byte, data ...byte) []byte {
    m := len(slice)
    n := m + len(data)
    fmt.Println(len(data))
    if n > cap(slice) {
        t := make([]byte, len(slice), (cap(slice) +1)*2)
        copy(t, slice)
        slice = t
    }
    slice = slice[0:n]
    copy(slice[m:n], data)
    return slice

    // for i:= range data:
}

func TestAppend() {
    a := make([]byte, 5, 10)
    b := AppendByte(a, 7, 11)
    fmt.Println("Hello World~")
    a = a[:6]
    fmt.Println(a[5])
    fmt.Println(b[5])
    fmt.Println(a)
    fmt.Println(len(a))
    fmt.Println(cap(a))

}

func TestCopy() {
    a := []byte{1,2}
    a = append(a, 3)
    b := []byte{4,5,6}
    copy(a, b)
    fmt.Println(a)
    fmt.Println(b)
    fmt.Println(len(a))
    fmt.Println(len(b))
}

func Change(b [4]int) [4] int{
    b[0] = 9
    return b
}

func TestArray() {
    a := [...]int{1,2,3,4}
    fmt.Println(a)
    b := Change(a)
    fmt.Println(a)
    fmt.Println(b)
}

func TestMemory() string {
    // xxxHello,World
    a,_ := ioutil.ReadFile("data.in")
    res := make([]byte, 0, len(a)-3)
    res = append(res, a[3:]...)
    return string(res)
}

func main() {
    // TestAppend()
    // TestCopy()
    tmp := TestMemory()
    fmt.Println(tmp)
}
