package main
import (
    "fmt"
    "io/ioutil"
    "person"
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

func TestMap() {
    m := make(map[string]int)
    m["a"] = 123
    m["b"] = 456
    fmt.Println(m)
}


func increment(i *int) {
      *i++
}

func TestPoint() {
    a:=1
    increment(&a)
    fmt.Println(a)
    fmt.Println(*(&a))
}

func TestIF() {
    if num:=1; num<0 {
        fmt.Println(num, "num < 0")
    } else if num < 1 {
        fmt.Println(num, "num = 0")
    } else {
        fmt.Println(num, "num > 0")
    }
}

func SwitchMain() {
    i := 3
    switch i {
        case 1:
            fmt.Println(i, "num = 1")
        case 2:
            fmt.Println(i, "num = 2")
        default:
            fmt.Println(i, "num other ")
    }
}

func TestLoop() int {
    sum := 0
    for i:=0; i<10 ; i++ {
        fmt.Println(i, "num")
        sum += i
    }

    i := 0
    for i < 10 {
        fmt.Println(i)
        i += 1
    }

    for {
        i+=1
        if i>12 {
            break
        } else {
            fmt.Println(i)
        }
    }

    return sum
}


func TestAdd1(a int, b int) int {
    return a+b
}

func TestAdd2(a int, b int) (c int) {
    c = a+b
    return
}

func TestMultiReturn() (a int, b string) {
    a = 1 + 1
    b = "asd"
    return a,b
}

func TestFunc() {
    fmt.Println(TestAdd1(1,2) == TestAdd2(1,2))
    a,b := TestMultiReturn()
    fmt.Println(a,b)
}

type person struct {
    name string 
    age int
    gender string
}

type person2 struct {
    name string 
    age int
    gender string
}

func TestStruct() {
    a := person{name: "Bob", age: 42, gender: "male"}
    b := person{"Bob", 42, "male"}
    fmt.Println(a.name)
    fmt.Println(b.age)
    p := &a
    fmt.Println(p.gender)
}


func (p *person) changeAge(age int) {
    fmt.Println(p)
    p.age = age
}

func (p *person2) changeAge(age int) {
    p.age = age
    fmt.Println(p)
}

func (p person) changeName(name string) {
    // will not change name
    p.name = name
}

func TestMethod() {
    a := person{"bob", 13, "male"}
    fmt.Println(a)
    a.changeAge(14)
    a.changeName("alice")
    fmt.Println(a)

    b := person2{"bob", 13, "male"}
    b.changeAge(15)
}



type animal interface {
    description() string
}

type cat struct {
    Type string
    Sound string
}
type snake struct {
    Type string
    Poisonous bool
}

func (c cat) description() string{
    fmt.Println("i am cat", c)
    return ""
}

func (s snake) description() string{
    fmt.Println("i am snake", s)
    return ""
}

func TestInterface() {
    var a animal
    a = cat{Sound:"aaa"}
    a.description()

    a = snake{Poisonous: true}
    a.description()
}

func main() {
    // TestAppend()
    // TestCopy()
    // tmp := TestMemory()
    // fmt.Println(tmp)
    // TestMap()
    // TestPoint()
    // TestIF()
    // SwitchMain()
    // TestLoop()
    // TestFunc()
    // TestStruct()

    // TestMethod()
    TestInterface()

    // mark METHODS
    // https://milapneupane.com.np/2019/07/06/learning-golang-from-zero-to-hero
}
