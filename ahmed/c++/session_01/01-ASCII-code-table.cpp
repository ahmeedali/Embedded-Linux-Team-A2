#include <iostream>

int main ()
{

    int i,j;
    std :: cout <<" \t ASCII code table\n" << "---------------------------------" << std::endl;
    std :: cout << "|     ascii\t" <<  "|   character\t|\n" << "---------------------------------" << std::endl;
    for (i = 33; i < 127 ;i++)
    std :: cout <<"|\t"<< i << "\t|\t" <<(char)i  <<"\t|" << std::endl;

 return 0;
} 