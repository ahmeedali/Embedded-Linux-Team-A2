#include <iostream>
/***
   Autor      :     YOUSSEF ADEL YOUSSEF
Description   :     Handle interrupt signal like (ctrl+c)
***/

#include <csignal>
#include <unistd.h>

// Define a flag to check if Ctrl+C was pressed
bool ctrlCPressed = false;

// Signal handler function to handle Ctrl+C
void signalHandler(int signum) 
{
    if (signum == SIGINT) {
        std::cout << "Ctrl+C pressed. Exiting gracefully..." << std::endl;
        ctrlCPressed = true;
    }
}

int main() 
{
    // Register the signal handler for Ctrl+C
    signal(SIGINT, signalHandler);

    std::cout << "Press Ctrl+C to trigger the signal handler." << std::endl;

    // Main loop
    while (!ctrlCPressed) 
    {
        std::cout << "Wait Interrupt Singal by (Ctrl + C)" << std::endl;
        sleep(2);
    }

    return 0;
}
