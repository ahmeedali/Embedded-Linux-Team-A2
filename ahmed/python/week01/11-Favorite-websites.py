#!/usr/bin/python3
import webbrowser
print ("1-freepik \n2-Illustrator Online editor \n3-Photo Online editor")
url= int (input ("Choose 1 ,2 or 3 : "))

websites= {1:'https://www.freepik.com',
           2:"https://fixthephoto.com/illustrator-online-editor.html",
           3:"https://www.photopea.com/"}
if  url in websites :
    webbrowser.open_new_tab(websites[url])
print (websites[url])