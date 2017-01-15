
int N=80000;
int N2=800000;
int PNUM=1;
  
void* task_thread(void *arg)  
{  
    int i=0;  
    printf(". ");  
    fflush(stdout);
    int sum=0,j;
    for(i=0;i<N;++i)
        for(j=0;j<N2/PNUM;++j)
            sum+=i*j;
    pthread_exit((void *)2);  
}  

void* task_process(void *arg)  
{  
    int i=0;  
    printf(". ");  
    fflush(stdout);
    int sum=0,j;
    for(i=0;i<N;++i)
        for(j=0;j<N2/PNUM;++j)
            sum+=i*j;
}
