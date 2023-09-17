#include <algorithm>
#include <array>
#include <iostream>
#include <vector>

int findingMax(std::vector<int>& vect){

int Max=0;
Max=*std::max_element(vect.begin(),vect.end());   
return Max;
}

int main()
{   int no=0;
    std::vector<int> Arr= {1,2,5,6,8,9};
    std::cin>>no;        //for trying the push_back func
    Arr.push_back(no);  //just trying the function 
    std::cout<<"Max element is : "<<findingMax(Arr)<<std::endl;
    return 0;
}
