from modules import math_module as cm

length_of_cycle = 64  # sample input of the length of the cycle
duration_green = 18  # sample input of the duration of the green light
intergreen_cycle = 14  # sample input of the duration of the intergreen
yellow_red_duration = 1  # standard value of the duration of the yellow-red light
yellow_duration = 3  # standard value of the duration of the yellow light

input_values = [length_of_cycle, duration_green, intergreen_cycle, yellow_red_duration, yellow_duration]

inpt = int(input(f"What would you to debug? \n"
                    f"1 Calculate the values and plot \n"
                    f"2 Only draw module \n"))
if inpt == 1:
    cm.calculate(input_values)
elif inpt == 2:
    cm.draw(input_values)
else:
    print("wrong input")