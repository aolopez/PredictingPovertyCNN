import requests
import shutil
import numpy as np

dhs_countries = ['malawi','nigeria','rwanda','tanzania','uganda']
lsms_countries = ['malawi','nigeria','tanzania','uganda']

def create_base_path(country_string, data_type):
    return '/Users/alejandrol/Documents/coding/CNNSat/predicting-poverty/data/output/%s/%s/candidate_download_locs.txt' % (data_type, country_string)
def get_coordinates(base_path):
    return np.loadtxt(base_path)
def create_output_base_path(country_string, data_type):
    return '/Users/alejandrol/Documents/coding/CNNSat/predicting-poverty/data/output/%s/%s/downloaded_locs.txt' % (data_type, country_string)
def download_image(url, output_path):
    request_data = url
    out_path = output_path
    response = requests.get(request_data, stream = True)
    with open(out_path, 'wb') as f:
        shutil.copyfileobj(response.raw, f)
def create_image_base_path(country_string, data_type, line):
    return '/Users/alejandrol/Documents/coding/CNNSat/predicting-poverty/data/output/%s/%s/images/%i.jpg' % (data_type, country_string, line)
def create_url(lat,lon):
    return 'https://maps.googleapis.com/maps/api/staticmap?format=jpg&maptype=satellite&center=%f,%f&zoom=16&size=400x400&key=AIzaSyDBqluvfC5fnV8ukIWWX5VNa_eHl68YDkw' % (lat,lon)

if __name__ == "__main__":
    for LSMS_CNT in lsms_countries:
        print '------------ %s ------------------' % LSMS_CNT
        coordinates = get_coordinates(create_base_path(LSMS_CNT, 'LSMS'))
        out_path = create_output_base_path(LSMS_CNT, 'LSMS')
        out_file = open(out_path, "w+")
        coordinates_count = 0
        for lat,lon,clat,clon in coordinates:
            percentage_done = coordinates_count*100.0/len(coordinates)
            if percentage_done % 5 ==0:
                print '%s ----- %i, percentage done: %i' % (LSMS_CNT, coordinates_count, percentage_done)
            url = create_url(lat,lon)
            image_file = create_image_base_path(LSMS_CNT, 'LSMS', coordinates_count)
            download_image(url, image_file)
            out_file.write('%s %f %f %f %f\n' % (image_file, lat, lon, clat, clon))
            coordinates_count += 1
        out_file.close()
