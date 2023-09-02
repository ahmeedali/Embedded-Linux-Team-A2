""" 
   Autor      :   Youssef Adel Youssef
Description   :   write a Python program for Write and Read from Excel sheet
"""i

mport openpyxl


def Read_Excel_File(File_Path):
    workbook = openpyxl.load_workbook(File_Path)
    sheet = workbook.active
    
    for row in sheet.iter_rows(values_only = True):
        print(row)
        
    workbook.close()


def Write_Excel_File(File_Path):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    
    data = [
        ["Name" , "Age" , "City"],
        ["Ahmed" , "31" , "Egypt"],
        ["John" , "28" , "New Yourk"],
        ["Youssef" , "27" , "Egypt"]
    ]
    
    for row in data:
        sheet.append(row)
        
    workbook.save(File_Path)
    workbook.close()


Write_Excel_File("Example.xlsx")
Read_Excel_File("Example.xlsx")