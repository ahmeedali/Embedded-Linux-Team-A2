#include <algorithm>
#include <array>
#include <iostream>

auto lam_sort_ascend = [](const int a,const int b){

   return (a < b);
};

auto lam_sort_descend = [](const int a,const int b){

   return (a > b);
};

int main() 
{
     std::array<int,5> arr={5,2,4,3,1};
     std::sort(arr.begin(),arr.end(),lam_sort_ascend);   //using lambda function for custom sorting

     for(int i : arr)
      std::cout<<i<<" ";

   std::cout<<std::endl;
   return 0;
}
