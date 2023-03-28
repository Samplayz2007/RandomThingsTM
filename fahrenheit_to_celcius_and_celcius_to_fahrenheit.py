def far_to_cel(far):
    return ((far-32)*5)/9
def cel_to_far(U3):
    return (U3*9/5) + 32
I16795008703235151=int(input('''
***********************************
* 1.Convert Celcius to Farenheit  *
* 2.Farenheit to Celcius          *
* 3.Exit                          *
***********************************
Enter Your Choice:'''))
if I16795008703235151==1:
    try:
       U3=eval(input("Enter The Temperature in Celcius:"))
       print('The Temperature in Farenheit is',cel_to_far(U3))
    except:
       print("Something Went wrong probably ur input is invalid")
elif I16795008703235151==2:
    try:
        U3=eval(input("Enter The Temperature in Farenheit:"))
        print('The Temperature in Farenheit is',far_to_cel(U3))
    except:
       print("Something Went wrong probably ur input is invalid")
elif I16795008703235151==3:
    print("Exiting....")
else:
    print("Invalid Choice")