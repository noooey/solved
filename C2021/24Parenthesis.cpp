#include<iostream>
#include<cstring>
using namespace std;

int main(void){
  string str;
  cin >> str;
  int left = 0;
  int right = 0;

  for(int i=0; i < str.length(); i++){
    if(str[i] == '(') left++;
    else if(str[i] == ')') right++;
    if(left < right){
      cout << 0 << endl;
      return 0;
    }
  }
  cout << 1 << endl;
  return 0;
}
