#include <iostream>
#include <algorithm>

int MaxNumber(int x, int y, int z) ;

int main (){
    std::cout << "Enter 3 number : " << std::endl;
    int x, y, z;
    std :: cin >> x >> y >> z;
    std :: cout << "Max Number is : "<< MaxNumber(x,y,z)<< std :: endl; 

    return 0;
} 

int MaxNumber(int x, int y, int z) {

    std :: max(std :: max(x,y),z);
    return z;
    
}
