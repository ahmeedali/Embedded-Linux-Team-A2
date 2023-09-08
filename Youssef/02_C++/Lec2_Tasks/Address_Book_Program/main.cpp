/***
   Autor      :     Youssef Adel Youssef
Description   :     Write Program to create address book program
***/

#include <iostream>
#include <string>

struct Contact
{
    std::string name;
    std::string phoneNumber;
    std::string email;
};

const int MAX_CONTACTS = 100; // Maximum number of contacts

int main() 
{
    Contact addressBook[MAX_CONTACTS]; // Array to store contacts
    int numContacts = 0; // Number of contacts in the address book

    while (true) 
    {
        std::cout << "\nAddress Book Menu:\n";
        std::cout << "1. Add Contact\n";
        std::cout << "2. Update Contact\n";
        std::cout << "3. Search Contact\n";
        std::cout << "4. List All Contacts\n";
        std::cout << "5. Delete Contact\n";
        std::cout << "6. Delete All Contacts\n";
        std::cout << "7. Exit\n";
        std::cout << "Enter your choice: ";

        
        int choice;
        std::cin >> choice; // Read user's choice


        switch (choice) 
        {
            case 1:
                if (numContacts < MAX_CONTACTS) 
                { // Check if the address book is not full
                    Contact newContact;
                    std::cout << "Enter Name: ";
                    std::cin.ignore(); // Clear any previous input
                    std::getline(std::cin, newContact.name); // Read the name with spaces
                    std::cout << "Enter Phone Number: ";
                    std::cin >> newContact.phoneNumber;
                    std::cout << "Enter Email: ";
                    std::cin >> newContact.email;

                    addressBook[numContacts] = newContact; // Add the new contact to the array
                    numContacts++; // Increment the contact count
                    std::cout << "Contact added successfully!\n";
                } 
                
                else 
                {
                    std::cout << "Address book is full. Cannot add more contacts.\n";
                }
                break;
            
            
            case 2:
                if (numContacts > 0) 
                { // Check if there are contacts to update
                    std::string searchName;
                    std::cout << "Enter the name of the contact you want to update: ";
                    std::cin.ignore(); // Clear any previous input
                    std::getline(std::cin, searchName); // Read the name with spaces

                    bool contactFound = false;
                    for (int i = 0; i < numContacts; i++) 
                    {
                        if (addressBook[i].name == searchName) 
                        { // Find the contact by name
                            std::cout << "Enter New Phone Number: ";
                            std::cin >> addressBook[i].phoneNumber;
                            std::cout << "Enter New Email: ";
                            std::cin >> addressBook[i].email;
                            contactFound = true;
                            std::cout << "Contact updated successfully!\n";
                            break; // Stop searching once the contact is found
                        }
                    }

                    if (!contactFound) 
                    {
                        std::cout << "Contact not found.\n";
                    }
                } 
                
                else 
                {
                    std::cout << "Address book is empty. Cannot update contacts.\n";
                }
                break;
            
            
            case 3:
                if (numContacts > 0) 
                { // Check if there are contacts to search
                    std::string searchName;
                    std::cout << "Enter the name of the contact you want to search for: ";
                    std::cin.ignore(); // Clear any previous input
                    std::getline(std::cin, searchName); // Read the name with spaces

                    bool contactFound = false;
                    for (int i = 0; i < numContacts; i++) 
                    {
                        if (addressBook[i].name == searchName) // Find the contact by name
                        { 
                            std::cout << "Name: " << addressBook[i].name << "\n";
                            std::cout << "Phone Number: " << addressBook[i].phoneNumber << "\n";
                            std::cout << "Email: " << addressBook[i].email << "\n";
                            contactFound = true;
                            break; // Stop searching once the contact is found
                        }
                    }

                    if (!contactFound) 
                    {
                        std::cout << "Contact not found.\n";
                    }
                } 
                
                else 
                {
                    std::cout << "Address book is empty. Cannot search for contacts.\n";
                }
                break;
            
            
            case 4:
                if (numContacts > 0) // Check if there are contacts to list
                { 
                    std::cout << "List of All Contacts:\n";
                    for (int i = 0; i < numContacts; i++) 
                    {
                        std::cout << "Contact " << i + 1 << ":\n";
                        std::cout << "Name: " << addressBook[i].name << "\n";
                        std::cout << "Phone Number: " << addressBook[i].phoneNumber << "\n";
                        std::cout << "Email: " << addressBook[i].email << "\n";
                        std::cout << "-----------------------------\n";
                    }
                } 
                
                else 
                {
                    std::cout << "Address book is empty. No contacts to list.\n";
                }
                break;
            

            case 5:
                if (numContacts > 0)  // Check if there are contacts to delete
                { 
                    std::string deleteName;
                    std::cout << "Enter the name of the contact you want to delete: ";
                    std::cin.ignore(); // Clear any previous input
                    std::getline(std::cin, deleteName); // Read the name with spaces

                    bool contactDeleted = false;
                    for (int i = 0; i < numContacts; i++) 
                    {
                        if (addressBook[i].name == deleteName) // Find the contact by name
                        { 
                            // Shift the remaining contacts to fill the gap
                            for (int j = i; j < numContacts - 1; j++) 
                            {
                                addressBook[j] = addressBook[j + 1];
                            }
                            numContacts--; // Decrement the contact count
                            contactDeleted = true;
                            std::cout << "Contact deleted successfully!\n";
                            break; // Stop searching once the contact is found and deleted
                        }
                    }

                    if (!contactDeleted) 
                    {
                        std::cout << "Contact not found.\n";
                    }
                } 
                
                else 
                {
                    std::cout << "Address book is empty. Cannot delete contacts.\n";
                }
                break;


            case 6:
                if (numContacts > 0) // Check if there are contacts to delete
                { 
                    // Clear all contacts by resetting the number of contacts to zero
                    numContacts = 0;
                    std::cout << "All contacts deleted successfully!\n";
                } 
                
                else 
                {
                    std::cout << "Address book is already empty. No contacts to delete.\n";
                }
                break;
            
            
            case 7:
                std::cout << "Exiting the address book program.\n";
                return 0; // Exit the program
            
            
            default:
                std::cout << "Invalid choice. Please select a valid option.\n";
                break;
        }
    std::cout << "\n===========================================================\n";
    }

    return 0;
}
