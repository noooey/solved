#include <iostream>

using namespace std;

int main(void) {
    int a;
    int b;
    int n;
    int w;
    int x;  // 양
    int y;  // 염소

    cin >> a >> b >> n >> w;  //  n = x + y, w = ax + by


    if(a == b){
        cout << -1 << endl;
    }
    else{
        x = (w - b*n) / (a - b);
        y = n - x;
        if(x == y || x <= 0 || y <= 0){
            cout << -1 << endl;
            return 0;
        }
        cout << x << " " << y << endl;
    }

    return 0;
}
