#include <iostream>
#include <math.h>


bool IsRight(unsigned int a, unsigned int b , unsigned int c);


int main()
{
    int a,b,c;
    std :: cout<< "Enter sides of the triangle : " << std::endl;
    std::cin >> a >> b >> c;
    if (IsRight(a,b,c))
    std::cout << a <<","<< b << ","<< c << "," << "is right angle triagnle "<< std::endl;
    else
    std::cout << a <<","<< b << ","<< c << "," << "is not right angle triagnle "<< std::endl;

return 0;

}

bool IsRight(unsigned int a, unsigned int b , unsigned int c){
 a = pow(a,2);
 b = pow(b,2); 
 c = pow(c,2);

    return ((a + b == c)||(c + b == a)||(c + a == b)); 
 
}