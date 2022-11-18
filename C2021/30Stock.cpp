#include <iostream>
using namespace std;

int profit = 0; // 이익
int total = 0; // 총 투자 금액
int num = 0;  // 주식 개수
int n;

int sum(int idx, int arr[]){
  int max = arr[idx+1];
  for(int j = idx+1; j < n; j++){
    if(max < arr[j]){
      max = arr[j];
    }
  }
  int q;
  for(q = idx+1; q < n; q++){
    if(arr[q] < max){
      total += arr[q];
      num++;
    }
    else{
      profit += max*num - total;
      break;
    }
  }
  total = 0;
  num = 0;
  return q;
}

int main(){
  cin >> n;
  int arr[n];
  for(int i = 0; i < n; i++) cin >> arr[i];


  int max = arr[0];  // 최고 주가
  for(int i = 0; i < n; i++){
    if(max < arr[i]){
      max = arr[i];
    }
  }

  int k;
  for(k = 0; k < n; k++){
    if(arr[k] < max){
      total += arr[k];
      num++;
    }
    else{
      profit += max*num - total;
      break;
    }
  }
  total = 0;
  num = 0;

  while(k < n){
    k = sum(k, arr);
  }

  cout << profit << endl;
}
