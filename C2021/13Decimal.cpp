#include <iostream>

using namespace std;

int main(void) {
    int n;
    cin >> n;

    int i = 2;
    for(; i <= n; i++){
        if(n % i == 0)
            break;
    }
   if(i == n)
       cout << 1 << endl;   // n은 소수
    else
        cout << 0 << endl;    // n은 소수X

    return 0;
}
