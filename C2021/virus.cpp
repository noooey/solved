#include <iostream>
#include <vector>
using namespace std;

int main(){
  int n;
  int s;
  int s1;
  int s2;

  vector<int> net{1};

  cin >> n;
  cin >> s;

  for(int m=0; m < s; m++){
    cin >> s1 >> s2;
    int i;
    for(i=0; i < net.size(); i++){
      if(net[i] == s1){
        int j;
        for(j=0; j < net.size(); j++){
          if(net[j] == s2) break;
        } if(j == net.size()) net.push_back(s2);
      }
    } if(i == net.size()){
      int k;
      for(k = 0; k < net.size(); k++){
        if(net[k] == s2){
          net.push_back(s1);
          break;
        }
      }
    }
  }
  for(int i = 0; i < net.size(); i++){
    cout << net[i];
  } cout << endl;
  cout << net.size()-1 << endl;
}
