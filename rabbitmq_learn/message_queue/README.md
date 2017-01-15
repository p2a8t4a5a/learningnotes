
> 因为python的GIL的问题，所以测试代码没有使用多线程。  
这里正好学着用shell来调用多进程

- **send.py** 往队列塞消息
- **receive.py** 往队列取消息 
- **run.sh** 启动一个send.py塞消息 四个receive.py处理消息

