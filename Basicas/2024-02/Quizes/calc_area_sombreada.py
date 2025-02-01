import math

def calculate_shaded_area(inner_circle_radius):
    
    outer_circle_radius = inner_circle_radius*2

    outer_circle_area = (outer_circle_radius**2)

    inner_circles_area = (inner_circle_radius**2)*2

    return outer_circle_area-inner_circles_area
#
# print(f"Shaded area without pi: {calculate_shaded_area(4)}")
# print(f"Shaded area is: {calculate_shaded_area(4)*math.pi}")

def calc_semicircles_attached_to_square_area(square_area):
    
    semicircle_diameter = math.sqrt(square_area)
    semicircle_radius = square_area/2

    area_circle_without_pi = (semicircle_radius**2)
    area_all_circles = area_circle_without_pi*2
    
    #print(f"{area_all_circles}/")
    return area_all_circles

print(calc_semicircles_attached_to_square_area(49/9))

