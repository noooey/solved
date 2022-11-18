#include <iostream>
#include <string>
#include <cstring>
using namespace std;
#define TARGET 'e'

int main(int argc, char *argv[]){
  if (argc < 2) { cout << "one command line argument needed\n"; return -1; }
  int n = strlen(argv[1]);
  char *a = new char[n*2+3];
  if (!a) {cout << "allocation failed.\n"; return -1;}
  a[0] = '!';

  char *r = argv[1];

  int i = 1;
  for(; *r; r++, i++){
    if(*r == 'e'){
      a[i] = 'e';
      i++;
      a[i] = 'e';
    } else{
      a[i] = *r;
    }
  }
  a[i] = '.';
  i++;
  a[i] = '\0';

  cout << a << endl;


  string s = "!";
  s += argv[1];
  s += ".";
  int pos = 0;

  while(1){
   pos = s.find("e", pos);
   if(pos == -1) break;
   s.insert(pos+1, "e");
   pos += 2;
  }

  cout << s << endl;
}
