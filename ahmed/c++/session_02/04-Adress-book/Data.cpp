// #include "Data.hpp"
#include "Data.hpp"
#include <algorithm>

AddressBook_queue::AddressBook_queue() {}

void AddressBook_queue::Add() {

  std::cout << "Enter name, sex, phone, and address (separated by Enter): ";

  std ::cin >> name >> sex >> phone >> address;

  auto person =
      std::make_pair(std::make_pair(std::make_pair(name, sex), phone), address);
  qperson.push_back(person);
}
void AddressBook_queue::Delete_last() {
  if (qperson.empty()) {
    std::cerr << "There are no contacts in the address book." << std::endl;
    return;
  }
  qperson.pop_back();
  std::cout << "the last contact deleted successfully" << std::endl;
}

void AddressBook_queue::ShowList() {
  std::sort(qperson.begin(), qperson.end());
  if (qperson.empty()) {
    std::cerr << "There are no contacts in the address book." << std::endl;
    return;
  }
  std::cout << "Contact List:" << std::endl;
  for (auto i : qperson) {
    std::cout << "- " << i.first.first.first << " | " << i.first.first.second
              << " | " << i.first.second << " | " << i.second << " | "
              << std::endl;
  }
}

void AddressBook_queue::search() {
  std::string name;
  std::cout << "Enter a name for the search: ";
  std::cin >> name;
  auto contact = std ::find_if(
      qperson.begin(), qperson.end(),
      [name](std::pair<std::pair<std::pair<std::string, char>, std::string>,
                       std::string>
                 found) { return found.first.first.first == name; });

  if (contact != qperson.end()) {

    std::cout << "Contact found: (" << contact->first.first.first << ", "
              << contact->first.first.second << ", " << contact->first.second
              << ", " << contact->second << ")" << std::endl;
  } else {
    std::cout << "contact not found." << std::endl;
  }
}

void AddressBook_queue::Delete_all() {
  qperson.clear();
  std::cout << "All contacts have been deleted." << std::endl;
}

void AddressBook_queue::Modfiy() {
  std::string name;
  std::cout << "Enter the name of the contact you want to modify: ";
  std::cin >> name;
  auto contact = std ::find_if(
      qperson.begin(), qperson.end(),
      [name](std::pair<std::pair<std::pair<std::string, char>, std::string>,
                       std::string>
                 found) { return found.first.first.first == name; });

  if (contact != qperson.end()) {

    std::cout << "Contact found: (" << contact->first.first.first << ", "
              << contact->first.first.second << ", " << contact->first.second
              << ", " << contact->second << ")" << std::endl;

    std::cout << "Enter new information (name, sex, phone, address): ";
    std::cin >> name >> sex >> phone >> address;

    contact->first.first.first = name;
    contact->first.first.second = sex;
    contact->first.second = phone;
    contact->second = address;

    std::cout << "Contact updated successfully." << std::endl;
  } else {
    std::cout << "contact not found." << std::endl;
  }
}

void AddressBook_queue::ExportToCSV() {
  std::cout << "Exporting to CSV..." << std::endl;
}

void AddressBook_queue::menu() {

  int choice;

  while (true) {
    std::cout << "\nAddress Book Menu:\n" << std::endl;
    std::cout << "1. Add a new contact" << std::endl;
    std::cout << "2. Delete last contact" << std::endl;
    std::cout << "3. Show contact list" << std::endl;
    std::cout << "4. Search for a contact" << std::endl;
    std::cout << "5. Delete all contacts" << std::endl;
    std::cout << "6. Modify a contact" << std::endl;
    std::cout << "7. Export to CSV" << std::endl;
    std::cout << "0. Quit" << std::endl;
    std::cout << "Enter your choice: ";
    std::cin >> choice;

    switch (choice) {
    case 1:
      Add();
      break;
    case 2:
      Delete_last();
      break;
    case 3:
      ShowList();
      break;
    case 4:
      search();
      break;
    case 5:
      Delete_all();
      break;
    case 6:
      Modfiy();
      break;
    case 7:
      ExportToCSV();
      break;
    case 0:
      std::cout << "Exiting the program." << std::endl;
      return;
    default:
      std::cout << "Invalid choice. Please try again." << std::endl;
      break;
    }
  }
}
