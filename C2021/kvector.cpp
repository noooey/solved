#include <iostream>
using namespace std;

class Kvector{
  int *m;
  int len;
public:
  static int total_len;

  Kvector(int sz = 0, int value = 0);
  Kvector(const Kvector& v);
  ~Kvector(){
    cout << this << " : ~Kvector() \n";
    total_len -= len;
    delete[] m;
  }
  void print() const{
    for (int i = 0; i < len; i++) cout << m[i] << " ";
    cout << endl;
  }
  void print() {
    for (int i = 0; i < len; i++) cout << m[i] << " ";
    cout << endl;
  }
  void clear(){
    delete[] m;
    m = nullptr;
    len = 0;
  }
  int size()const{ return len; }
  int size(){ return len; }
};

Kvector::Kvector(int sz, int value){
  if(sz == 0){
    m = nullptr;
    return;
  }
  m = new int[sz];
  len = sz;
  total_len += len;
  for(int i = 0; i < len; i++){
    m[i] = value;
  }
  cout << this << " : Kvector( " << sz << ", " << value << ") \n";
}

Kvector::Kvector(const Kvector& v){
  len = v.size();
  total_len += len;
  m = new int[len];
  for(int i = 0; i < len; i++){
    m[i] = v.m[i];
  }
  cout << this << " : Kvector(*" << &v << ") \n";
}

int Kvector::total_len = 0;

int main(){
  Kvector v1(3); v1.print();
  const Kvector v2(2, 9); v2.print();
  Kvector v3(v2); v3.print();

  cout << "total length = " << Kvector::total_len << endl;
  v2.print();
  v3.print();
  cout << "total length = " << Kvector::total_len << endl;
  return 0;
}
