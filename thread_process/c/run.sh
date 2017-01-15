#!/bin/bash






for((i=4;i<=100;i++));do
echo ========多进程 $i===========
gcc -o multi_process multi_process.c -Wno-implicit-function-declaration
echo $i|./multi_process
echo ======================

# echo ========多线程 $i===========
# gcc -o multi_thread multi_thread.c -pthread
# echo $i|./multi_thread
# echo ======================
done
