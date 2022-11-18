#include <iostream>
using namespace std;

int main(void){
  int n;  // 정방행렬의 행과 열의 크기
  cin >> n;
  int num;
  int sum = 0;
  int max;
  int arr[n][n];
  int sum_arr[2*n];

  for(int i=0; i<2*n; i++){
    sum_arr[i]=0;
  }

  for(int y=n-1; y >= 0; y--){
    for(int x=0; x < n; x++){
      cin >> num;
      arr[y][x] = num;
    }
  }

  for(int y=0; y < n; y++){
    for(int x=0; x < n; x++){
      for(int i=0; i < n; i++){
        if(y == x-i || y == x+(n-i)) sum_arr[i] += arr[y][x];
      }
      for(int i=0; i < n; i++){
        if(y == -x+i || y == -x+n+i) sum_arr[n+i] += arr[y][x];
      }
    }
  }

  max = sum_arr[0];
  for(int i=0; i < 2*n; i++){
    if(sum_arr[i] > max){
      max = sum_arr[i];
    }
  }

  cout << max << endl;
}
