#include <iostream>
using namespace std;

int main(){
  char a[10] = "abcde";

  cout << "1 "<< sizeof("abcde") << endl;
  cout <<"2 "<< sizeof(a) << endl;
  for (int i = 0; i < 10; i++)
    cout << a[i] << endl;

  return 0;
}
