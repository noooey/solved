#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(){
  srand(time(NULL));
  for (int i=0; i<10; i++){
    int dice = rand()%6 + 1;
    cout << dice << " ";
  }
  cout << endl;
}
