#include <iostream>
#include <thread>
#include <mutex>
using namespace std;
static int sharedData = 0;
mutex dataMutex;

void increase() {
  int i = 0;
  for(;i<50000;i++){
    dataMutex.lock();
    sharedData++;
    dataMutex.unlock();
  }
}

int main(){
  thread t(increase);
  for(int i = 0; i < 50000; i++){
    dataMutex.lock();
    sharedData--;
    dataMutex.unlock();
  }
  if(t.joinable())
    t.join();
  cout << "sharedData = " << sharedData << end1;
}
