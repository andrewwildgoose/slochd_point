import gpxpy
import gpxpy.gpx

def parse_gpx(gpx_file):
    gpx = gpxpy.parse(gpx_file)
    total_distance = 0.0

    for track in gpx.tracks:
        for segment in track.segments:
            total_distance += segment.length_3d()

    print(f'Total distance: {total_distance} meters')
    return total_distance