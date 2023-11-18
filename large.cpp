#include <iostream>
using namespace std;
int main() {
    int a,b,c;
    cout<<"Enter the three numbers :";
    cin>>a>>b>>c;
    if(a>=b && a>=c)
    cout<<"thw largest number is :"<<a;
    if(b>=a && b>=c)
    cout<<"thw largest number is :"<<b;
    if(c>=a && c>=b)
    cout<<"thw largest number is :"<<c;
    return 0;
    }