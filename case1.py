
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и выводит название этого дня недели.
""""
day = int(input("Input number day week: "))
if day==1:  print("Monday")
if day==2:  print("Tuesday")
if day==3:  print("Wednesday")
if day ==4: print("Thursday")
if day ==5: print("Friday")
if day ==6: print("Saturday")
if day ==7: print("Sunday")
else: print("There are 7 days in a week")
"""""""""
day = int(input("Input number day week: "))
match day:
    case 1:
        {
            print("Monday")
        }
    case 2:
        {
            print("Tuesday")
        }
    case 3:
        {
            print("Wednesday")
        }
    case 4:
        {
            print("Thursday")
        }
    case 5:
        {
            print("Friday")
            
        }
    case 6:
        {
            print("Saturday")
        }
    case 7:
        {
            print("Sunday") 
        }
    case 8:
        {
             print("Error, in a week of 7 days") 
        }
