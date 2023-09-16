#include <cctype>
#include <codecvt>
#include <iostream>
#include <ostream>

bool is_letter_vowel(char c) {
  bool vowelCheck = false;

  // check if the character parameter belongs to the alphapet
  if (!std::isalpha(c)) {
    std::cerr << "Non-alphaptic character" << std::endl;
  } else {
    // check if the character parameter is an uppercase or lowercase vowel
    vowelCheck =
        ((c == 'a') || (c == 'o') || (c == 'u') || (c == 'i') || (c == 'e') ||
         (c == 'A') || (c == 'O') || (c == 'U') || (c == 'I') || (c == 'E'));
  }

  return vowelCheck;
}

int main(int argc, const char **argv) {
  is_letter_vowel('w')? std::cout << "Vowel" << std::endl : std::cout << "Not Vowel" << std::endl;
  is_letter_vowel('a')? std::cout << "Vowel" << std::endl : std::cout << "Not Vowel" << std::endl;
  is_letter_vowel('1')? std::cout << "Vowel" << std::endl : std::cout << "Not Vowel" << std::endl;
  is_letter_vowel(3)? std::cout << "Vowel" << std::endl : std::cout << "Not Vowel" << std::endl;
  is_letter_vowel('I')? std::cout << "Vowel" << std::endl : std::cout << "Not Vowel" << std::endl;
  is_letter_vowel(argv[1][0])? std::cout << "Vowel" << std::endl : std::cout << "Not Vowel" << std::endl;
  return 0;
}