#include<iostream>
#include<queue>
#include<string>
#include<cstring>
using namespace std;

const int n=5;
int used[n];
int temp[n];

void dfs(int a){
    if(a==n){
        for(int i=0;i<n;++i){
            cout<<temp[i]<<" ";
        }
        cout<<endl;
        return;
    }
    for(int i=0;i<n;++i){
        if(!used[i]){
            temp[a]=i;
            used[i]=1;
            dfs(a+1);
            used[i]=0;
        }
    }
}
void test(){
    queue<string >q;
    q.push("1");
}

int main(){
    dfs(0);
    return 0;
}


