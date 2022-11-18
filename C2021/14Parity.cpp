#include <iostream>
#include <cmath>

using namespace std;

int main(void) {
    long n;

    cin >> n;

    long k = n;
    long arr[32] = {};

    for(int i = 0; i < k; i++){
        arr[i] = k % 2;
        k = k / 2;

        if(n == 0) break;
    }

    int count = 0;
    for(int j = 0; j < 32; j++){
        if(arr[j] == 1) count++;
    }

    if(count % 2 == 0) cout << n << endl; // 짝수 -> 짝수
    else cout << (long)pow(2, 31) + n << endl; // 홀수 -> 짝수
    return 0;
}
