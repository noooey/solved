#include <iostream>
using namespace std;

int main(void){
  int n; int k;
  cin >> n >> k;
  int arr[n];
  int arr2[n];

  int num;
  for(int i=0; i < n; i++){
    cin >> num;
    arr[i] = num;
    arr2[i] = num;
  }

  for(int t=0; t < k; t++){
    for(int i=0; i < n; i++){
      if(i == 0){
        if(arr[i+1] < 3 || arr[i+1] > 7) if(arr[i] > 0) arr2[i] = arr[i]-1;
        if(7 >= arr[i+1] && arr[i+1] >= 4) if(arr[i] < 9) arr2[i] = arr[i]+1;
      }
      if(n-1 > i && i > 0){
        if((arr[i-1]+arr[i+1]) < 3 || (arr[i-1]+arr[i+1]) > 7) if(arr[i] > 0) arr2[i] = arr[i]-1;
        if(7 >= (arr[i-1]+arr[i+1]) && (arr[i-1]+arr[i+1]) >= 4) if(arr[i] < 9) arr2[i] = arr[i]+1;
      }
      if(i == n-1){
        if(arr[i-1] < 3 || arr[i-1] > 7) if(arr[i] > 0) arr2[i] = arr[i]-1;
        if(7 >= arr[i-1] && arr[i-1] >= 4) if(arr[i] < 9) arr2[i] = arr[i]+1;
      }
    }
    for(int i=0; i < n; i++) arr[i] = arr2[i];
  }

  for(int i=0; i < n; i++){
    cout << arr[i] << " ";
  } cout << endl;
}
