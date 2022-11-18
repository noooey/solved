#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

bool checkCardNumberLength(string s){
  if(s[0] == '3') if(14 <= s.length() && s.length() <= 15) return true;
  else if(s[0] == '4') if(s.length() == 13 || s.length() == 16) return true;
  else if(s[0] == '5') if(s.length() == 16) return true;
  else if(s[0] == '6') if(s.length() == 16) return true;
  return false;
}

bool isCheckSumValid(string s){
  reverse(s.begin(), s.end());
  cout << s << endl;

  int sum= 0;
  for(int i = 0; i < s.length(); i++){
    int a = s[i]-'0';
    if(i % 2 == 1){
      if(a*2 > 9) s[i] = a*2-9;
      else s[i] = a*2;
      int tmp = s[i];
      sum += tmp;
    }
    else if(i % 2 == 0) sum += a;
    cout << sum << endl;
  }

  if(sum%10 == 0) return true;

  return false;
}

int main(void){
  string cardNumber;
  cin >> cardNumber;

  if(!checkCardNumberLength(cardNumber)){
    cout << "0\n";
    return 0;
  }
  cout << isCheckSumValid(cardNumber) << endl;
}
