#include<iostream>
using namespace std;
#define maxn 1000

int A[maxn+1];
void update(int k,int add){
    while(k<maxn){
        A[k]+=add;
        k+=k&(-k);
    }
}
int get(int k){
    int sum=0;
    while(k){
        sum+=A[k];
        k-=k&(-k);
    }
    return sum;
}
int main(){
    cout<<"hello"<<endl;
    int q;
    cin>>q;
    while(q--){
        int t,a,b;
        cin>>t>>a;
        if(t==1){
            cin>>b;
            update(a,b);
        }
        else
            cout<<get(a)<<endl;


    }

}
