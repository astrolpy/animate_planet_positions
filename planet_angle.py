import numpy as np
import math
import astropy
import astropy.coordinates
from astropy.time import Time
from datetime import datetime


def planet_angle(planet, year, month, day, hour, minute, seccond):
    
    
    t = Time(datetime(year, month, day, hour, minute, seccond), scale='utc')
    print(t)
    
    #Get ccords of the planet anf the sun (relative to earth which is 0,0)
    coords_body = astropy.coordinates.get_body(planet.name, t)
    coords_sun = astropy.coordinates.get_body('sun', t)
    
    #Convert to cartesian
    coords_body = [coords_body.cartesian.x.value, coords_body.cartesian.y.value]
    coords_sun = [coords_sun.cartesian.x.value, coords_sun.cartesian.y.value]

    #Shift so sun is at 0, 0 
    coords_body = [coords_body[0] - coords_sun[0], coords_body[1] - coords_sun[1]]

    planet.angle = math.degrees(math.atan2(coords_body[1], coords_body[0]))



