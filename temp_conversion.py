"""convert_cel_to_far() which takes one float parameter representing
degrees Celsius and returns a float representing the same temperature 
in degrees Fahrenheit using the following formula:
F = C * 9/5 + 32"""

"""convert_far_to_cel() which take one float parameter representing
degrees Fahrenheit and returns a float representing the same temperature in degrees Celsius using the following formula:
C = (F - 32) * 5/9"""


def cel_to_far(c_deg):
    f = (c_deg * 9 / 5) + 32
    return f"{c_deg} degrees C is {f:.1f} degrees F"


def far_to_cel(f_deg):
    c = (f_deg - 32) * 5 / 9
    return f"{f_deg} degrees F is {c:.1f} degrees C"


def start_program():
    start = True
    while start:
        try:
            cels = float(input("enter a temp in degrees C: "))
            cel_temp = cel_to_far(cels)
            print(cel_temp)
            print()
            far = float(input("enter a temp in degrees F: "))
            far_temp = far_to_cel(far)
            print(far_temp)
            start = False
                
        except ValueError:
            print("you must enter a numeric value")
            
    
    
start_program()
