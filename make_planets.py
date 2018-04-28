class planet(object):

    name = ''
    colour = ''
    radius = 0.
    x_position = 0.
    y_position = 0.


def make_planets():

    mercury = planet()
    mercury.name = 'Mercury'
    mercury.radius = 0.387
    mercury.colour = 'orange4'
    mercury.x_position = mercury.radius
    mercury.y_position = 0.

    venus = planet()
    venus.name = 'Venus'
    venus.radius = 0.723
    venus.colour = 'goldenrod'
    venus.x_position = venus.radius
    venus.y_position = 0.
 
    earth = planet()
    earth.name = 'Earth'
    earth.radius = 1
    earth.colour = 'DodgerBlue'
    earth.x_position = earth.radius
    earth.y_position = 0.

    mars = planet()
    mars.name = 'Mars'
    mars.radius = 1.524
    mars.colour = 'orange4'
    mars.x_position = mars.radius
    mars.y_position = 0.

    jupiter = planet()
    jupiter.name = 'Jupiter'
    jupiter.radius = 5.203
    jupiter.colour = 'bisque'
    jupiter.x_position = jupiter.radius
    jupiter.y_position = 0.

    saturn = planet()
    saturn.name = 'Saturn'
    saturn.radius = 9.539
    saturn.colour = 'gold'
    saturn.x_position = saturn.radius
    saturn.y_position = 0.

    uranus = planet()
    uranus.name = 'Uranus'
    uranus.radius = 19.18
    uranus.colour = 'CadetBlue'
    uranus.x_position = uranus.radius
    uranus.y_position = 0.

    neptune = planet()
    neptune.name = 'Neptune'
    neptune.radius = 30.06
    neptune.colour = 'SlateBlue'
    neptune.x_position = neptune.radius
    neptune.y_position = 0.

    pluto = planet()
    pluto.name = 'Pluto'
    pluto.radius = 39.53
    pluto.colour = 'gray'
    pluto.x_position = pluto.radius
    pluto.y_position = 0.

    planet_list = [mercury, venus, earth, mars, jupiter, saturn, neptune, uranus, pluto]
    return planet_list
