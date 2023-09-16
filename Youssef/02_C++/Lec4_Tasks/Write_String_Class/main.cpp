/***
   Autor      :     YOUSSEF ADEL YOUSSEF
Description   :     Write string class which has members { length - string}
***/

#include <iostream>
#include <cstring>

class MyString 
{
    private:
        char* string;  // Pointer to the character array
        int length;    // Length of the string


    public:
        // Constructor
        MyString(const char* str) 
        {
            length = std::strlen(str);
            string = new char[length + 1]; // +1 for the null terminator
            std::strcpy(string, str);
        }

        // Destructor to free memory
        ~MyString() 
        {
            delete[] string;
        }

        // Member function to get the length
        int getLength() const 
        {
            return length;
        }

        // Member function to get the string
        const char* getString() const 
        {
            return string;
        }
};

int main() 
{
    MyString myStr("Hello, World!");
    std::cout << "Length of the string: " << myStr.getLength() << std::endl;
    std::cout << "String content: " << myStr.getString() << std::endl;

    return 0;
}
