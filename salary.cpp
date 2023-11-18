#include<iostream>
#include<conio.h>
using namespace std;
int main()
{
    int rate,pay,hour,overtime,opay,total;
    cout<<"Enter the number of hours worked: ";
    cin>>hour;
    cout<<"Enter the rate: ";
    cin>>rate;
    if(hour>40)
    {
    overtime=hour-40;
    pay = 40*rate;
    opay = (overtime * (2 * rate));
    total = pay + opay;
    }
    else
    {
        pay = hour * rate;
        total = pay;
        }
        cout<<"\nTotal salary is : " <<total ;
        return 0;
        }


        
    

    






