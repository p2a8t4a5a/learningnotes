#include<stdio.h>  
#include<string.h>  
#include<stdlib.h>  
#include<unistd.h>  
#include<pthread.h>  
#include<time.h>
#include "work.c"
// gcc main2.c -o main2 -pthread
  

void usr()  
{  
    time_t t=time(NULL);
    scanf("%d",&PNUM);
    //初始化线程属性结构
    pthread_attr_t attr;  
    pthread_attr_init(&attr);  
    pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);  

    pthread_t pid[PNUM];  
    int i;
    for(i=0;i<PNUM;++i)
        pthread_create(&pid[i], &attr, task_thread, NULL);  

    //前台工作  
    //等待pid2返回，返回值赋给p 
    void *p;  
    for(i=0;i<PNUM;++i)
        pthread_join(pid[i], &p); 
    time_t t2=time(NULL);
    printf("total time = %lf \n",difftime(t2,t));
}  
  
 
int main()  
{  
    usr();  
    return 0;  
}  
  
   
  
