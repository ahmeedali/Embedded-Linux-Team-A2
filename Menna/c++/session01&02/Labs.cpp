#include <algorithm>
#include <cstddef>
#include <cstdlib>
#include <iostream>
#include <vector>

// class Data{
// uint16_t x1;
// int x2;
// int x3;
// };

// int main(void) {

// Data d;

// std::cout << sizeof(d) << std::endl;

//     return 0;
// }
//////////////////////////////// FUNC OVERLOADING ////////////////////////////////////////////////////
///void fun(int x=4,int y);  error the 2nd param should be initialized too or reverse the order
// void fun(float x){ std::cout<<x<<" im float "<<std::endl; }
// void fun(int x,int y=7)
// { std::cout<<x<<" im ffun1 "<<y<<std::endl;}  
// void fun(int x,double y){            
//   std::cout<<x<<" iim fun2 "<<y<<std::endl; //if we put the same line definition it will give an error since the parameters types the same
// }                                           //thats why i changed the y from int to double

// //int fun(int x,int y);                     //this will give an error since : 1-overloaded functions may have same return type (there is no way to differ
//                                             //between 2 func with their return type only) 2-initializing a parameter doesnt make it differ except when calling it

// int multiply(int x,int y){ return x*y;}   //the return type here is different but they are overloaded cause they have different param types
// double multiply(double x1,double y1){ return x1*y1; }

// int main(void) {
// //over loaded functions
// fun(2);  //here it called fun1
// fun(2,2.3);  //here it called fun2 
// fun(static_cast<float>(3.0));  //to change it from double to float

// multiply(2.0,3.3);  //here the fractional numbers by default double ..if you want to use float cast it
// multiply(2,3);

// return 0;
// }
//////////////////////////////////// NULLPTR AND NULL //////////////////////////////////////////////////////
// C++ program to demonstrate problem with NULL
// #include <bits/stdc++.h>
// using namespace std;

// function with integer argument
//void fun(int N) { cout << "fun(int)"<<endl; return;}

// Overloaded function with char pointer argument
//void fun(char* s) { cout << "fun(char *)"; return;}

//int main()
//{
	// Ideally, it should have called fun(char *),
	// but it causes compiler error cause null can be converted to int types also not only the pointer types
	//fun(NULL);

//   fun(nullptr); //only access the pointer types 
//}
/////////////////////////////////////////////////////////////
// C++ program to show comparisons with nullptr
//#include <bits/stdc++.h>
//using namespace std;

// program to test behavior of nullptr
//int main()
//{
	// creating two variables of nullptr_t type
	// i.e., with value equal to nullptr
//	nullptr_t np1, np2;

	// <= and >= comparison always return true ?? both equal nullptr //the program compiled although it shows an error
	// if (np1 <= np2)
	// 	cout << "can compare" << endl;
	// else
	// 	cout << "can not compare" << endl;

	// Initialize a pointer with value equal to np1
//	char *x = np1; // same as x = nullptr (or x = NULL
					// will also work)
// 	if (x == nullptr)
// 		cout << "x is null" << endl;
// 	else
// 		cout << "x is not null" << endl;

// 	return 0;
// }
// int main() {

// int* ptr = new int;
// *ptr = 42;
// delete ptr;
// ptr = nullptr;  //why?????for re-usability??

//     return 0;
// }
/////////////////////////////////////////////// CONST AND CONSTEXPR ///////////////////////////////////////

int getRand()
{
	return rand()%10;
}


constexpr int sum(int a, int b)
{
   a=1;             //1- only 1 line function available in c++11,,multi lines available 

//std::cout<<"Hello"<<a<<std::endl;    //2- cant use any functions that are runtime dependent

//   for (int i=0; i<rand(); i++) {     3- here rand function is runtime dependent ..produces error
//       b=a*i;
//   }

   return a+b;
}



int temp2=20;
int main() {
///////////////////////////////////////////// Refrences /////////////////////////////////////////
// int x{10};
// int &y =x;
// int* ptr= &x;
// y=2;
// std::cout<<" Y is "<<y<<" X is "<<x<<" *ptr is "<<*ptr<<std::endl;   
   
// int n =0;   
// //changing value of Y not the refrence   
// y=n;   
   
// //y=11;   //it still points to the x
   
// std::cout<<" X is "<<x<<" n is " <<n<<std::endl;
///////////////////////////////////////////// AUTO /////////////////////////////////////////
//   const int x =10; 

//   auto ptr = &x;

//   auto var1 = x;             //here var1 is int not const int so we must add const
//   auto  &var2 = x;   //except refrence case it can see the const keyword

//   auto lst={1,2,3,5};

 // auto lst1{1,2,3,5};  gives error in this type of initialization

///////////////////////////////////////////// CAST_Types /////////////////////////////////////////
// int x =10;
// int* ptr =&x;
//float* t= static_cast<float*>(ptr);  1- the cast is not allowed with data types other than the primitive ones
// float y = static_cast<int>(x);

// char a ='a';

//ptr = static_cast<int*>(&a);          2- cant convert between different pointer types

//reinterpret cast: 
//1- used to convert between ddifferent pointer types (use it carefully)
//2- do not use it unless you have a good reason
//ptr = reinterpret_cast<int*>(&a);    //here we will access 4 bytes instead of 1 which may result in bad behaviour
///////////////////////////////////////// LAMBDA EXP /////////////////////////////////////////////////

// std::vector<int> v{1,2,3,5,8};

// /*function to print content of a vector*/
// std::for_each(v.begin(),v.end(),[](int i){
// 	std::cout<<i<<std::endl;
// });

// auto func1=[](int a, int b){

//         return a + b;
// };

// func1(50,5);

////////////// Some Rules of Lambda :

// int temp1=0;

// auto fun2=[](int var){
// //	return var+temp1;   1- cant use global variables to it must passed as parameter or in capture .
// };

// auto fun9 = [temp1](int v)
// {
//   // temp1=12;         2-  the value captured is read only cant be changed
//   int y=temp1;          //or assign its value to a variable then change this variable
//    return temp1 +v;
// };

// auto f3=[&temp1](int v){

//   temp1=21*2;         //3- we can change temp1 througth capturing its refrence (pass by refrence)
//   v=2;
//   return temp1+v;

// };
// //f3(2);
// //std::cout<<temp1<<std::endl;    //temp1 is changed in original variable 

// auto f4=[&](int v){
//   temp2 = 10;
//   temp1=21*2;         //4- capture all the global (to the function) variables (pass by refrence)
//   v=2;
//   return temp2+v;

// };

// // f4(5);
// // std::cout<<temp2<<std::endl; 

// auto f5=[=](int v){
//   temp2 = 10;          //5- capture all the global variables by value (pass by value)
//   //temp1=21*2;             // variables local to functions are read only
//   v=2;
//   return temp2+v;

// };

/*To overcome the previous problem use this*/

// auto f6=[=,&temp1](int v){
//   temp2 = 10;          //6- capture all the global variables by value (pass by value)
//   temp1=21*2;             // variables local to functions are read only
//   v=2;
//   return temp2+v;

// };

// auto fun10 = [temp1](int v)mutable
// {
//   temp1=12;       // 7-  temp1 can be changed if we used mutable keyword
//   int y=temp1;          //or assign its value to a variable then change this variable
//    return temp1 +v;
// };
//note : lambda function consumes more memory(.txt)than ordinary function

//std::cout<<typeid(fun10(5)).name()<<std::endl; //returns int

/////////////////////////////////////////////// CONST AND CONSTEXPR ///////////////////////////////////////


//const int var1=getRand();        

//constexpr int var2=getRand();  //compiler error since the rand function returns its value in the runtime
                                 //constexpr is a way to make sure that this line will be excuted before runtime (during compiletime)

//const int var1=sum(2,3);  
//constexpr int var1=sum(2,3);    //no compiler error ..the function ends in compile time

//constexpr int var1=sum(2,rand()); compiler error since constexpr is the type of var1
// int var1=sum(2,rand());     //no error although sum func is has constexpr qualifier..but here it wont turn into assembly in compile time
// std::cout<<var1<<std::endl;

//////////////////////////////////////////////////////////////////////////////////////////

 return 0;

 }
