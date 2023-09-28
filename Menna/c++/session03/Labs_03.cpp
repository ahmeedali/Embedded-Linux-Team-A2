///////////////////////////////// ENUM ///////////////////////////////////////////
//c style :
// enum type {
// RED,
// Blue,
// Green=4,
// Black
// };

// int main(int argc, const char** argv) {

// enum type obj;
// std::cout << RED << std::endl;    //1- can be accessed directly

// std::cout << obj << std::endl;    //2-prints first member in obj

// //obj{Black};                     //3-this type of definition cant be used
// obj=Black;
// std::cout << obj << std::endl;
// //obj=1;                           //4-cant assign int to enum type object but the opposite can happen
//     return 0;
// }
//////////////////////////
//c++ style :
// enum class type {
// RED,
// Blue,
// Green=4,
// Black
// };

// int main() {

// type obj;
//  //   std::cout << obj << std::endl;  //1-cant be printed as in c
// std::cout << (int)obj << std::endl;   //2-use casting to print it
// std::cout << static_cast<int>(obj) << std::endl; 

// obj=type::Blue;                        //3-accessed through enum name
// std::cout << (int)type::Black << std::endl;  
//     return 0;
// }

////////////////////////// classes ///////////////////////////

// class Master;                                  //forward declaration of a class

// class object {

// private:

// int x=0;
// int y=0;
// friend class Master;                           //To access private members of this class
// public:                         

// object(){std::cout << "constructor called" << std::endl;}   // 1- or object()=default;

// object(int var,int var2) :x(var) ,y(var2)        // 4- this initializer list used only with constructors
// {                                                // 2- must create constructor if you created parameterised one
//                                                  //5- less code is used here due to initializer list
//     std::cout << "Param constructor called" << std::endl;
//     std::cout << " var : "<< var << std::endl;
// }

// ~object(){std::cout << "Destructor called" << std::endl;}

// void set_fun(int var1)
// {                                   // 3- if we didnt call this function outside the class(not used)it wont be in .txt section 
//                                     //(to overcome this define the fun outside the class)
//     x=var1;
// }

// int get_fun();

// };

// int  object::get_fun(){
//  std::cout << this << std::endl;      //8- this used inside this inside the class related things only--it points to the class instance 
// return x;
// }

// class Master{

// private:

// object b1;                            //14- static members are related to the class blueprint 
// static int kx;                       //11- must be defined outside the class wether public or private
// static const int ky=8;               //12- can be defined here or outside
// public:

// static int jk;                       

// void fun1()
// {
//   kx = b1.x;                        //10- we can access the private var of object class
// }

// };

// int Master::kx=52; 
// //const int Master::ky=5;
// int Master::jk=5; 

// int main() {

// // //object ob;                              //6- ordinary const also called this way      
// // object ob1(2,3);                          //5- param const used this way cant be called on 2 steps

// // //ob();                                   //7- used to call () operator not constructor 

// // ob1.get_fun();               
// // std::cout << &ob1<< std::endl;            //9- "this" points to instance address

// std::cout << Master::jk<< std::endl;         //13- public can be accessed from class directly
// //std::cout << Master::kx<< std::endl;       // 15- any private member cant be accessed from the class directly


// return 0;
// }
/////////////////////////////// Parsing ////////////////////////
// int main() {

// std::string stream="MennaSayed  5562  gh8232";    //every string is parsed 

// int ID;
// std::string Name;
// std::string Pass;

// std::stringstream ss(stream);  //converting to string stream

// ss>>Name>>ID>>Pass;                //parsing the stream

// std::cout<<Name<<" "<<typeid(Name).name()<<std::endl;
// std::cout<<ID<<" "<<typeid(ID).name()<<std::endl;
// std::cout<<Pass<<" "<<typeid(Pass).name()<<std::endl;


//     return 0;
// }
