#include <iostream>

#define DEFAULT_RANGE 10

// function to print multiplication table for a number until defined range
void mult_table(int num, int range = DEFAULT_RANGE){

  std::cout << "The Multplication Table for " << num << " :" << std::endl;

  for(int i = 1; i <= range; i++){
    std::cout << num << " * " << i << " = " <<num*i << std::endl;
  }
}

int main(int argc, const char **argv) {
  
  // local variable to store the input number from the user
  int n = 0;
  // local variable to store the range of the table from the user
  int r = 0;

  // ask the user to enter an integer number
  std::cout << "Enter an integer number: ";
  std::cin >> n;

  // ask the user to enter a range for the table
  std::cout << "Enter range: ";
  std::cin >> r;

  // call the mult_table function to print out the table for the entered number
  mult_table(n, r);
  mult_table(9);

  return 0;
}