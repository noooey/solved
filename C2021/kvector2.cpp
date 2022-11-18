#include <iostream>
using namespace std;

class Kvector{
  int *m;
  int len;
public:
  Kvector(int sz = 0, int value = 0): len(sz){
    if(sz == 0){
      m = nullptr;
      return;
    }
    m = new int[sz];
    len = sz;
    for(int i = 0; i < len; i++){
      m[i] = value;
    }
    cout << this << " : Kvector( " << sz << ", " << value << ") \n";
  }
  Kvector(const Kvector& v){
    len = v.size();
    m = new int[len];
    for(int i = 0; i < len; i++){
      m[i] = v.m[i];
    }
    cout << this << " : Kvector(*" << &v << ") \n";
  }
  ~Kvector(){
    cout << this << " : ~Kvector() \n";
    delete[] m;
  }
  void print() const{
    for (int i = 0; i < len; i++) cout << m[i] << " ";
    cout << endl;
  }
  void clear(){
    delete[] m;
    m = nullptr;
    len = 0;
  }
  int size()const{ return len; }

  Kvector& operator=(const Kvector& v);
  int& operator[](auto idx);
  friend bool operator==(const Kvector& v, const Kvector& e);
  friend bool operator!=(const Kvector& v, const Kvector& e);
  friend ostream& operator<<(ostream& os, const Kvector& e);
};

Kvector& Kvector::operator=(const Kvector& v){
  if(this != &v){
    delete[] m;
    len = v.size();
    m = nullptr;
    m = new int[len];
    for(int i  = 0; i < len; i++){
      m[i] = v.m[i];
    }
  }
  return *this;
}

int& Kvector::operator[](auto idx){
  return m[idx];
}

bool operator==(const Kvector& v, const Kvector& e){
  if(v.len != e.len) return 0;
  int count = 0;
  for(int i = 0; i < v.len; i++){
    if(v.m[i] == e.m[i])
      count++;
  }
  if(count == v.len)
    return 1;
  else return 0;
}

bool operator!=(const Kvector& v, const Kvector& e){
  for(int i = 0; i < v.len; i++){
    if(v.m[i] != e.m[i])
      return 1;
  } return 0;
}

ostream& operator<<(ostream& os, const Kvector& e){
  for(int i = 0; i < e.len; i++)
    os << e.m[i] << " ";
  return os;
}

int main(){
  Kvector v1(3); v1.print();
  Kvector v2(2, 9); v2.print();
  Kvector v3(v2); v3.print();
  cout << (v1 == v2) << endl;
  cout << (v3 == v2) << endl;
  v3 = v2 = v1;
  cout << v1 << endl;
  cout << v2 << endl;
  cout << v3 << endl;
  cout << (v3 != v2) << endl;
  v1[2] = 2;
  v2[0] = v1[2];
  cout << "v1: " << v1 << "v2: " << v2 << "v3: " << v3 << endl;
  return 0;
}
