#include <iostream>
#include <bitset>
using namespace std;

int main(){
  unsigned int m;
  unsigned int n;
  cin >> m >> n;

  unsigned int mm = m;
  unsigned int nn = n;

  unsigned int weight_m;
  for(weight_m = 0; mm; mm >>= 1) weight_m += mm & 1;
  unsigned int weight_n;
  for(weight_n = 0; nn; nn >>= 1) weight_n += nn & 1;
  cout << weight_m << " " << weight_n << " ";

  unsigned int dis;
  unsigned int c = (m^n);
  for(dis = 0; c; c >>= 1) dis += c & 1;
  cout << dis << endl;
}
