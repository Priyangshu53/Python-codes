#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define NUMBER 10

struct Process{
    int processId;
    int status; // 0 means cpu bound and 1 means io bound
};
void generate(struct Process p[],int num){
    for (int i = 0; i < num; i++){
        p[i].processId=i+1;
        p[i].status=rand()%2;
    }
}
void display(struct Process p[],int num){
    char *s;
    for(int i=0;i<num;i++){
        printf("Process ID = %d\n",p[i].processId);
        s=(p[i].status==0)?"CPU Bound":"IO Bound";
        printf("Status = %s\n",s);
        printf("\n");
    }
}
int main(){
    srand(time(0));
    struct Process newstate[NUMBER];
    struct Process readystate[NUMBER];
    struct Process temp;
    int cpuindex=0,ioindex=NUMBER,cpuBoundCount=2,ioBoundCount=1,c=0,j;
    generate(newstate,NUMBER);
    display(newstate,NUMBER); 
    for (int i = 0; i < NUMBER; i++){
        for (int j = 0; j < NUMBER-1-i; j++){
            if(newstate[j].status>newstate[j+1].status){
                temp=newstate[j];
                newstate[j]=newstate[j+1];
                newstate[j+1]=temp;
            }
        }
    }
    for (int i = 0; i < NUMBER; i++){
        if(newstate[i].status==1){
            ioindex=i;
            break;
        }
    }
    j=ioindex;
    if(ioindex%2==0)
        ioindex++; 
    for (int i = 0; i < NUMBER; i++){
        if(cpuBoundCount>0 && cpuindex<ioindex-1 && j<NUMBER){
            readystate[c++]=newstate[cpuindex];
            cpuBoundCount--;
            cpuindex++;
            printf("Iteration %d:\n",i+1);
            display(readystate,c);
            printf("\n");
            
        }
        else if(cpuBoundCount!=2 && j<NUMBER){
            readystate[c++]=newstate[j];
            j++;
            cpuBoundCount=2;
            printf("Iteration %d:\n",i+1);
            display(readystate,c);
            printf("\n");
        }
    }
return 0;
}