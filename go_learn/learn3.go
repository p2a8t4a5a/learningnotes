package main
import (
    "fmt"
    "io/ioutil"
    "encoding/json"
    "net/http"
    "errors"
    "time"
    "math/rand"
    "runtime"
    "sync"
    "sync/atomic"
	"os"
    "strings"
    "os/exec"
    "flag"
    "reflect"
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
}

func TestAppend() {
    a := make([]byte, 5, 10)
    // b := append(a, 7, 11)
    b := AppendByte(a, 7, 11) // equals append
    fmt.Println("Hello World~")
    a = a[:6] // 改变了a的长度，因为实际a和b是共享内存的
    fmt.Println(a[5])
    fmt.Println(b[5])
    fmt.Println(a)
    fmt.Println(b)
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
    a, _ := ioutil.ReadFile("data/data.in")
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
    p.age = age
    fmt.Println(p)
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

    animals := []animal{&cat{Sound:"aaa"}, &snake{Poisonous: true}}
    for _, ani := range animals{
        ani.description()
    }
}

func TestJsonMarshal() {
    mapA := map[string]int{"name": 337, "age": 10}
    mapB, _ :=  json.Marshal(mapA)
    fmt.Println("type:", reflect.TypeOf(mapB))
    fmt.Println(mapB)
    fmt.Println(string(mapB))
}

type response struct {
    Name string `json:"name"`
    Age int `json:"age"`
    hobby string
}

func TestJsonUnmarshal() {
    // raw_str := `{\"name\":\"bob\", \"age\":13}`
    raw_str := `{"name":"bob", "age":13}`
    fmt.Println("type", reflect.TypeOf(raw_str))
    res := response{hobby:"code"}
    err := json.Unmarshal([]byte(raw_str), &res)
    if err == nil {
        fmt.Println(res)
    } else {
        fmt.Println(err)
    }
}

func TestErrorHandle() {
    resp, err := http.Get("http://baidu.com")
    if err != nil {
        fmt.Println(err)
        return
    }
    fmt.Println(resp)
}

func Add(num int) (int, error) {
    if num < 4 {
        return num, errors.New("Error: bigger or equal than 4")
    } else {
        return num + 1, nil
    }
}

func TestErrorHandle2() {
    num := 3
    if res, err := Add(num) ; err != nil {
        fmt.Println(err)
    } else {
        fmt.Printf("res: %v", res)
    }
}

 func TestPanicAndCatch() {
     f()
     fmt.Println("Returned normally from f.")
 }

 func f() {
     defer func() {
         if r := recover(); r != nil {
             fmt.Println("Recovered in f", r)
         }
     }()
     fmt.Println("Calling g.")
     g(0)
     fmt.Println("Returned normally from g.")
 }

 func g(i int) {
     if i > 3 {
         fmt.Println("Panicking!")
         panic(fmt.Sprintf("this is a panic: %v", i))
     }
     defer fmt.Println("Defer in g", i)
     fmt.Println("Printing in g", i)
     g(i + 1)
 }

 func TestGo() {
     go c()
     fmt.Println("I am main")
     time.Sleep(time.Second * 3)
 }

 func c() {
     time.Sleep(time.Second * 2)
     fmt.Println("I am concurrent")
 }

 // Golang prefers not sharing the variables of one thread with another 
 // because this adds a chance of deadlock and resource waiting. 
 // There is another way to share resources between Go routines: via go channels.

func TestChannel() {
    c := make(chan string)
    go func() {  time.Sleep(time.Second * 5); c <- "hello"; }()
    fmt.Println("before msg")
    msg := <-c
    fmt.Println(msg)
}

func sc(ch chan<- string) {
    ch <- "hello, this is a send only type"
}

func TestOneWayChannel() {
    ch := make(chan string)
    go sc(ch)
    fmt.Println(<-ch)
}

func TestFirstArrive() {
    c1 := make(chan string)
    c2 := make(chan string)
    go speed1(c1)
    go speed2(c2)
    fmt.Println("The first to arrive is:")
    select {
		case s1 := <-c1:
			fmt.Println(s1)
		case s2 := <-c2:
			fmt.Println(s2)
    }
}

func speed1(ch chan string) {
    time.Sleep(5 * time.Second)
    ch <- "speed 1"
}

func speed2(ch chan string) {
    time.Sleep(1 * time.Second)
    ch <- "speed 2"
}

func consume(ch chan string, t time.Duration) {
	time.Sleep( t * time.Second)
    showMsgImm("Recived", <-ch)
}

func TestBufferChannel() {
	ch := make(chan string, 2)
	go consume(ch, 3)
	go consume(ch, 5)
	go consume(ch, 7)
	ch <- "aaa";
	ch <- "bbb";
    showMsgImm("success send aaa, bbb")
	ch <- "ccc";
    showMsgImm("success send ccc")
	ch <- "ddd";
    showMsgImm("success send ddd")
	ch <- "eee";
    showMsgImm("success send eee")
}



func testDefer() (num int, err error) {
    // fmt.Println("reached fmt.Println")
    //  会是倒序输出
    defer fmt.Println("defer reached fmt.Println 1")
    defer fmt.Println("defer reached fmt.Println 2")
    defer fmt.Println("defer reached fmt.Println 3")
    return
}

func testPanic(){
    defer fmt.Println("defer fmt.Println 405")
    defer func(){ if r:=recover();r !=nil{
        fmt.Println(r)
    }}()


    if true {
        panic("no value for $USER")
    }
}

func subRoutine(name string, delay time.Duration, ch chan string) {
    t0 := time.Now()
    fmt.Printf("name:%s, start:%s, delay:%s\n", name, t0, delay* time.Second)

    time.Sleep(delay * time.Second)

    t1 := time.Now()
    fmt.Printf("name:%s, end:%s\n", name, t1)
    fmt.Printf("name:%s, used:%s\n", name, t1.Sub(t0))
    ch <- "a"
}

func testRoutine() {
    ts := time.Now().Unix()
    rand.Seed(ts)
    var name string
    ch := make(chan string)
    n := 5
    for i:=0; i<n; i++ {
        name = fmt.Sprintf("go_%02d", i)
        // 0-4 s
        // go subRoutine(name, time.Duration(rand.Intn(5)), ch)
        go subRoutine(name, 3, ch)
        // 默认不是真正的并发
    }
    for i:=0; i<n; i++ {
        <-ch
    }
}

func doSomeThingHard(n int, thread string, ch chan string) (sum int){
    t0 := time.Now()
    for i:=0; i<n; i++{
        sum += i
    }
    fmt.Printf("sum:%d, thread:%s, time used:%s\n", sum, thread, time.Now().Sub(t0))
    os.Stdout.Sync()

    ch <- thread
    return
}

func testCPU() {
    // 限制最大核数, 默认为CPU的个数
    runtime.GOMAXPROCS(5)
    t0 := time.Now()
    n := 20000000000
    ch := make(chan string)
    go doSomeThingHard(n, "1", ch)
    go doSomeThingHard(n, "2", ch)
    go doSomeThingHard(n, "3", ch)
    go doSomeThingHard(n, "4", ch)
    go doSomeThingHard(n, "5", ch)
    for i:=0 ; i< 5; i++ {
        <-ch
    }
    fmt.Println(time.Now().Sub(t0))
}

func testSellTicket() {
    // mutex := sync.Mutex{}
    var mutex sync.Mutex
    mutex.Lock()
    fmt.Println("123")
    mutex.Unlock()
}

func testAtomic() {
    var cnt uint32
    for i:=0; i< 100 ; i++ {
        go func() {
            for j:=0; j<2000; j++ {
                // time.Sleep(time.Millisecond)
                // cnt ++
                atomic.AddUint32(&cnt, 1)
            }
        }()
    }
    time.Sleep(time.Second)
    cntFinal := atomic.LoadUint32(&cnt)
    fmt.Println("cnt", cnt)
    fmt.Println("cntFinal", cntFinal)
}

func PrintlnWithSequence(strs ...string) {
	fmt.Println(strs)
}

func showMsgImm(msg string, a ...interface{}){
    // fmt.Println("Type", reflect.TypeOf(a))
    if len(a) > 0 {
        fmt.Println(msg, a)
    } else {
        fmt.Println(msg)
    }
    os.Stdout.Sync()
}

func TestChannel2(){
	channel := make(chan string) //注意: buffer为0
    go func() {
        channel <- "hello"
        showMsgImm("write \"hello\" done!")

        channel <- "World" //Reader在Sleep，这里在阻塞
        showMsgImm("write \"World\" done!")

        time.Sleep(3*time.Second)
        showMsgImm("after sleep 3s...")

        channel <- "channel"
        showMsgImm("after send \"channel\" done!")
    }()

    showMsgImm("start...")
    time.Sleep(2*time.Second)
    showMsgImm("Reader Wake up...")

    msg := <-channel
    showMsgImm("Reader: ", msg)

    msg = <-channel
    showMsgImm("Reader: ", msg)

    msg = <-channel //Writer在Sleep，这里在阻塞
    showMsgImm("Reader: ", msg)
}

func TestChannelTimeout(){
	ch := make(chan string)
	go func() {
		time.Sleep(5 * time.Second)
		ch <- "finished success"
	}()
	select {
		case msg:= <-ch:
			fmt.Println(msg)
		case <- time.After(3 * time.Second):
			fmt.Println("timeout")
	}
}

func TestChannelClose(){
	// 会根据返回的不同调整返回策略
	ch := make(chan string)
	go func() {
		for i:=0; i<3; i++ {
			ch <- fmt.Sprintf("name:%d", i)
		}
        defer close(ch)
	}()
	// more := true
	// var msg string
    // for more {
    //     msg, more = <-ch
    //     if more{
    //         fmt.Println(msg)
    //     } else {
    //         fmt.Println("closed channel")
    //     }
    // }
    for msg := range ch {
        fmt.Println(msg)
    }
}

func testTimeer() {
    // first
    <-time.After(3 * time.Second)
    fmt.Println("after 3 s")

    // second 可以stop
    timer := time.NewTimer(2*time.Second)
    <-timer.C
    fmt.Println("after 2 s")

    // third
    time.Sleep(1*time.Second)
    fmt.Println("after 1 s")
}

func testTicker() {
    ticker := time.NewTicker(time.Second)
    for t := range ticker.C {
        fmt.Println("Tick at", t)
    }
}

func testShowEnv(){
    os.Setenv("WEB", "sss")
    println(os.Getenv("WEB"))

    for _, env := range os.Environ(){
        e := strings.Split(env, "=")
        println(e[0], "=", e[1])
    }
}

func testExec(){
    cmd := exec.Command("curl", "www.baidu.com")

    out, err := cmd.Output()
    if err != nil {
        println("Command error:"+ err.Error())
        return
    }
    println(string(out))
}

func testArgs() {
    args := os.Args
    fmt.Println(args)
    fmt.Println(args[1:])
}

func testFullArgs() {
    host := flag.String("host", "123.123.123.123", "the full hostname")
    port := flag.Int("port", 80, "num of port")
    flag.Parse()
    fmt.Println("host:", *host)
    fmt.Println("port:", *port)
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
    // TestInterface()

    // mark METHODS
    // https://milapneupane.com.np/2019/07/06/learning-golang-from-zero-to-hero
    // TestJsonMarshal()
    // TestJsonUnmarshal()
    // TestErrorHandle()
    // TestErrorHandle2()
    // TestPanicAndCatch()
    // TestChannel()
    // TestOneWayChannel()
    // TestChannel2()
    // TestChannelTimeout()
	// TestChannelClose()
	// TestFirstArrive()

	// TestBufferChannel()
    // testDefer()
    // testPanic()
    // testRoutine()
    // testCPU()

    // testSellTicket()
    // testAtomic()
    // testTimeer()
    // testTicker()
    // testShowEnv()
    // testExec()
    // testArgs()
    // testFullArgs()
}


func init() {
    // fmt.Println("I am init")
}
