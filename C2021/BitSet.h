#include <iostream>
#include <exception>
#include "Bvector.h"

class IncompatibleException : public std::exception{
public:
  int n1;
  int n2;
  IncompatibleException(int n1 = 32, int n2 = 32): n1(n1), n2(n2){}
};

class BitSet : public Bvector{
  public:
    BitSet(int sz=32);
void insert(int v);
friend BitSet operator+(const BitSet& v1, const BitSet& v2);
friend std::ostream& operator<<(std::ostream& os, const BitSet& s);
};
