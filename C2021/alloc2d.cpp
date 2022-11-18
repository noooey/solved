#include <iostream>
#include <cstdlib>
using namespace std;

int **makeArray2D(int *sz);
void destroyArray2D(int **arr, int *sz);

int main(int argc, char *argv[]){
  if(argc < 2){
    cout << "usage : ./str  1d 2d 3d ... nd \n";
    return -1;
  }

  int i, dim = argc-1;
  int *size = new int[dim];

  for(i = 1; i < argc; i++) size[i-1] = atoi(argv[i]);

  int **arr2d = NULL;

  arr2d = makeArray2D(size);
  for(int i = 0; i < size[0]; i++){
    for(int j = 0; j < size[1]; j++) arr2d[i][j] = i*size[1]+j;
  }
  for(int i = 0; i < size[0]; i++){
    for(int j = 0; j < size[1]; j++) cout << arr2d[i][j] << ' ';
    cout << endl;
  }
  destroyArray2D(arr2d, size);
  return 0;
}

int **makeArray2D(int *sz){
  int n1 = sz[0], n2 = sz[1];
  int **arr = new int *[n1];
  for(int i = 0; i < n1; i++) arr[i] = new int[n2];
  return arr;
}
void destroyArray2D(int **arr, int *sz){
  int n1 = sz[0];
  for(int i = 0; i < n1; i++) delete[] arr[i];
  delete[] arr;
}
