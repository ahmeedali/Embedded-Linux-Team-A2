#include <bitset>
#include <iostream>

int main(int argc, const char **argv) {

  // local variables to store the parameters entered from the user
  int num = 0;
  std::string bin;

  // ask the user to input  a decimel number
  std::cout << "Enter a decimel number: ";

  // read decimal number from the user
  std::cin >> num;

  // represent the entered decimel number in a binary form
  std::cout << "Binary representation: " << std::bitset<8>(num) << std::endl;

    // ask the user to input  a binary number
  std::cout << "Enter a binary number: ";

  // read binary number from the user
  std::cin >> bin;

  // represent the entered binary number in a decimel form
  std::cout << "Decimel representation: " << std::stoi(bin, 0, 2) << std::endl;

  return 0;
}