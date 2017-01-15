#!/bin/bash
# 任务数 处理机核

tasks=40

for((i=1;i<=9;++i));do
    echo ========$tasks=$i===========
    python multi_thread.py $tasks $i
    python multi_process.py $tasks $i
    echo ======================
done

echo ========$tasks=$tasks===========
python multi_thread.py $tasks $tasks
python multi_process.py $tasks $tasks
echo ======================
