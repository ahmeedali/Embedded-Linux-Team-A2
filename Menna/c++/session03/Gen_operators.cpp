#include <iostream>

struct operators{  //all the members are public
int x;
int t=10;
void fun(){
    x=t;
}
 void operator=(int x);//it only accepts one operand

int operator%(int z){

    return z%t;
}

int operator*(int z){

    return z*t;
}

int operator&(int z){

    return z&t;
}

int operator>>(int z){

    return z>>1;
}

bool operator==(int z){

    return z==t;
}

void operator()(){       //can be used to implement constructor for a struct

    std::cout << "constructor for struct" << std::endl; 
    
}

};

void operators::operator=(int x){
   operators::x=x; 
}

int main() {
   operators obj{12};   //1-the operator = can be accessed this way
   operators ob;
   ob=11;                  //Or through this
   obj.t=100;
   int u= obj>>(20);      //2-these two operators cant be called inside cout stream
   int r= obj==(100);
   obj();                  //3- constructor like calling
   std::cout << ob.x << std::endl;
   std::cout << obj.x << std::endl;
   std::cout << obj%(20) << std::endl;
   std::cout << obj*(20) << std::endl;
 //  std::cout << obj() << std::endl;       //if we used return "constructor for struct";
   std::cout << u << std::endl;
   std::cout << r << std::endl;
    return 0;
}

