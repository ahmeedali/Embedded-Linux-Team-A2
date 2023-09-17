#include <vector>
#include <algorithm>
#include <array>
#include <iostream>

template <std::size_t array_size>                  // generic array size type using template
bool search_ele(int (&arr)[array_size],int no){   //passing a refrence array and its size to make ranged for loop work inside a function 

    for(int i : arr){   
      if (i == no ) {
       return true;
       }
    }
 return false;
}

int main()
{
   int no=0;
   int arr[10]={1,2,9,20,3,80,100,66,52,2};
  
   std::cin>>no;
   if(search_ele(arr,no))
   {
      std::cout<<"the no is found"<<std::endl;
   }
   else
    {
      std::cout<<"the no isn't found"<<std::endl;
    }
   
  
return 0;
}
