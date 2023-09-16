#include "Array.hpp"
#include <algorithm>
#include <iostream>

Array::Array() {}
/*****************************************************/
void Array::find_max_number() {

  auto max = std::max_element(arr.begin(), arr.end());

  std::cout << "The max element is " << max << std::endl;
}
/*****************************************************/
void Array::search_for_number() {
  int val;
  std::cout << "Enter number for the search: ";
  std::cin >> val;

  auto num = std::find(arr.begin(), arr.end(), val);

  if (num != arr.end()) {

    std::cout << "Found at position " << std::distance(arr.begin(), num)
              << std::endl;
  } else {

    std::cout << "Not found" << std::endl;
  }
}
/*****************************************************/
void Array::delete_number() {

  int val;
     for (auto i:arr)
        std:: cout << i <<" " ;

  std::cout << "\nEnter number for the delete: ";
  std::cin >> val;

    auto num = std::remove(arr.begin(), arr.end(), val);
        std::cout << "Element Deleted Successfully! " << std::endl;

        for (auto i:arr)
                std:: cout << i <<" " ;
                std:: cout <<"\n";
    
 }
 
 void Array::even_and_odd()
 {
    int odd, even;
    std :: cout << "Even number :" << std :: endl;
     for (auto i : arr){
        
        if ( i % 2 ==0) {
            std :: cout << i << " ";  }  
     }
     
     std :: cout << "\nOdd number :" << std :: endl;
     for (auto i : arr){
        
        if ( i % 2 !=0) {
            std :: cout << i << " "; 
            }  
     }
     
 }
 


Array::~Array() {}