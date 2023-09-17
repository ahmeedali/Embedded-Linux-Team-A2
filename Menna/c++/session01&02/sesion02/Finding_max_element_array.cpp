#include <algorithm>
#include <array>
#include <iostream>

int findingMax(int* arr, int size){
  int max=0;   
  max=*std::max_element(arr,arr+size);
  return max;
}

int main()
{
   int arr[5]={1,2,9,20,3};
   std::cout<< "max element is : "<<findingMax(arr,5)<<std::endl;

    return 0;
}
