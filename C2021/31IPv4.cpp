#include <iostream>
#include <bitset>
#include <cstring>
#include <algorithm>
using namespace std;

int main(){
  int k;
  cin >> k;

  if(k == 1){ // 주소 ->  숫자변환
    string add = "";
    cin >> add;

    bitset<32>bit(0);
    unsigned char *byte = (unsigned char *)&bit;

    string tmp = "";
    for(int i = add.length()-1; i >= 0; i--){
      if(add[i] == '.'){
        reverse(tmp.begin(), tmp.end());
        *byte++ = stoi(tmp);
        tmp = "";
      } else tmp += add[i];
    }

    reverse(tmp.begin(), tmp.end());
    *byte = stoi(tmp);
    tmp = "";

    string s = bit.to_string();
    //unsigned int num = stoi(s, NULL, 2);     // 1 255.255.255.255

    unsigned int result = 0;

    for(int i = 0; s[i] != '\0'; i++){
      result = (result << 1) + s[i] - '0';
    }

    cout << result << endl;

  }
  else{  // 숫자 ->  주소변환
    unsigned int n;
    cin >> n;

    bitset<32>bit(n);
    unsigned int byteArr[4];
    unsigned char *byte = (unsigned char *)&bit;
    for(int i = 0; i < 4; i++){
      byteArr[i] = *byte++;
    }

    for(int i = 3; i > 0; i--){
      cout << byteArr[i] << ".";
    }
    cout << byteArr[0] << endl;
  }
}
