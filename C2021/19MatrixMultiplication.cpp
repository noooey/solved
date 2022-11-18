#include <iostream>
using namespace std;

int main(void){
  int m; // arr1의 행의 개수
  int n; // arr1의 열의 개수, arr2의 행의 개수
  int o; // arr2의 열의 개수
  int num;
  int sum = 0;

  cin >> m >> n >> o;
  int arr1[m][n];
  int arr2[n][o];
  int arr3[m][o];

  for(int i = 0; i < m; i++){
    for(int j = 0; j < n; j++){
      cin >> num;
      arr1[i][j] = num;
    }
  }
  for(int j = 0; j < n; j++){
    for(int k = 0; k < o; k++){
      cin >> num;
      arr2[j][k] = num;
    }
  }

  for(int i = 0; i < m; i++){
    for(int k = 0; k < o; k++){
      for(int j = 0; j < n; j++){
        arr3[i][k] = 0;
        sum += arr1[i][j]*arr2[j][k];
      } arr3[i][k] += sum; sum = 0;
    }
  }

  for(int i = 0; i < m; i++){
    for(int k = 0; k < o; k++){
      cout << arr3[i][k] << " ";
    } cout << endl;
  }
  return 0;
}
