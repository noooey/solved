#include <iostream>
#include <cstring>
#include <cctype>
using namespace std;

int main(void){
  string s;

  cin >> s;

  string c;  // 국가 번호
  string p;  // 출판사 번호
  string b;  // 도서번호
  string checksum;  // 체크섬 번호

  bool result = true;

  if(s.length() != 13){
    result = false;
    cout << result << endl;
    return 0;
  }   // s길이 13이 아니면(세부분, 다섯부분...)

  string tmp = "";
  int count = 0;
  for(int i = 0; i < 13; i++){
    if(s[i] == '-'){
      if(tmp.length() == 0){  // 길이가 0인거
        result = false;
        cout << result << endl;
        return 0;
      }
      if(count == 0){
        if(tmp.length() > 5){  // 첫번째 부분 길이 > 5
          result = false;
          cout << result << endl;
          return 0;
        }
        c = tmp;
      }
      else if(count == 1){
        if(tmp.length() > 7){   // 두번째 부분 길이 > 7
          result = false;
          cout << result << endl;
          return 0;
        }
        p = tmp;
      }
      else if(count == 2){
        if(tmp.length() > 6){  // 세번째 부분 길이 > 6
          result = false;
          cout << result << endl;
          return 0;
        }
        b = tmp;
      }
      count++;
      tmp = "";
      continue;
    }
    else if(count != 3 && isdigit(s[i]) == 0){  // '-' 외 다른 문자
      result = false;
      cout << result << endl;
      return 0;
    }
    else tmp += s[i];
  }

  if(tmp.length() > 1) result = false; // 네번째부분 길이 > 1
  checksum = tmp;

  //'-'뺀 스트링 idx 0 to 9
  string n = c + p + b;   // length() == 9
  cout << "c: " << c << endl;
  cout << "p: " << p << endl;
  cout << "b: " << b << endl;
  cout << n << endl;
  int sum = 0;
  int t = 0;
  for(int i = 0; i < 9; i++){
    sum += (n[i]-'0')*(10-i);
    //cout << sum << endl;
  }
  cout << sum << endl;

  int check = 0;
  if(sum%11 != 0) check = ((sum/11)*11+11)-sum;

  cout << check << endl;
  cout << checksum << endl;
  if(check != 10) result = (to_string(check)==checksum);
  else result = (checksum=="X");
  cout << result << endl;
  return 0;
}
