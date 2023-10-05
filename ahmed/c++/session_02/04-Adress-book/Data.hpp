#ifndef DATA_H
#define DATA_H
#include <iostream>
#include <vector>
#include <deque>

#pragma once

class AddressBook_queue {
    std::string name;
    std::string address;
    std::string phone;
    char sex;
    public:
        std::vector <std::pair<std::pair < std::pair<std::string,char>,std::string>,std::string>> qperson;  
        AddressBook_queue();
        void Add();
        void Delete_last();
        void ShowList();
        void search();
        void Delete_all();
        void Modfiy();
        void ExportToCSV();
        void menu();

};


#endif