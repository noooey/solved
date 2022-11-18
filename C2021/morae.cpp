#include <iostream>
using namespace std;

int main(){
   int k;
   cin >> k;

   for(int i = 0; i < k/2+1; i++) {
      for(int j=0; j < i; j++) {
           cout << "-";
         }
      for(int n = 0; n < k - 2*i; n++) {
         if(n%2 == 0) {
            cout << "*";
         } else {
            cout << "+";
         }
      }
      for(int j = 0; j < i; j++) {
         cout << "-";
      }
      cout << endl;
   }
   for(int i = k/2; i > 0; i--) {
     for(int j = 0; j < i-1; j++){
       cout << "-";
     }
     for(int n = 0; n < k - 2*(i-1); n++) {
       if(n%2 == 0) {
          cout << "*";
       } else {
          cout << "+";
       }
     }
     for(int j = 0; j < i-1; j++){
       cout << "-";
     }
     cout << endl;
   }
   return 0;
}
