#include <iostream>
using namespace std;

int main(){
   int k;
   cin >> k;

   int h = k/2;

   int absy = 0;
   int absx = 0;

   for(int y = h; y >= -h; y--) {
      if(y>0) absy = y;
      else absy = -y;

      for(int x = -h; x <= h; x++) {
         if(x>0) absx = x;
         else absx = -x;

         if(absx<absy){
           if((absx+absy)%2 == 0) {
              cout << "*";
           } else {
              cout << "+";
           }
         }
         else if(absx>absy){
           cout << "-";
         }
         else {
           cout << "*";
         }
      }
      cout << endl;
   }
   return 0;
}
