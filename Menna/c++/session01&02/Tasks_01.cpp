#include <iostream>
#include <iomanip>
#include <bitset>

//Task: summing the digits in a number :
int num =0;
int sum = 0;

int main(){

std::cout<<"Please enter the number you want to add : ";
std::cin >> num;

while(num>0)
{  
   sum += num%10;
   num = num/10;  
}
std::cout << "The Sum of digits is : "<< sum <<std::endl;
return 0;

}
/////////////////////////////////////////////////////////////////////////
//Task2: printing the ascii table :

int main(void)
{
     char a;
     int num = 0;

    std::cout<<"The Ascii table :"<<std::endl;
    std::cout<<"+--------+--------+"<<std::endl;
    std::cout<<"|  Char  |  Ascii |"<<std::endl;
    std::cout<<"+--------+--------+"<<std::endl;
    while (num < 128) {
    a=num; 
    if(a<31) { std::cout<<"|"<< "   "<< "  "<<" |"<< "  "<<num << "  "<<" |" <<std::endl;} 
    else{std::cout<<"|"<< "   "<< a << "  "<<" |"<< "  "<<num << "  "<<" |" <<std::endl;} 
    
    num++;

    }
    

    return 0;
}
//////////////////////////////////////////////////////////////////////////
//Task 3 : changing from decimal to binary and vice versa :

int main()
{
    int num = 0;
    std::bitset<16>binary;

    std::cout<<"Enter the decimal number : ";
    std::cin >> num ;
    std::cout<<"the binary equivalent : "<< std::bitset<16>(num)<<std::endl;

    std::cout<<"Enter the binary number : ";
    std::cin >> binary;
    std::cout<<"the decimal equivalent  : "<< binary.to_ulong()<<std::endl;

    return 0;
}
