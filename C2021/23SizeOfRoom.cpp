#include <iostream>
#include <string>
using namespace std;

int dfs(int n, int m, int k);
void bubbleSort(int *size, int num);

#define MAX_SIZE (100+1)
#define MAX_ROOMS 100
#define ROOM  -1
#define WALL  -2
int arr[MAX_SIZE][MAX_SIZE];   // 맵

int main(void){
  int num = 0; // 방의 개수
  int m;   // 가로 길이
  int n;   // 세로 길이
  int roomSize[MAX_ROOMS];   // 방 사이즈
  cin >> m >> n;

  char str;
  for(int i = 0; i < n; i++){
    for(int j = 0; j < m; j++){
      cin >> str;
      if(str == '+') arr[n][m] = WALL;
      else arr[n][m] = ROOM;
    }
  }

  for(int i = 0; i < n; i++){
    for(int j = 0; j < m; j++){
      cout << arr[n][m] << " ";
    } cout << endl;
  }

  for(int i = 0; i < n; i++){
    for(int j = 0; j < m; j++){
      if(arr[n][m] == ROOM){
        roomSize[num] = dfs(n, m, num);
        num++;
      }
    }
  }

  bubbleSort(roomSize, num);

  cout << num << endl;
  for(int i = 0; i < num; i++){
    cout << roomSize[i] << " ";
  } cout << endl;
}

int dfs(int n, int m, int k){
  int left, right, up, down;
  if(arr[n][m] == ROOM){
    arr[n][m] = k;
    left = dfs(n, m-1, k);
    right = dfs(n, m+1, k);
    up = dfs(n+1, m, k);
    down = dfs(n-1, m, k);
    return left+right+up+down+1;
  }
  return 0;
}

void bubbleSort(int *size, int num){
  int t;
  for(int j = num-1; j > 0; j--){
    for(int i = 0; i < j; i++){
      if(size[i+1] > size[i]){
        t = size[i];
        size[i] = size[i+1];
        size[i+1] = t;
      }
    }
  }
}
