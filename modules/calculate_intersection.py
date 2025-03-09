import math as m
from modules import draw_intersection as di
def calculate_intersection(main_road, secondary_road, base_values):
    """Base values: 
        [0] - velocity (km/h)
        [1] - vehicle length (m)
        [2] - yellow time (s)
        [3] - red-yellow time (s)
        
        main_road:
        [0] - distance (m)
        [1] - width (m)
        [2] - sdr of mein road (vehicles/day)
        
        secondary_road:
        [0] - distance (m)
        [1] - width (m)
        [2] - sdr of secondary road (vehicles/day)"""

    # Calculations for the main road:
    velocity_mph = base_values[0] * 0.2778
    main_lane_saturation_intensity = main_road[1] * 525
    main_evacuation_time = m.ceil((main_road[0] + base_values[1]) / velocity_mph)
    main_intergreen_time = m.ceil(base_values[2] + main_evacuation_time)
    main_lane_saturation_levels_sum = (0.1 * main_road[2])/ main_lane_saturation_intensity
    main_lane_saturation_level = main_lane_saturation_levels_sum / 2
    main_lost_time = m.ceil(2 * (main_intergreen_time - 1))
    main_minimal_cycle_duration = m.ceil(main_lost_time / (1 - main_lane_saturation_levels_sum))
    main_optimal_cycle_duration = m.ceil((1.5 * main_lost_time + 5) / (1 - main_lane_saturation_levels_sum))
    main_suboptimal_cycle_duration = m.ceil((main_minimal_cycle_duration + main_optimal_cycle_duration) / 2)
    main_minimal_green_cycle = m.ceil(0.5 * (main_minimal_cycle_duration - main_lost_time) - 1)
    main_optimal_green_cycle = m.ceil(0.5 * (main_optimal_cycle_duration - main_lost_time) - 1)
    main_suboptimal_green_cycle = m.ceil((main_minimal_green_cycle + main_optimal_green_cycle) / 2)

    for i, dur in enumerate([main_minimal_cycle_duration, main_optimal_cycle_duration, main_suboptimal_cycle_duration]):
        if dur % 2 != 0:
            if i == 0:
                main_minimal_cycle_duration += 1
            elif i == 1:
                main_optimal_cycle_duration += 1
            else:
                main_suboptimal_cycle_duration += 1

    for i, dur in enumerate([main_minimal_green_cycle, main_suboptimal_green_cycle, main_optimal_green_cycle]):
        if dur < 8:
            if i == 0:
                main_minimal_green_cycle = 8
            if i == 1:
                main_suboptimal_green_cycle = 8
            if i == 2:
                main_optimal_green_cycle = 8
    # Calculations for the secondary road:
    secondary_lane_saturation_intensity = secondary_road[1] * 525
    secondary_evacuation_time = m.ceil((secondary_road[0] + base_values[1]) / velocity_mph)
    secondary_intergreen_time = m.ceil(base_values[2] + secondary_evacuation_time)
    secondary_lane_saturation_levels_sum = (0.1 * secondary_road[2])/ secondary_lane_saturation_intensity
    secondary_lane_saturation_level = secondary_lane_saturation_levels_sum / 2
    secondary_lost_time = m.ceil(2 * (secondary_intergreen_time - 1))
    secondary_minimal_cycle_duration = m.ceil(secondary_lost_time / (1 - secondary_lane_saturation_levels_sum))
    secondary_optimal_cycle_duration = m.ceil((1.5 * secondary_lost_time + 5) / (1 - secondary_lane_saturation_levels_sum))
    secondary_suboptimal_cycle_duration = m.ceil((secondary_minimal_cycle_duration + secondary_optimal_cycle_duration) / 2)
    secondary_minimal_green_cycle = m.ceil(0.5 * (secondary_minimal_cycle_duration - secondary_lost_time) - 1)
    secondary_optimal_green_cycle = m.ceil(0.5 * (secondary_optimal_cycle_duration - secondary_lost_time) - 1)
    secondary_suboptimal_green_cycle = m.ceil((secondary_minimal_green_cycle + secondary_optimal_green_cycle) / 2)

    for i, dur in enumerate([secondary_minimal_cycle_duration, secondary_optimal_cycle_duration, secondary_suboptimal_cycle_duration]):
        if dur % 2 != 0:
            if i == 0:
                secondary_minimal_cycle_duration += 1
            elif i == 1:
                secondary_optimal_cycle_duration += 1
            else:
                secondary_suboptimal_cycle_duration += 1

    for i, dur in enumerate([secondary_minimal_green_cycle, secondary_suboptimal_green_cycle, secondary_optimal_green_cycle]):
        if dur < 8:
            if i == 0:
                secondary_minimal_green_cycle = 8
            if i == 1:
                secondary_suboptimal_green_cycle = 8
            if i == 2:
                secondary_optimal_green_cycle = 8

    # Create the list of the values
    """[0] - main cycle duration, [1] - secondary cycle duration, [2] - main green cycle, [3] - secondary green cycle,
    [4] - main intergreen time, [5] - secondary intergreen time, [6] - yellow time, [7] - red-yellow time"""
    minimal_cycle_solution = [main_minimal_cycle_duration, secondary_minimal_cycle_duration, main_minimal_green_cycle,
                              secondary_minimal_green_cycle, main_intergreen_time, secondary_intergreen_time,
                              base_values[2], base_values[3]]
    suboptimal_cycle_solution = [main_suboptimal_cycle_duration, secondary_suboptimal_cycle_duration,
                                 main_suboptimal_green_cycle, secondary_suboptimal_green_cycle, main_intergreen_time,
                                 secondary_intergreen_time, base_values[2], base_values[3]]
    optimal_cycle_solution = [main_optimal_cycle_duration, secondary_optimal_cycle_duration, main_optimal_green_cycle,
                              secondary_optimal_green_cycle, main_intergreen_time, secondary_intergreen_time,
                              base_values[2], base_values[3]]

    """[0] - velocity (m/s), [1] - main lane saturation intensity, [2] - secondary lane saturation intensity,
        [3] - main evacuation time (s), [4] - secondary evacuation time (s), [5] - main intergreen time (s),
        [6] - secondary intergreen time (s), [7] - main lane saturation levels, [8] - secondary lane saturation levels,
        [9] - main lane saturation levels sum, [10] - secondary lane saturation levels sum, [11] - main lost time (s),
        [12] - secondary lost time (s), [13] - main minimal cycle duration (s), [14] - secondary minimal cycle duration (s),
        [15] - main minimal green cycle (s), [16] - secondary minimal green cycle (s), [17] - main suboptimal cycle duration (s),
        [18] - secondary suboptimal cycle duration (s), [19] - main suboptimal green cycle (s), [20] - secondary suboptimal green cycle (s),
        [21] - main optimal cycle duration (s), [22] - secondary optimal cycle duration (s), [23] - main optimal green cycle (s),
        [24] - secondary optimal green cycle (s)"""

    rapport_values = [velocity_mph, main_lane_saturation_intensity, secondary_lane_saturation_intensity,
                      main_evacuation_time, secondary_evacuation_time, main_intergreen_time, secondary_intergreen_time,
                      main_lane_saturation_level, secondary_lane_saturation_level, main_lane_saturation_levels_sum,
                      secondary_lane_saturation_levels_sum, main_lost_time, secondary_lost_time,
                      main_minimal_cycle_duration, secondary_minimal_cycle_duration, main_minimal_green_cycle,
                      secondary_minimal_green_cycle, main_suboptimal_cycle_duration,
                      secondary_suboptimal_cycle_duration,
                      main_suboptimal_green_cycle, secondary_suboptimal_green_cycle, main_optimal_cycle_duration,
                      secondary_optimal_cycle_duration, main_optimal_green_cycle, secondary_optimal_green_cycle]
    print(rapport_values)

    color = int(input("give 1 or 2 as color check: "))
    calculate_extras_intersection(minimal_cycle_solution, color)
    calculate_extras_intersection(suboptimal_cycle_solution, color)
    calculate_extras_intersection(optimal_cycle_solution, color)
"""[0] - main cycle duration, [1] - secondary cycle duration, [2] - main green cycle, [3] - secondary green cycle,
    [4] - main intergreen time, [5] - secondary intergreen time, [6] - yellow time, [7] - red-yellow time"""
def calculate_extras_intersection(cycle_solution,color):
    k_main_duration = cycle_solution[0] / 2
    k_secondary_duration = cycle_solution[1] / 2
    main_short_red = cycle_solution[4] - cycle_solution[6]
    secondary_short_red = cycle_solution[5] - cycle_solution[6]
    main_long_red = cycle_solution[0] - (cycle_solution[2] + cycle_solution[6] + main_short_red + cycle_solution[7])
    secondary_long_red = cycle_solution[1] - (cycle_solution[3] + cycle_solution[6] + secondary_short_red + cycle_solution[7])
    full_cycle_duration = (cycle_solution[2]*2 + cycle_solution[3] + cycle_solution[4]*2 + cycle_solution[5])

    cycle_solution.extend([k_main_duration, k_secondary_duration, main_short_red, secondary_short_red, main_long_red, secondary_long_red, full_cycle_duration])
    """[0] - main cycle duration, [1] - secondary cycle duration, [2] - main green cycle, [3] - secondary green cycle,
        [4] - main intergreen time, [5] - secondary intergreen time, [6] - yellow time, [7] - red-yellow time [8] - k_main_duration,
        [9] - k_secondary_duration, [10] - main short red, [11] - secondary short red, [12] - main long red, [13] - secondary long red,
        [14] - full cycle duration"""
    di.draw_inter_method_choice(cycle_solution, color)

