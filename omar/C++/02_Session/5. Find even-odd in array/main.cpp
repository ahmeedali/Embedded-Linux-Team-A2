#include <array>
#include <iostream>
#include <algorithm>

int array[6] = {88,21,106,15,30,40};

void findOddInArray(const int arr[], const int arr_size);
void findEvenInArray(const int arr[], const int arr_size);
void printArray(int arr[], const int arr_size);

void findOddInArray(const int arr[], const int arr_size){
  int odd_numbers = 0;
  int odd_arr[arr_size];

  for(int i = 0; i < arr_size; i++){
    if((arr[i])%2 != 0){
      odd_arr[odd_numbers] = arr[i];
      odd_numbers++;
    }
  }
  
  if(!odd_numbers){
    std::cout << "No odd numbers\n" << std::endl;
  }
  else{
    std::cout << "Odd numbers array" << std::endl;
    printArray(odd_arr, odd_numbers);
    std::cout << "" << std::endl;
  }

}

void findEvenInArray(const int arr[], const int arr_size){
  int even_numbers = 0;
  int even_arr[arr_size];

  for(int i = 0; i < arr_size; i++){
    if((arr[i])%2 == 0){
      even_arr[even_numbers] = arr[i];
      even_numbers++;
    }
  }
  
  if(!even_numbers){
    std::cout << "No even numbers\n" << std::endl;
  }
  else{
    std::cout << "Even numbers array" << std::endl;
    printArray(even_arr, even_numbers);
    std::cout << "" << std::endl;
  }

}

void printArray(int arr[], const int arr_size){
  std::cout << "[";
  for(int i = 0; i < arr_size; i++){
    std::cout << arr[i];
    if(i < arr_size-1){
      std::cout << ", ";
    }
  }
  std::cout << "]" << std::endl;
}

int main(int argc, const char **argv) {

  int array_size = sizeof(array)/sizeof(array[0]);

  findOddInArray(array, array_size);
  findEvenInArray(array, array_size);

  return 0;
}