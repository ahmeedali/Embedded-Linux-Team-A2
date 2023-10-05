#include "Array.hpp"
#include <algorithm>
#include <iostream>

Array::Array() {}
/*****************************************************/
void Array::find_max_number() {

  auto max = std::max_element(arr.begin(), arr.end());

  std::cout << "The max element is " << *max << std::endl;
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

 void Array::menu(){
 int choice{0};
  
     while (choice!=-1) {

    
        std::cout << "\n----- MENU -----" << std::endl;
        for (int i: arr)
          {  std:: cout << i << " ";  }
        std::cout << "\n1. Find the maximum number\n"
                  << "2. Search for a number\n"
                  << "3. Delete a number\n"
                  << "4. Display even and odd numbers\n"
                  << "5. Exit\n"
                  << "Enter your choice: ";
        std::cin >> choice;

        switch (choice) {
            case 1:
                find_max_number();
                break;
            case 2:
                search_for_number();
                break;
            case 3:
                delete_number();
                break;
            case 4:
                even_and_odd();
                break;
            case 5:
                std::cout << "Exiting the program." << std::endl;
                choice =-1;
                break;
            default:
                std::cout << "Invalid choice! Please try again." << std::endl;
        }
    }



 }

 
Array::~Array() {}