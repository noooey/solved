#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

int main(void){
  int k;
  cin >> k;

  int h;

  set<int> s{1};

  for(int i = 0; i < k; i++){
    auto it = s.begin();
    h = *it;

    s.erase(h);

    s.insert(2*h);
    s.insert(3*h);
    s.insert(5*h);
  }
  cout << h << endl;;
  return 0;
}
