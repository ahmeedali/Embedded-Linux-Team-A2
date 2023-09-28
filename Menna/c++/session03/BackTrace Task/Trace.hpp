#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

#define  EnterFn  std::cout<<"Enter to : "<<__PRETTY_FUNCTION__<<std::endl; BackTrace::getInstance().BT.push_back(__func__);
#define  ExitFn   std::cout<<"Exiting from : "<<__PRETTY_FUNCTION__<<std::endl; 

#define print_bt  BackTrace::getInstance().print_B();

class BackTrace{
private:
BackTrace(){}

public:

std::vector<std::string>BT;

static BackTrace& getInstance()
{
    static BackTrace bt;
    return bt;
}

 void print_B();

};
