#include <iostream>
#include <algorithm>
#include <set>

using namespace std;

int main(void) {

  set<int> s_in;
  set<int> s_un;
  set<int> s_df;

  int n1;
  int num1;
  cin >> n1;
  int arrA[n1];
  for(int i = 0; i < n1; i++){
    cin >> num1;
    arrA[i] = num1;
    s_df.insert(num1);
  }

  int n2;
  int num2;
  cin >> n2;
  int arrB[n2];
  for(int i = 0; i < n2; i++){
    cin >> num2;
    arrB[i] = num2;
  }

  for(int i = 0; i < n2; i++){
    s_un.insert(arrB[i]);
    for(int j = 0; j < n1; j++){
      if(arrA[j] == arrB[i]){
        s_in.insert(arrA[j]);
        s_df.erase(arrA[j]);
      }
    }
  }

  for(auto it = s_df.begin(); it != s_df.end(); it++){
      s_un.insert(*it);
  }

  cout << s_in.size() << " ";
  for(auto it = s_in.begin(); it != s_in.end(); it++){
    cout << *it << " ";
  } cout << endl;
  cout << s_un.size() << " ";
  for(auto it = s_un.begin(); it != s_un.end(); it++){
    cout << *it << " ";
  } cout << endl;
  cout << s_df.size() << " ";
  for(auto it = s_df.begin(); it != s_df.end(); it++){
    cout << *it << " ";
  } cout <<endl;
}
