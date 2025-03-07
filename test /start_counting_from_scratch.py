from modules import calculate_module as cm

# Define the velocity (km/h)
velocity = 30
# Define the distance (m)
distance = 204
# Define the width of the road (m)
width = 3
# Define an average traffic
sdr = 4800
# Define the typical vehicle length (m)
vehicle_length = 10
# Define the yellow time (s)
yellow_time = 3
# Define the red-yellow time (s)
red_yellow_time = 1

input_values = [velocity, distance, width, sdr, vehicle_length, yellow_time, red_yellow_time]
cm.calculate(input_values)