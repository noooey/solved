#include <iostream>
#include <cstring>
#include <cctype>
#include <algorithm>
using namespace std;

int digitL(bool ltor, string s){
  if(ltor == false) reverse(s.begin(), s.end());
    if(s == "0001101") return 0;
    else if(s == "0011001") return 1;
    else if(s == "0010011") return 2;
    else if(s == "0111101") return 3;
    else if(s == "0100011") return 4;
    else if(s == "0110001") return 5;
    else if(s == "0101111") return 6;
    else if(s == "0111011") return 7;
    else if(s == "0110111") return 8;
    else if(s == "0001011") return 9;
    else throw s;
}

int digitR(bool ltor, string s){
  if(ltor == false) reverse(s.begin(), s.end());
    if(s == "1110010") return 0;
    else if(s == "1100110") return 1;
    else if(s == "1101100") return 2;
    else if(s == "1000010") return 3;
    else if(s == "1011100") return 4;
    else if(s == "1001110") return 5;
    else if(s == "1010000") return 6;
    else if(s == "1000100") return 7;
    else if(s == "1001000") return 8;
    else if(s == "1110100") return 9;
    else throw s;
}

string Barcode(char a[]){
  string str = a;
  int ten[12];
  for(int i = 0; i < 12; i++) ten[i] = 0;
  bool ltor = true;
  if(str.length() != 95) throw str;
  if(str.substr(0, 3) != "101" || str.substr(92, 3) != "101") throw str;
  if(str.substr(45, 5) != "01010") throw str;
  if(str.substr(3, 7) == "0001101") ltor = true;   // 좌 -> 우
  else ltor = false;

  if(ltor==true){
    for(int i = 0; i < 6; i++){
      ten[i] = digitL(ltor, str.substr(3+7*i, 7));
    }
    for(int i = 0; i < 6; i++){
      ten[6+i] = digitR(ltor, str.substr(50+7*i, 7));
    }
  }
  else{
    for(int i = 0; i < 6; i++){
      ten[i] = digitR(ltor, str.substr(3+7*i, 7));
    }
    for(int i = 0; i < 6; i++){
      ten[6+i] = digitL(ltor, str.substr(50+7*i, 7));
    }
  }

  int CheckSum;
  if(ltor == true) CheckSum = 3*(ten[0] + ten[2] + ten[4] + ten[6] + ten[8] + ten[10]) + ten[1] + ten[3] + ten[5] + ten[7] + ten[9];
  else CheckSum = 3*(ten[1] + ten[3] + ten[5] + ten[7] + ten[9] + ten[11]) + ten[2] + ten[4] + ten[6] + ten[8] + ten[10];
  int Code = CheckSum % 10;
  int check_digit;
  if(Code == 0) check_digit = 0;
  else check_digit = (10 - Code);

  bool corr = true;
  if(ltor == false){
    if(check_digit != ten[0]) corr = false;
  }
  else{
    if(check_digit != ten[11]) corr = false;
  }

  string zz = "";
  if(ltor == true) for(int i = 0; i < 12; i++) zz += to_string(ten[i]);
  else for(int i = 0; i < 12; i++) zz += to_string(ten[i]);
  if(ltor == false) reverse(zz.begin(), zz.end());
  if(corr == false){
    zz += "*"+to_string(check_digit);
  }
  return zz;
}

int main(){
  char input[101];
  cin >> input;
  try {
    string code = Barcode(input);
    cout << code.substr(0, 6) << '-' << code.substr(6, 8) << endl;
  }
  catch(...){
    cout << "******-******\n";
  }
}
