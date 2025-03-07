from modules import draw_module as dm


def calculate(input_values):
    # [0] velocity, [1] distance, [2] width, [3] sdr, [4] vehicle_length, [5] yellow_time, [6] red_yellow_time
    velocity_mph = input_values[0] * 0.2778
    lane_saturation_intensity = input_values[2] * 525
    evacuation_time = (input_values[1] + input_values[4]) / velocity_mph
    intergreen_time = input_values[5] + evacuation_time
    lane_saturation_levels = (0.1 * input_values[3]) / lane_saturation_intensity
    lane_saturation_levels_sum = lane_saturation_levels * 2
    lost_time = 2 * (intergreen_time - 1)
    minimal_cycle_duration = lost_time / (1 - lane_saturation_levels_sum)
    optimal_cycle_duration = (1.5 * lost_time + 5) / (1 - lane_saturation_levels)
    minimal_green_cycle = 0.5 * (minimal_cycle_duration - lost_time) - 1
    optimal_green_cycle = 0.5 * (optimal_cycle_duration - lost_time) - 1
    calculated_min_values = [minimal_cycle_duration, minimal_green_cycle, intergreen_time, input_values[6],
                             input_values[5]]
    calculated_opt_values = [optimal_cycle_duration, optimal_green_cycle, intergreen_time, input_values[6],
                             input_values[5]]
    print("Minimal values: ", calculated_min_values)
    print("Optimal values: ", calculated_opt_values)
    calculate_extras(calculated_min_values)
    calculate_extras(calculated_opt_values)

# [length_of_cycle, duration_green, intergreen_cycle, yellow_red_duration, yellow_duration]

def calculate_extras(values):
    k_duration = values[0] / 2  # duration of cycle for one light
    k_short_red = values[2] - values[4]  # duration of red between yellows
    k_long_red = values[1] + values[2] - values[3]  # duration of red during kull K cycle
    values.extend([k_duration, k_short_red, k_long_red])
    if all(value > 0 for value in values):
        dm.draw_method_choice(values)
    else:
        print("theres problem here")