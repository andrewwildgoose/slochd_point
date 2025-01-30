import logging
import gpx_service.gpx_parser as parser
import calcs.slochd_calcs as calcs

from objects.route import Route

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)d]')

def calculate_slochd(file_path):
    logging.info(f"Starting to process the file: {file_path}")
    
    # Parse the GPX file
    try:
        with open(file_path, 'r') as gpx_file:

            gpx_distance_km = parser.get_distance_km(gpx_file)
        logging.info("GPX file parsed successfully")
    except Exception as e:
        logging.error(f"Failed to parse GPX file: {e}", exc_info=True)
        raise
    
    # Calculate the slochd point
    try:
        gpx_in_miles = calcs.km_to_miles(gpx_distance_km)
        slochd_value = calcs.calc_slochd(gpx_in_miles)
        logging.info("Slochd value calculated successfully")
    except Exception as e:
        logging.error(f"Failed to calculate slochd value: {e}", exc_info=True)
        raise
    
    return slochd_value

def build_route(file_path):
    logging.info(f"Starting to process the file: {file_path}")
    
    # Parse the GPX file
    try:
        with open(file_path, 'r') as gpx_file:

            gpx_distance_km = parser.get_distance_km(gpx_file)
        logging.info("GPX file parsed successfully")
    except Exception as e:
        logging.error(f"Failed to parse GPX file: {e}", exc_info=True)
        raise

if __name__ == "__main__":
    try:
        file_path = input("Enter the path to the GPX file: ").strip('"')
        slochd_value = calculate_slochd(file_path)
        logging.info(f"The slochd value is: {slochd_value}")
    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)
        print(f"An error occurred: {e}")