#include <iostream>
#include <bitset>
using namespace std;

int main(){
  unsigned int n;
  cin >> n;
  bitset<32>bit(n);
  unsigned int byteArr[4];
  unsigned char *byte = (unsigned char *)&bit;
  for(int i = 0; i < 4; i++){
    byteArr[i] = *byte++;
  }

  unsigned int sum = 0;
  for(int i = 1; i < 4 ; i++){
    sum += byteArr[i];
  }

  while(1){
    if(sum >= 256) sum -= 256;
    else break;
  }

  string checkSum = to_string(255-sum);
  string last = to_string(byteArr[0]);

  if(checkSum == last) cout << 1 << endl;
  else cout << 0 << endl;  // 손상O
}
