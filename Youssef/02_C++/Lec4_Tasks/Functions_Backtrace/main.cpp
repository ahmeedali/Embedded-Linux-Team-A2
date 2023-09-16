/***
   Autor      :     YOUSSEF ADEL YOUSSEF
Description   :     Create A class that can be use to make backtrace for calling functions
***/

#include <iostream>
#include <vector>
#include <string>

// A class for logging function enter and exit events
class BacktraceLogger 
{
    public:
        // Constructor to log function entry
        BacktraceLogger(const std::string& functionName) : functionName(functionName) 
        {
            std::cout << "Enter to [" + functionName + "]" << std::endl;
            logEnter();
        }

        // Destructor to log function exit
        ~BacktraceLogger() 
        {
            std::cout << "Exit from [" + functionName + "]" << std::endl;
            logExit();
        }

        // Static method to print the backtrace
        static void printBacktrace() 
        {
            std::cout << "Back Trace as follows:" << std::endl;
            for (int i = 0; i < trace.size(); i++) 
            {
                std::cout << i << "- " << trace[i] << std::endl;
            }
            std::cout << "Back Trace is Finished" << std::endl;
        }

    private:
        // Private method to log function entry
        void logEnter() 
        {
            trace.push_back(functionName);
        }

        // Private method to log function exit
        void logExit() 
        {
            trace.push_back(functionName);
        }

        // Static vector to store the backtrace
        static std::vector<std::string> trace;
        std::string functionName;
};

// Initialize the static vector for the backtrace
std::vector<std::string> BacktraceLogger::trace;

// Example functions
void fun3() 
{
    BacktraceLogger logger("fun3");
    BacktraceLogger::printBacktrace();       // Print the backtrace
}

void fun2() 
{
    BacktraceLogger logger("fun2");
    fun3();
}

void fun1() 
{
    BacktraceLogger logger("fun1");
    fun2();
}

int main() 
{
    BacktraceLogger logger("main");
    fun1();

    return 0;
}
