#include <iostream>
#include <cmath>
using namespace std;
enum COMPLEX_PART {RE, IM};

class Complex{
  double re, im;
  double norm() const { return sqrt(re*re + im*im); }
public:
  Complex(double re=0, double im=0) : re(re), im(im) {}
  Complex(const Complex& c){ re=c.re; im=c.im; }
  Complex& operator=(const Complex& c){  re = c.re; im = c.im; return *this; }
  Complex operator-(){ Complex t(-re, -im); return t; }
  Complex operator~(){ Complex t(re, -im); return t; }
  Complex& operator++(){ re++; return *this; }
  Complex operator++(int){ Complex t(*this); operator++(); return t; }
  Complex& operator--(){ re--; return *this; }
  Complex operator--(int){ Complex t(*this); operator--(); return t; }
  Complex& operator+=(const Complex& c){ re += c.re; im += c.im; return *this; }
  Complex& operator-=(const Complex& c){ re -= c.re; im -= c.im; return *this; }
  Complex& operator*=(const Complex& c){ int tmp = re; re = re*c.re-im*c.im; im = tmp*c.im+im*c.re; return *this; }

  double& operator[](COMPLEX_PART idx){ return (idx? im : re); }
const double& operator[](COMPLEX_PART idx) const{ return (idx? im : re); }

friend bool operator==(const Complex& c1, const Complex& c2){ return ((c1.re == c2.re) && (c1.im == c2.im)); }
friend bool operator!=(const Complex& c1, const Complex& c2){ return !(c1 == c2); }
friend bool operator<(const Complex& c1, const Complex& c2){ return c1.norm() < c2.norm(); }
friend bool operator>(const Complex& c1, const Complex& c2){ return c1.norm() > c2.norm(); }
friend bool operator<=(const Complex& c1, const Complex& c2){ return c1.norm() <= c2.norm(); }
friend bool operator>=(const Complex& c1, const Complex& c2){ return c1.norm() >= c2.norm(); }

friend ostream& operator<< (ostream& os, const Complex& c);
friend istream& operator>> (istream& is, Complex& c);

friend Complex operator+(Complex lhs, const Complex& c);
friend Complex operator-(Complex lhs, const Complex& c);
friend Complex operator*(Complex lhs, const Complex& c);

};

istream& operator>> (istream& is, Complex& c){
  is >> c.re >> c.im;
  return is;
}
ostream& operator<< (ostream& os, const Complex& c){
  os << c.re << ((c.im>=0.0)? '+':'-') << abs(c.im) << "i ";
  return os;
}

Complex operator+(Complex lhs, const Complex& c){
  Complex result(lhs.re + c.re, lhs.im + c.im);
  return result;
}
Complex operator-(Complex lhs, const Complex& c){
  Complex result(lhs.re - c.re, lhs.im - c.im);
  return result;
}
Complex operator*(Complex lhs, const Complex& c){
  Complex result(lhs.re*c.re - lhs.im*c.im, lhs.re*c.im + lhs.im*c.re);
  return result;
}

int main(void){
    Complex c1, c2, c3, c4;
    Complex c5, c6, c7, c8, c9;
    cin >> c1 >> c2 >> c3 >> c4;

    cout << c1 << " " << c2 << " " << c3 << " " << c4 << endl;
    cout << (2 + c1 + 3) + (2 - c2 - 3) * (2 * c3 * 3) - ( 2 * c4 - 3 ) << endl;

    c5 = c6 = c7 = c8 = c1;
    cout << (c5 == c2) << " " << (c5 != c2) << endl;
    cout << (c5 > c2) << " " << (c5 >= c2) << " " << (c5 < c2) << " " << (c5 <= c2) << endl;
    cout << (c5 == c6) << " " << (c5 != c6) << endl;
    cout << (c5 > c6) << " " << (c5 >= c6) << " " << (c5 < c6) << " " << (c5 <= c6) << endl;
    c5 += c2;
    c6 -= c3;
    c7 *= c4;
    c8 = c2[RE];
    c9 = c3[IM];
    cout << c5 << " " << c6 << " " << c7 << " " << c8 << " " << c9 << endl;

    c7 = -c6;
    c8 = (++c7) * 2;
    c9 = 2 * (c7++);
    cout << c7 << " " << c8 << " " << c9 << endl;

    c7 = ~c6;
    c8 = (++c7) * 2;
    c9 = 2 * (c7++);
    cout << c7 << " " << c8 << " " << c9 << endl;
}
