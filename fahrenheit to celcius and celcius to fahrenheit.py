def far_to_cel(far):
    return ((far-32)*5)/9
def cel_to_far(cel):
    return (cel*9/5) + 32
choice=int(input('''
***********************************
* 1.Convert Celcius to Farenheit  *
* 2.Farenheit to Celcius          *
* 3.Exit                          *
***********************************
Enter Your Choice:'''))
if choice==1:
    try:
       cel=eval(input("Enter The Temperature in Celcius:"))
       print('The Temperature in Farenheit is',cel_to_far(cel))
    except:
       print("Something Went wrong probably ur input is invalid")
elif choice==2:
    try:
        cel=eval(input("Enter The Temperature in Farenheit:"))
        print('The Temperature in Farenheit is',far_to_cel(cel))
    except:
       print("Something Went wrong probably ur input is invalid")
elif choice==3:
    print("Exiting....")
else:
    print("Invalid CHoice")