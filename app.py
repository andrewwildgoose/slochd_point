import gpx_service.gpx_parser as parser
import calcs.slochd_calcs as calcs

def calculate_slochd(file_path):
    # Parse the GPX file
    gpx = parser.parse_gpx(file_path)
    
    # Calculate the slochd point
    slochd_value = calcs.calc_slochd(gpx)
    
    return slochd_value

if __name__ == "__main__":
    file_path = input("Enter the path to the GPX file: ")
    slochd_value = calculate_slochd(file_path)
    print(f"The slochd value is: {slochd_value}")