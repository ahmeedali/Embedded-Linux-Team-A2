#include <iostream>

void ascii_table(void){

  std::cout << "__________________________________" << std::endl;
  std::cout << "|               |" << "|               |" << std::endl;
  std::cout << "|     Char      |" << "|     ASCII     |" << std::endl;
  std::cout << "|               |" << "|               |" << std::endl;
  std::cout << "**********************************" << std::endl;
  std::cout << "__________________________________" << std::endl;

  for(char c = ' '; c <= '~'; c++){
    std::cout << "||\t" << c << "\t" << "||\t" << int(c) << "\t||" << std::endl; 
  }

  std::cout << "**********************************" << std::endl;
}

int main(int argc, const char **argv) {
  
  ascii_table();
  
  return 0;
}