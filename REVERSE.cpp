#include <iostream>
using namespace std;
int main() {
    int n, rev=0,rem;
   cout << "Enter the number: ";
   cin >> n;
    while(n>0){
 rem = n % 10;
 n = n / 10;
 rev = (rev * 10) + rem;
    }
cout<<"The reverse number is : "<< rev;
}


