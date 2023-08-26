#!/usr/bin/python3

import pyautogui
from time import sleep

# Pause time interval between each pyautogui command
pyautogui.PAUSE = 1

# Opening Visual Studio Code
pyautogui.hotkey('win')
pyautogui.write('vs')
vscode = pyautogui.locateOnScreen("vscode.png", confidence=0.8, minSearchTime=4)
if(vscode):
    pyautogui.press('enter')
sleep(4)

# This function is used for clearing the search bar
def clear_extensions_search():
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.hotkey('delete')


# Installing clangd

# Accessing the Extensions search
pyautogui.hotkey('ctrl', 'shift', 'x')

# Clearing search bar
clear_extensions_search()

# Type clangd in the search bar
pyautogui.write('clangd')

# Locate clangd in the extensions options
clangd_loc = pyautogui.locateOnScreen("clangd.png", minSearchTime=8, confidence=0.8)

# Check for loacting clangd
if(clangd_loc):
    # print(clangd_loc.width, clangd_loc.height)

    # Open clangd from the Extensions options
    clangd_x, clangd_y = pyautogui.locateCenterOnScreen("clangd.png", confidence=0.8)
    pyautogui.moveTo(clangd_x, clangd_y)
    pyautogui.click()

    # Check that clangd has opened
    clangd_entry = pyautogui.locateOnScreen("clangd_entry.png", minSearchTime=5, confidence=0.8)
    
    if(clangd_entry):
        clangd_entry_x, clangd_entry_y = pyautogui.locateCenterOnScreen("clangd_entry.png", confidence=0.8)
        clangd_tuple = (clangd_entry_x, clangd_entry_y, clangd_entry.width, clangd_entry.height)
        clangd_install_x, clangd_install_y = pyautogui.locateCenterOnScreen("install.png", confidence=0.8, region=clangd_tuple)
        pyautogui.moveTo(clangd_install_x, clangd_install_y)
        pyautogui.click()
        sleep(4)

clangd_installed = pyautogui.locateOnScreen("clangd_installed.png", minSearchTime=5, confidence=0.8)

if(clangd_installed):
    print("Clangd installed successfuly\n")
else:
    print("Clangd installation unsuccessful\n")



# Installing cpp testmate

# Accessing the Extensions search
pyautogui.hotkey('ctrl', 'shift', 'x')

# Clearing search bar
clear_extensions_search()

# Type cpp testmate in the search bar
pyautogui.write('c++ testmate')

# Locate cpp testmate in the extensions options
cpp_testmate_loc = pyautogui.locateOnScreen("cpp_testmate.png", minSearchTime=8, confidence=0.8)

# Check for loacting cpp_testmate
if(cpp_testmate_loc):
    # print(cpp_testmate_loc.width, cpp_testmate_loc.height)

    # Open cpp_testmate from the Extensions options
    cpp_testmate_x, cpp_testmate_y = pyautogui.locateCenterOnScreen("cpp_testmate.png", confidence=0.8)
    pyautogui.moveTo(cpp_testmate_x, cpp_testmate_y)
    pyautogui.click()

    # Check that cpp_testmate has opened
    cpp_testmate_entry = pyautogui.locateOnScreen("cpp_testmate_entry.png", minSearchTime=5, confidence=0.8)
    
    if(cpp_testmate_entry):
        cpp_testmate_entry_x, cpp_testmate_entry_y = pyautogui.locateCenterOnScreen("cpp_testmate_entry.png", confidence=0.8)
        cpp_testmate_tuple = (cpp_testmate_entry_x, cpp_testmate_entry_y, cpp_testmate_entry.width, cpp_testmate_entry.height)
        cpp_testmate_install_x, cpp_testmate_install_y = pyautogui.locateCenterOnScreen("install.png", confidence=0.8, region=cpp_testmate_tuple)
        pyautogui.moveTo(cpp_testmate_install_x, cpp_testmate_install_y)
        pyautogui.click()
        sleep(4)

cpp_testmate_installed = pyautogui.locateOnScreen("cpp_testmate_installed.png", minSearchTime=5, confidence=0.8)

if(cpp_testmate_installed):
    print("C++ Testmate installed successfuly\n")
else:
    print("C++ Testmate installation unsuccessful\n")



# Installing cpp helper

# Accessing the Extensions search
pyautogui.hotkey('ctrl', 'shift', 'x')

# Clearing search bar
clear_extensions_search()

# Type cpp helper in the search bar
pyautogui.write('c++ helper')

# Locate cpp helper in the extensions options
cpp_helper_loc = pyautogui.locateOnScreen("cpp_helper.png", minSearchTime=8, confidence=0.8)

# Check for loacting cpp helper
if(cpp_helper_loc):
    # print(cpp_helper_loc.width, cpp_helper_loc.height)

    # Open cpp_helper from the Extensions options
    cpp_helper_x, cpp_helper_y = pyautogui.locateCenterOnScreen("cpp_helper.png", confidence=0.8)
    pyautogui.moveTo(cpp_helper_x, cpp_helper_y)
    pyautogui.click()

    # Check that cpp_helper has opened
    cpp_helper_entry = pyautogui.locateOnScreen("cpp_helper_entry.png", minSearchTime=10, confidence=0.7)
    
    if(cpp_helper_entry):
        cpp_helper_entry_x, cpp_helper_entry_y = pyautogui.locateCenterOnScreen("cpp_helper_entry.png", confidence=0.7)
        cpp_helper_tuple = (cpp_helper_entry_x, cpp_helper_entry_y, cpp_helper_entry.width, cpp_helper_entry.height)
        cpp_helper_install_x, cpp_helper_install_y = pyautogui.locateCenterOnScreen("install.png", confidence=0.8, region=cpp_helper_tuple)
        pyautogui.moveTo(cpp_helper_install_x, cpp_helper_install_y)
        pyautogui.click()
        sleep(4)

cpp_helper_installed = pyautogui.locateOnScreen("cpp_helper_installed.png", minSearchTime=5, confidence=0.8)

if(cpp_helper_installed):
    print("C++ Helper installed successfuly\n")
else:
    print("C++ Helper installation unsuccessful\n")



# Installing cmake

# Accessing the Extensions search
pyautogui.hotkey('ctrl', 'shift', 'x')

# Clearing search bar
clear_extensions_search()

# Type cmake in the search bar
pyautogui.write('cmake')

# Locate cmake in the extensions options
cmake_loc = pyautogui.locateOnScreen("cmake.png", minSearchTime=8, confidence=0.8)

# Check for loacting cmake
if(cmake_loc):
    # print(cmake_loc.width, cmake_loc.height)

    # Open cmake from the Extensions options
    cmake_x, cmake_y = pyautogui.locateCenterOnScreen("cmake.png", confidence=0.8)
    pyautogui.moveTo(cmake_x, cmake_y)
    pyautogui.click()

    # Check that cmake has opened
    cmake_entry = pyautogui.locateOnScreen("cmake_entry.png", minSearchTime=10, confidence=0.8)
    
    if(cmake_entry):
        cmake_entry_x, cmake_entry_y = pyautogui.locateCenterOnScreen("cmake_entry.png", confidence=0.8)
        cmake_tuple = (cmake_entry_x, cmake_entry_y, cmake_entry.width, cmake_entry.height)
        cmake_install_x, cmake_install_y = pyautogui.locateCenterOnScreen("install.png", confidence=0.8, region=cmake_tuple)
        pyautogui.moveTo(cmake_install_x, cmake_install_y)
        pyautogui.click()
        sleep(4)

cmake_installed = pyautogui.locateOnScreen("cmake_installed.png", minSearchTime=5, confidence=0.8)

if(cmake_installed):
    print("Cmake installed successfuly\n")
else:
    print("Cmake installation unsuccessful\n")



# Installing cmake tools

# Accessing the Extensions search
pyautogui.hotkey('ctrl', 'shift', 'x')

# Clearing search bar
clear_extensions_search()

# Type cmake tools in the search bar
pyautogui.write('cmake to')

# Locate cmake tools in the extensions options
cmake_tools_loc = pyautogui.locateOnScreen("cmake_tools.png", minSearchTime=8, confidence=0.8)

# Check for loacting cmake tools
if(cmake_tools_loc):
    # print(cmake_tools_loc.width, cmake_tools_loc.height)

    # Open cmake_tools from the Extensions options
    cmake_tools_x, cmake_tools_y = pyautogui.locateCenterOnScreen("cmake_tools.png", confidence=0.8)
    pyautogui.moveTo(cmake_tools_x, cmake_tools_y)
    pyautogui.click()

    # Check that cmake_tools has opened
    cmake_tools_entry = pyautogui.locateOnScreen("cmake_tools_entry.png", minSearchTime=5, confidence=0.7)

    if(cmake_tools_entry):
        cmake_tools_entry_x, cmake_tools_entry_y = pyautogui.locateCenterOnScreen("cmake_tools_entry.png", minSearchTime=5, confidence=0.7)
        cmake_tools_tuple = (cmake_tools_entry_x, cmake_tools_entry_y, cmake_tools_entry.width, cmake_tools_entry.height)
        cmake_tools_install_x, cmake_tools_install_y = pyautogui.locateCenterOnScreen("cmake_tools_install.png", confidence=0.8, region=cmake_tools_tuple)
        pyautogui.moveTo(cmake_tools_install_x, cmake_tools_install_y)
        pyautogui.click()
        sleep(4)

cmake_tools_installed = pyautogui.locateOnScreen("cmake_tools_installed.png", minSearchTime=5, confidence=0.8)

if(cmake_tools_installed):
    print("cmake_tools installed successfuly\n")
else:
    print("cmake_tools installation unsuccessful\n")

