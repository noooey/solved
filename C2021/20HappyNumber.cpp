#include <iostream>
#include <set>
#include <sstream>
using namespace std;

int fff(int x){
  int sum = 0;
  string str_n = to_string(x);
  cout << str_n << endl;
  for(int i = 0; i < str_n.length(); i++)
    //sum += stoi(k)*stoi(k);
  }
  return sum;
}


int main(void){
  int n;
  cin >> n;

  int result = n;
  int count = 1;

  set<int> s;
  s.insert(n);

  while(result != 1){
    result = fff(result);
    s.insert(result);
    count++;
    if(count != s.size()) break;
  }

  if(result == 1) cout << "HAPPY" << endl;
  else cout << "UNHAPPY" << endl;

  return 0;
}
