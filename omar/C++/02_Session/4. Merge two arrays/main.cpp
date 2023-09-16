#include <array>
#include <iostream>
#include <algorithm>

int array1[6] = {88,15,106,15,30,40};
int array2[3] = {8, 90, 50};

void merge(const int arr1[], const int arr1_size, const int arr2[], const int arr2_size, int merge_arr[]){
  // Inserting first array elements in the merge array
  for(int i = 0; i < arr1_size; i++){
    merge_arr[i] = arr1[i];
  }

  // Inserting second array elements in the merge array
    for(int j = 0; j < arr2_size; j++){
      merge_arr[arr1_size + j] = arr2[j];
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

  int array1_size = sizeof(array1)/sizeof(array1[0]);
  int array2_size = sizeof(array2)/sizeof(array2[0]);

  int new_array_size = array1_size + array2_size;
  int new_array[new_array_size];

  merge(array1, array1_size, array2, array2_size, new_array);

  std::cout << "First array" << std::endl;
  printArray(array1, array1_size);
  std::cout << "" << std::endl;

  std::cout << "Second array" << std::endl;
  printArray(array2, array2_size);
  std::cout << "" << std::endl;

  std::cout << "Merged array" << std::endl;
  printArray(new_array, new_array_size);
  std::cout << "" << std::endl;

  return 0;
}