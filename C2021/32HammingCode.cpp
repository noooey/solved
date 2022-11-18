#include <iostream>
#include <bitset>
#include <cstring>
#include <cmath>
#include <vector>
using namespace std;

   //전송해야할 실제 데이터 -> 송신
unsigned Hencode(bitset<32> v){
  // 1, 2, 4, 5, 16 위치에 P추가
  bitset<32> n;
  int j = 0;
  for(int i = 0; i < 31; i++){
    if(i == 0 || i == 1 || i == 3 || i == 7 || i == 15 ){
      n[i] = 0;
      continue;
    }
    n[i] = v[j];
    j++;
  }

  int cnt[5];
  for(int i = 0; i < 5; i++){
    cnt[i] = 0;
  }
  for(int i = 0; i < 31; i++){
    if((i > 0) && (i % 2 == 0)){
      if(n[i] == 1) cnt[0]++;
    }
    if((i > 1) && ((i-1)%4 == 0) && ((i-1)%4 == 1)){
      if(n[i] == 1) cnt[1]++;
    }
    if((i > 3) && (4 > ((i-3)%8)) && ((i-3)%8) >= 0){
      if(n[i] == 1) cnt[2]++;
    }
    if((i > 7) && (8 > ((i-7)%16)) && ((i-7)%16) >= 0){
      if(n[i] == 1) cnt[3]++;
    }
    if((i > 15) && (16 > ((i-15)%32)) && (((i-15)%16) >= 0)){
      if(n[i] == 1) cnt[4]++;
    }
  }
  for(int i = 0; i < 5; i++) if(cnt[i] % 2 == 1) n[pow(2, i)-1] = 1;

  return n.to_ulong();

}
   // 실제 데이터를 추출해야할 해밍(31, 26)코드 -> 수신
unsigned Hdecode(bitset<32> v){
  bitset<32> n;
  vector<int> p1;
  vector<int> p2;
  vector<int> p3;
  vector<int> p4;
  vector<int> p5;

  bool err = false;

  for(int i = 0; i < 31; i++){
    if((i > 0) && (i % 2 == 0)){
      if(v[i] == 1) p1.push_back(i);
    }
    if((i > 1) && 2 > ((i-1)%4) && ((i-1)%4 >= 0)){
      if(v[i] == 1) p2.push_back(i);
    }
    if((i > 3) && (4 > ((i-3)%8)) && ((i-3)%8) >= 0){
      if(v[i] == 1) p3.push_back(i);
    }
    if((i > 7) && (8 > ((i-7)%16)) && ((i-7)%16) >= 0){
      if(v[i] == 1) p4.push_back(i);
    }
    if((i > 15) && (16 > ((i-15)%32)) && (((i-15)%16) >= 0)){
      if(v[i] == 1) p5.push_back(i);
    }
  }

  vector<int> tmp;
  if(p1.size()%2 != v[0]) {tmp.push_back(1); err = true;}
  if(p2.size()%2 != v[1]) {tmp.push_back(2); err = true;}
  if(p3.size()%2 != v[3]) {tmp.push_back(4); err = true;}
  if(p4.size()%2 != v[7]) {tmp.push_back(8); err = true;}
  if(p5.size()%2 != v[15]) {tmp.push_back(16); err = true;}

  int sum = 0;
  for(int i = 0; i < tmp.size(); i++){
    sum += tmp[i];
  }
  if(err) v.flip(sum-1);

  int j = 0;
  for(int i = 0; i < 31; i++){
    if(i == 0 || i == 1 || i == 3 || i == 7 || i == 15 ){
      continue;
    }
    n[j] = v[i];
    j++;
  }

  return n.to_ulong();

}

int main(void){
  int mode;   // 0 or 1
  unsigned value;

  cin >> mode >> value;
  if(mode == 0)
    cout << Hencode(value) << endl;
  else
    cout << Hdecode(value) << endl;

  return 0;
}
