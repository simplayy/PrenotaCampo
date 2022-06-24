from math import sin, cos, radians, acos
from django.conf import settings
import json
import os
# http://en.wikipedia.org/wiki/Earth_radius
# """For Earth, the mean radius is 6,371.009 km (˜3,958.761 mi; ˜3,440.069 nmi)"""
EARTH_RADIUS_IN_MILES = 3958.761

def calc_dist_fixed(lat_a, long_a, lat_b, long_b):
    """all angles in degrees, result in miles"""
    lat_a = radians(lat_a)
    lat_b = radians(lat_b)
    delta_long = radians(long_a - long_b)
    cos_x = (
        sin(lat_a) * sin(lat_b) +
        cos(lat_a) * cos(lat_b) * cos(delta_long)
        )
    return acos(cos_x) * EARTH_RADIUS_IN_MILES

def find_istat_json(json_object, name):
        for dict in json_object:
            if '-' in dict['cap']:
                l,h = map(int, dict['cap'].split('-'))
                for r in range(l,h+1):
                    if str(r) == name:
                        return dict['istat']

            elif dict['cap'] == name:
                return dict['istat']
        return "0"

def find_lng_json(json_object, name):
        for dict in json_object:
            if dict['istat'] == name:
                return dict['lng']
        return "0"

def find_lat_json(json_object, name):
        for dict in json_object:
            if dict['istat'] == name:
                return dict['lat']
        return "0"

def find_comune_json(json_object, name):
        for dict in json_object:
            if dict['istat'] == name:
                return dict['comune']
        return "0"

def cap_to_lat(cap):
    f = open(os.path.join( settings.BASE_DIR, 'gestione/geo/italy_cap.json' ))
    jsonData = json.load(f)
    istat = "0"
    try:
        istat = find_istat_json(jsonData, str(cap))
        
    except KeyError:
        print("cap doesn't exist")
    f.close()
    
    f = open(os.path.join( settings.BASE_DIR, 'gestione/geo/italy_geo.json' ))
    jsonData = json.load(f)
    
    lat = "0"
    try:
        lat = find_lat_json(jsonData, istat)
    except KeyError:
        print("lat doesn't exist")

    print(lat)
    return float(lat)


def cap_to_lng(cap):
    f = open(os.path.join( settings.BASE_DIR, 'gestione/geo/italy_cap.json' ))
    jsonData = json.load(f)
    istat = "0"
    try:
        istat = find_istat_json(jsonData, str(cap))
        
    except KeyError:
        print("cap doesn't exist")
    f.close()
    
    f = open(os.path.join( settings.BASE_DIR, 'gestione/geo/italy_geo.json' ))
    jsonData = json.load(f)
    
    lng = "0"
    try:
        lng = find_lng_json(jsonData, istat)
    except KeyError:
        print("lng doesn't exist")

  
    return float(lng)


def cap_to_comune(cap):
    f = open(os.path.join( settings.BASE_DIR, 'gestione/geo/italy_cap.json' ))
    jsonData = json.load(f)
    istat = "0"
    try:
        istat = find_istat_json(jsonData, str(cap))
        
    except KeyError:
        print("cap doesn't exist")
    f.close()
    
    f = open(os.path.join( settings.BASE_DIR, 'gestione/geo/italy_geo.json' ))
    jsonData = json.load(f)
    
    comune = ""
    try:
        comune = find_comune_json(jsonData, istat)
    except KeyError:
        print("comune doesn't exist")

    
    return comune