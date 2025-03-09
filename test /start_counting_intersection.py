from modules import calculate_intersection as ci

# Define the velocity (km/h)
velocity = 40
# Define the distance of the main road(m)
main_distance = 250
# Define the distance of the secondary road(m)
secondary_distance = 150
# Define the width of the main road (m)
main_width = 3
# Define the width of the secondary road (m)
secondary_width = 3
# Define an average traffic
main_sdr = 7000
secondary_sdr = 3000
# Define the typical vehicle length (m)
vehicle_length = 10
# Define the yellow time (s)
yellow_time = 3
# Define the red-yellow time (s)
red_yellow_time = 1

main_road = [main_distance, main_width, main_sdr]
secondary_road = [secondary_distance, secondary_width, secondary_sdr]
base_values = [velocity, vehicle_length, yellow_time, red_yellow_time]

# Call the calculate_intersection function
ci.calculate_intersection(main_road, secondary_road, base_values)