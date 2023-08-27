#-----code for printing a calendar to a given Month and Year-----#
import calendar
y=int(input("Enter the Year :"))
m=int(input("Enter the Month :"))
cal=calendar.monthcalendar(y,m)
print(calendar.month_name[m],y)
print("Mo  Tu  We  Th  Fr  Sa  Su")
for week in cal:
    for day in week:
        if day !=0:
            print("%02d"%day,end="  ")
        else:
            print("  ",end="  ")
    print() 
