#ifndef ARRAY_H
#define ARRAY_H
#include <array>
#include <algorithm>



struct Array
{
    std::array < int, 10> arr{{5,50,6,97,54,12,45,78,32,94}};

    Array();
    void find_max_number();
    void search_for_number();
    void delete_number();
    int merge_two();
    void even_and_odd();
                                      
    ~Array();
};


#endif