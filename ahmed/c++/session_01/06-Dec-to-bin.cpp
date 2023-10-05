#include <bitset>
#include <iostream>

int main() {

  int Dec_number;
  std::cout << "Enter a decimal number:  ";
  std::cin >> Dec_number;

  std::bitset <8> Dec_to_Bin(Dec_number);
  std::cout <<"Binary representation :  "<< Dec_to_Bin<< std::endl;;
  
/*******************************************************************/
  std::string Bin_number;
  std::cout << "Enter a binary number:  ";
  std::cin >> Bin_number;

  std::bitset<8> Bin_to_Dec(Bin_number);
  std::cout << "Binary representation :  " <<Bin_to_Dec.to_ulong() << std::endl;



  return 0;
}