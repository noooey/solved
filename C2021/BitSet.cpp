#include <iostream>
#include "BitSet.h"
using namespace std;
BitSet::BitSet(int sz): Bvector(sz){}
void BitSet::insert(int v){ set(v); }
BitSet operator+(const BitSet& v1, const BitSet& v2){
  if(v1.NBITS != v2.NBITS) throw IncompatibleException(v1.NBITS, v2.NBITS);
  BitSet v3(v1.NBITS);
  for(int i = 0; i < v1.NBITS; i++) if(v1.bit(i) || v2.bit(i)) v3.set(i);
  return v3;
}
ostream& operator<<(ostream& os, const BitSet& s){
  os << " { ";
  for(int i = 0; i < s.NBITS; i++) if(s.bit(i)) os << i << " ";
  os << "}";
  return os;
}
int main(int argc, char *argv[]){
  BitSet b1(132), b2(131);
  b1.insert(3); b1.insert(5); b1.insert(8);
  b2.insert(4); b2.insert(5); b2.insert(8); b2.insert(130);
  b1.print(); b2.print();
  cout << "b1= " << b1 << endl;
  cout << "b2= " << b2 << endl;
  try{
    cout << "b1+b2= " << b1+b2 << endl;
  }
  catch(IncompatibleException& e){
    cout << "In + operation, the operands are not compatible." << endl;
    cout << "The size of the first BitSet is " << e.n1 << endl;
    cout << "The size of the second BitSet is " << e.n2 << endl;
  }
  return 0;
}
