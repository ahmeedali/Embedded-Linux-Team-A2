#include <iostream>

int sum_of_digits(int num){
  // loacal variable for accumulation of the digits in the number
  int sum = 0;

  while(num != 0){
    sum += num%10;
    num /= 10;
  }

  return sum;
}


int main(int argc, const char **argv) {

  std::cout << "The summation of digits of the number 12345 is: " << sum_of_digits(12345) << std::endl;
  
  if((argc > 1)){
    std::cout << "The summation of digits of the number " << std::stoi(argv[1]) << " is: ";
    std::cout << sum_of_digits(std::stoi(argv[1])) << std::endl;
  }
  return 0;
}