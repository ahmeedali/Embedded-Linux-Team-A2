#include "Trace.hpp"

void BackTrace::print_B(){
 
  for (std::string i : BT) {
     std::cout<<"The order is : "<<i<<std::endl;
  }

}

