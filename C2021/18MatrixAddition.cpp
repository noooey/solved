#include <iostream>
using namespace std;

int main(void){
  int m; // 행의 개수
  int n; // 열의 개수
  int num;

  cin >> m >> n;
  int arr1[m][n];
  int arr2[m][n];
  int arr3[m][n];
  
  for(int i = 0; i < m; i++){
    for(int j = 0; j < n; j++){
      cin >> num;
      arr1[i][j] = num;
    }
  }
  for(int i = 0; i < m; i++){
    for(int j = 0; j < n; j++){
      cin >> num;
      arr2[i][j] = num;
    }
  }

  for(int i = 0; i < m; i++){
    for(int j = 0; j < n; j++){
      arr3[i][j] = arr1[i][j] + arr2[i][j];
    }
  }

  for(int i = 0; i < m; i++){
    for(int j = 0; j < n; j++){
      cout << arr3[i][j] << " ";
    } cout << endl;
  }
  return 0;
}
