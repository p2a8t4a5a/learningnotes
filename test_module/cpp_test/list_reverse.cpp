#include<iostream>
using namespace std;

struct Node{
    int data;
    Node *next;
};
Node *head;

Node * reverse(Node *temp,Node *&head){
    if(temp==NULL || temp->next==NULL){
        head=temp;
        return temp;
    }
    else{
        Node *pre=reverse(temp->next,head);
        pre->next=temp;
        temp->next=NULL;
        return temp;
    }

}
void reverse(Node *&head){
    Node *pre,*cur,*nxt;
    pre=head;
    cur=head->next;
    while(cur){
        nxt=cur->next;
        cur->next=pre;

        pre=cur;
        cur=nxt;

    }
    head->next=NULL;
    head=pre;
}


int main(){
    int n=10;
    head=new Node();
    head->data=1;
    head->next=NULL;
    Node *temp=head;
    Node *temp2;
    for(int i=2;i<=n;++i){
        temp2=new Node();
        temp2->data=i;
        temp2->next=NULL;
        temp->next=temp2;
        temp=temp2;
    }
    reverse(head);
    reverse(head,head);
    temp=head;
    while(temp!=NULL){
        cout<<temp->data<<" ";
        temp=temp->next;
    }
}
