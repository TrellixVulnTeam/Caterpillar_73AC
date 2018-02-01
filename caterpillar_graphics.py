""" Graphics for caterpillar """

from vpython import *
from random import random, shuffle

def make_head(caterpillar_pos, forward, upward):
    """ Make caterpillar head """
    right = cross(forward, upward)
    head_ball = sphere(pos=caterpillar_pos[0], color=color.orange)
    left_eye = sphere(pos=caterpillar_pos[0] + 0.5*forward + 0.5*upward - 
                      0.4*right, radius=0.35)
    right_eye = sphere(pos=caterpillar_pos[0] + 0.5*forward + 0.5*upward +
                       0.4*right, radius=0.35)
    left_pupil = sphere(pos=caterpillar_pos[0] + 0.6*forward + 0.56*upward - 0.42*right,
                        radius=0.25, color=color.black)
    right_pupil = sphere(pos=caterpillar_pos[0] + 0.6*forward + 0.56*upward
                         + 0.42*right, radius=0.25, color=color.black)
    head = compound([head_ball, left_eye, right_eye, left_pupil, right_pupil])
    return head

def make_helmet(caterpillar_pos, forward, upward):
    """ Make caterpillar helmet """
    right = cross(forward, upward)
    helmet = sphere(pos=caterpillar_pos[0] + 0.1*forward + 0.15*upward - 
                    0*right, radius=1.2, opacity=0.3)
    return helmet

def make_body(caterpillar_pos, head, forward, upward):
    """ Make caterpillar body """
    body = [head]
    right = cross(forward, upward)
    for increment in range(1, 5):
        body_sphere = sphere(pos=caterpillar_pos[increment], color=color.blue)
        left_foot = sphere(pos=caterpillar_pos[increment] + 0*forward -
                           0.6*upward - 0.5*right, radius=0.3, color=color.orange)
        right_foot = sphere(pos=caterpillar_pos[increment] + 0*forward -
                            0.6*upward + 0.5*right, radius=0.3, color=color.orange)
        body_segment = compound([body_sphere, left_foot, right_foot])
        body.append(body_segment)
    return body

def make_suit(caterpillar_pos, helmet, forward, upward):
    """ Make caterpillar suit """
    suit = [helmet]
    right = cross(forward, upward)
    body_sphere = sphere(pos=caterpillar_pos[1], radius=1.1,
                         color=color.white)
    left_foot = sphere(pos=caterpillar_pos[1] + 0*forward -
                       0.6*upward - 0.5*right, radius=0.4, color=color.black)
    right_foot = sphere(pos=caterpillar_pos[1] +  0*forward -
                        0.6*upward + 0.5*right, radius=0.4, color=color.black)
    back_pack = box(pos=caterpillar_pos[1] + vector(0, 1.1, 0), width=1.8,
                    height=0.3, length=1, color=color.white)
    back_pack_decal = box(pos=caterpillar_pos[1] +  0*forward + 1.15*upward + 0*right, width=1.2,
                          height=0.25, length=0.8, color=color.white)
    left_jet = cylinder(pos=caterpillar_pos[1] - 0.6*forward + 1.1*upward + 0.9*right,
                        radius=0.25, length=1.1, color=color.white)
    right_jet = cylinder(pos=caterpillar_pos[1] - 0.6*forward + 1.1*upward - 0.9*right,
                         radius=0.25, length=1.1, color=color.white)
    left_jet_cap = sphere(pos=caterpillar_pos[1] + 0.5*forward + 1.1*upward + 0.9*right,
                          radius=0.25, color=color.white)
    right_jet_cap = sphere(pos=caterpillar_pos[1] + 0.5*forward + 1.1*upward - 0.9*right,
                           radius=0.25, color=color.white)
    left_jet_nozzle = cone(pos=caterpillar_pos[1] -0.9*forward + 1.1*upward + 0.9*right,
                           radius=0.25, color=color.black)
    right_jet_nozzle = cone(pos=caterpillar_pos[1] -0.9*forward + 1.1*upward - 0.9*right,
                            radius=0.25, color=color.black)
    back_pack_offset = box(pos=caterpillar_pos[1] + 0*forward - 1.1*upward + 0*right, width=1.8,
                           height=0.3, length=1, opacity=0)
    body_segment = compound([body_sphere, left_foot, right_foot, back_pack,
                             left_jet, right_jet, left_jet_cap, right_jet_cap,
                             left_jet_nozzle, right_jet_nozzle,
                             back_pack_decal, back_pack_offset])
    suit.append(body_segment)
    for increment in range(2, 5):
        body_sphere = sphere(pos=caterpillar_pos[increment], radius=1.1,
                             color=color.white)
        left_foot = sphere(pos=caterpillar_pos[increment] + 0*forward -
                           0.6*upward - 0.5*right, radius=0.4, color=color.black)
        right_foot = sphere(pos=caterpillar_pos[increment] + 0*forward -
                            0.6*upward + 0.5*right, radius=0.4, color=color.black)
        body_segment = compound([body_sphere, left_foot, right_foot])
        suit.append(body_segment)
    return suit

def make_planets(number_of_planets):
    """ Makes planets """
    planets = []
    planet = sphere(pos=vector(40, -10, 0), radius=20, texture=textures.wood_old)
    # Test planet. Remove when reinstating all planets
    planets.append(planet)
    # Test planet. Remove when reinstating all planets
    # for _ in range(number_of_planets):
    #     planet = sphere(pos=vector(int(150*random() - 50), int(150*random() - 50),
    #                                int(150*random()) - 50),
    #                     radius=int(20*random()), texture=textures.wood_old)
    #     if norm(planet.pos).equals(vector(0, 1, 0)) or norm(planet.pos).equals(vector(0, -1, 0)):
    #         planet.pos += vector(1, 0, 0)
    #     planets.append(planet)
    return planets

def make_food(planets):
    """ Distributes food on planets """
    for planet in planets:
        foods = []
        number_of_food = 3
        # for _ in range(int(5*random() + 5)): # makes 5-10 pellets
        #     food_pos = norm(vector(random() - 0.5, random() - 0.5,
        #                            random() - 0.5))*planet.radius + planet.pos
        #     food = sphere(pos=food_pos, texture=textures.rock)
        #     foods.append(food)
        colorlist = [color.blue, color.cyan, color.green, color.magenta,
                     color.orange, color.red, color.yellow, color.black, color.white]
        toward_zero = norm(-planet.pos)*planet.radius
        perp_to_zero = norm(cross(toward_zero, vector(0, -1, 0)))
        for num in range(number_of_food):
            shuffle(colorlist)
            food_pos = norm(toward_zero + ((perp_to_zero * (num - number_of_food/2)) * 2)
                           ) * (planet.radius + 0.5) + planet.pos
            food = cone(pos=food_pos, color=colorlist.pop(), axis=perp_to_zero*2)
            foods.append(food)
        planet.food = foods
    return
