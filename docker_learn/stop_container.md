# 优雅的终止docker容器
1. http服务处理完已有的http request
2. 写入内存的数据，持久化到存储设备中
3. 微服务架构中，从服务发现模块中注销自己

## docker stop
    - 会向容器中PID为1的进程发送系统信号SIGTERM信号，未终止的话，会在10秒后发送SIGKILL强行kill掉进程。
    - SIGKILL是发往内核的，应用程序没有机会去处理。
    docker stop --time=20 container_name

## docker kill
    - 默认情况下, 不会给容器任何gracefully shutdown的机会, 实际还允许发送自定义的系统信号
    docker kill --signal=SIGINT container_name
    直接发送,SIGKILL和SIGINT两个信号，没有超时选项

## 在程序中接收并处理信号
    ### 错误
        CMD bash run.sh
        实际翻译成 CMD ["sh", "-c", "bash run.sh"]
        PID1变成了sh
    ### 正确
        CMD ["bash", "run.sh"]
