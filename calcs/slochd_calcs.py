# 1 mile = 1.609344 km
# 1 km = 0.621371192 miles
M_TO_KM_RATIO = 1.609344
KM_TO_M_RATIO = 0.621371192

# Will return slochd point in miles for miles total dist
SLOCHD_RATIO_3 = 0.6167619 # My calculation
SLOCHD_RATIO_4 = 0.61728395 # ChatGTP'S calculation

def calc_slochd(dist):
    '''
    Return the point at which the number of miles from the start is equal to the kilometers to the finish.
    INPUT:
        dist - float - total distance of the route in miles
    OUTPUT:
        slochd_point - float - point at which the number of miles from the start is equal to the kilometers to the finish
    '''
    slochd_point_m = dist * SLOCHD_RATIO_3

    slochd_point_km = miles_to_km(slochd_point_m)
    slochd_dict = {'km': slochd_point_km, 'miles': slochd_point_m}  

    return slochd_dict

def miles_to_km(miles):
    '''
    Convert miles to kilometers
    INPUT:
        miles - float - distance in miles
    OUTPUT:
        kilometers - float - distance in kilometers
    '''
    kilometers = miles * M_TO_KM_RATIO
    return kilometers

def km_to_miles(kilometers):
    '''
    Convert kilometers to miles
    INOUT:
        kilometers - float - distance in kilometers
    OUTPUT:
        miles - float - distance in miles
    '''
    miles = kilometers * KM_TO_M_RATIO
    return miles