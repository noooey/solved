#include <iostream>
using namespace std;

int main(){
  int n;
  cin >> n;

  int arr[n];

  for(int i = 0; i < n; i++){
    cin >> arr[i];
  }

  for(int i = n-1; i > 0; i--){
    for(int j = 0; j < i; j++){
      if(arr[j] > arr[j+1]){
        int tmp = arr[j];
        arr[j] = arr[j+1];
        arr[j+1] = tmp;
      }
    }
  }

  int result[4] = 0;
  result[0] = arr[n-1]*arr[n-2]*arr[n-3];  // 양수 3개
  result[1] = arr[n-1]*arr[n-2];   // 양수 2개
  result[2] = arr[0]*arr[1];  // 음수 2개
  result[3] = arr[0]*arr[1]*arr[n-1];  //음수 2개 양수 1개


  int max = result[0];
  for(int i = 1; i < 4; i++){
    if(result[i] > max) max = result[i];
  }

  cout << max << endl;

}
