#include<iostream>
using namespace std;
int main() {
    int dividend , divisor;
    cout << "Enter the Divisor : "; 
    cin >> divisor ;
    cout << "Enter the divisor : ";
    cin>>dividend;
    int quo = dividend / divisor;
    int rem = dividend % divisor;
    cout<<"the quotient is : "<<quo;
    cout<<"\nThe remainder is: "<<rem;
    return 0;
    }
