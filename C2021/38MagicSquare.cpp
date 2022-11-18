#include <iostream>

using namespace std;

int **genMagicSquare(int n){
  int **arr = new int *[n];

  for(int i = 0; i < n; i++){
    arr[i] = new int[n];
  }
  return arr;
}

int main(void){
  int n;

  cin >> n;
  if(!(n%2)) return 1;

  int **sq = genMagicSquare(n);

  int a = 0;
  int b = n/2;
  for(int k = 1; k <= n*n; k++){
    if(a < 0 && b > n-1) { a += 2; b -= 1; }
    else if(a < 0) a = n-1;
    else if(b > n-1) b = 0;
    if(sq[a][b] != 0) { a += 2; b -= 1; }
    sq[a][b] = k;
    a--; b++;
  }

  for(int i = 0; i < n; i++){
    for(int j =0; j < n; j++)
      cout << sq[i][j] << ' ';
    cout << endl;
  }
}
