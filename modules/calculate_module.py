from modules import draw_module as dm
import math as m


def calculate(input_values):
    # [0] velocity, [1] distance, [2] width, [3] sdr, [4] vehicle_length, [5] yellow_time, [6] red_yellow_time
    velocity_mph = input_values[0] * 0.2778
    lane_saturation_intensity = input_values[2] * 525
    evacuation_time = m.ceil((input_values[1] + input_values[4]) / velocity_mph)
    intergreen_time = m.ceil(input_values[5] + evacuation_time)
    lane_saturation_levels = (0.1 * 0.5 * input_values[3]) / lane_saturation_intensity
    lane_saturation_levels_sum = lane_saturation_levels * 2
    lost_time = m.ceil(2 * (intergreen_time - 1))
    minimal_cycle_duration = m.ceil(lost_time / (1 - lane_saturation_levels_sum))
    optimal_cycle_duration = m.ceil((1.5 * lost_time + 5) / (1 - lane_saturation_levels_sum))
    minimal_green_cycle = m.ceil(0.5 * (minimal_cycle_duration - lost_time) - 1)
    optimal_green_cycle = m.ceil(0.5 * (optimal_cycle_duration - lost_time) - 1)
    suboptimal_cycle_duration = m.ceil((minimal_cycle_duration + optimal_cycle_duration) / 2)
    suboptimal_green_cycle = m.ceil((minimal_green_cycle + optimal_green_cycle) / 2)

    for i, dur in enumerate([minimal_cycle_duration, optimal_cycle_duration, suboptimal_cycle_duration]):
        if dur % 2 != 0:
            if i == 0:
                minimal_cycle_duration += 1
            elif i == 1:
                optimal_cycle_duration += 1
            else:
                suboptimal_cycle_duration += 1

    # Create the list of the values
    standard_calc_values = [intergreen_time, input_values[6], input_values[5]]
    calculated_min_values = [minimal_cycle_duration, minimal_green_cycle]
    calculated_min_values.extend(standard_calc_values)
    calculated_subopt_values = [suboptimal_cycle_duration, suboptimal_green_cycle]
    calculated_subopt_values.extend(standard_calc_values)
    calculated_opt_values = [optimal_cycle_duration, optimal_green_cycle]
    calculated_opt_values.extend(standard_calc_values)

    print(f"Standard values: \n"
          f"Velocity: {velocity_mph} m/s\n"
          f"Lane saturation intensity: {lane_saturation_intensity}\n"
          f"Evacuation time: {evacuation_time} s\n"
          f"Intergreen time: {intergreen_time} s\n"
          f"Lane saturation levels: {lane_saturation_levels}\n"
          f"Lane saturation levels sum: {lane_saturation_levels_sum}\n"
          f"Lost time: {lost_time} s\n")
    print(f"Minimal values: \n"
          f"Minimal cycle duration: {minimal_cycle_duration} s\n"
          f"Minimal green cycle: {minimal_green_cycle} s\n")
    print(f"Suboptimal values: \n"
          f"Suboptimal cycle duration: {suboptimal_cycle_duration} s\n"
          f"Suboptimal green cycle: {suboptimal_green_cycle} s\n")
    print(f"Optimal values: \n"
          f"Optimal cycle duration: {optimal_cycle_duration} s\n"
          f"Optimal green cycle: {optimal_green_cycle} s\n")

    inpt = int(input("enter 1 for color, 2 for black and white: \n"))
    calculate_extras(calculated_min_values, inpt)
    calculate_extras(calculated_subopt_values, inpt)
    calculate_extras(calculated_opt_values, inpt)

    print(calculated_opt_values)


# [length_of_cycle, duration_green, intergreen_cycle, yellow_red_duration, yellow_duration]

def calculate_extras(values, inpt):
    k_duration = m.ceil(values[0] / 2)  # duration of cycle for one light
    k_short_red = values[2] - values[4]  # duration of red between yellows
    k_long_red = values[0] - (values[1] + values[4] + k_short_red + values[
        3])  # duration of red during kull K cycle """values[1] + values[2] - values[3]"""
    values.extend([k_duration, k_short_red, k_long_red])
    if all(value > 0 for value in values):

        dm.draw_method_choice(values, inpt)
    else:
        print("theres problem here")
