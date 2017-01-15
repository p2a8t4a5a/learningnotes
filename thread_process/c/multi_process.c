#include<unistd.h>
#include<sys/types.h>
#include<stdio.h>
#include<time.h>
#include"work.c"

void show(){
    printf("my pid at exit %d\n",getpid());
}

int main(){
    time_t t=time(NULL);
    pid_t pid[32];
    scanf("%d",&PNUM);
    int n=1,i=0;
    while((n<<1)<=PNUM){
        pid[i] = fork();
        n<<=1;
        i++;
    }
    int is_par=1;
    for(i=0;n!=1;n>>=1,i++){
        if(pid[i])
            is_par=0;
    }
    if(is_par){
        task_process(NULL);
        time_t t2=time(NULL);
        printf("total time = %lf \n",difftime(t2,t));
        fflush(stdout);
        sleep(1);
        wait();
    }
    else{
        task_process(NULL);
    }
        
    return 0;
}
