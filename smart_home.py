'''
Task: convert c to f
Name: c_to_f
Input: degrees_c
Side Effects: no
Return: degrees_f
'''
def c_to_f(degrees_c):
    degrees_c = float(degrees_c)
    degrees_f = (degrees_c * 9/5) + 32
    return degrees_f


'''
Task: tell the user the current temperature
Name: print_temp
Input: temp_in_f
Side Effects: "The temperature is: x"
Return: no
'''
def print_temp(temp_in_f):
    print("The temperature is: ", temp_in_f)
    return None


temp_in_c = input("What is the temp in C? ") #asks for the temp in c
f_degrees = c_to_f(temp_in_c) # converts it to f
print_temp(f_degrees) # calls the fn to tell the user the temp