import gpxpy
import gpxpy.gpx

def get_distance_km(gpx_file):
    print(f'Parsing GPX file: {gpx_file}, type: {type(gpx_file)}')
    gpx = gpxpy.parse(gpx_file)

    total_distance = 0.0

    for track in gpx.tracks:
        for segment in track.segments:
            total_distance += segment.length_3d()

    print(f'Total distance: {total_distance} meters')
    total_distance_km = total_distance / 1000
    print(f'Total distance: {total_distance_km} KM')
    return total_distance_km