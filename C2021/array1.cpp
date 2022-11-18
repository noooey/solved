#include <iostream>
using namespace std;

int main(){
  int arr[3][4] = {{10, -1, 3},{2, 5, 6}};

  for(int i=0; i<3; i++)
    for(int j=0; j<4; j++) {
      cout << "arr[" << i << "][" << j << "] value: ";
      cout << arr[i][j] << " address: " << &arr[i][j] << endl;
    }
  return 0;
}
