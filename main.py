
print("select option 1 for difference\n select option 2 for common ")
option = int(input(" your option : 1.cleaning & output 2.Only cleaning "))
print("you have selected option: ",option)
if __name__ == '__main__':
    if option==1:
        exec(open("Cleaning.py").read())
        exec(open("Output.py").read())
    elif option==2:
        exec(open("cleaning.py").read()) 


print("Refer final.csv in output folder")


  

 
 
