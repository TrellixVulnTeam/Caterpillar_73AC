''' Snake clone '''

from math import acos
from vpython import *
from caterpillar_graphics import make_body, make_food, make_head, make_helmet, make_suit, make_planets

keyevent = ''

def direction(event):
    ''' Capture keyboard interupt and choose new direction and new orientation '''
    # value = event.key
    global keyevent
    keyevent = event.key

def change_direction(forward, upward, turn, turn_axis):
    ''' Checking keyevent value and uddate direction if keyevent is not empty '''
    global keyevent
    if keyevent == 'a':
        forward = -cross(forward, upward)
        turn = radians(90)
        turn_axis = upward
    if keyevent == 'd':
        forward = cross(forward, upward)
        turn = radians(90)
        turn_axis = -upward
    if keyevent == 'w':
        forward, upward = upward, -forward
        turn = radians(90)
        turn_axis = cross(forward, upward)
    if keyevent == 's':
        forward, upward = -upward, forward
        turn = radians(90)
        turn_axis = -cross(forward, upward)
    keyevent = ''
    return forward, upward, turn, turn_axis

def planet_direction(forward, upward, turn, turn_axis, on_planet, planets):
    ''' Checking keyevent value and uddate direction while on planet.'''
    global keyevent
    # planet planet planet planet planet planet planet
    if keyevent == 'a':
        forward = -cross(forward, upward)
        forward = forward.rotate(1/planets[on_planet].radius, -cross(forward, upward))
        #turn and turn_axis not yet adapted
        #this means the caterpillar body's legs and face will get out of sync with the planet
        turn = radians(90)
        turn_axis = upward
    # planet planet planet planet planet planet planet
    if keyevent == 'd':
        forward = cross(forward, upward)
        forward = forward.rotate(1/planets[on_planet].radius, -cross(forward, upward))
        #turn and turn_axis not yet adapted
        #this means the caterpillar body's legs and face will get out of sync with the planet
        turn = radians(90)
        turn_axis = -upward
    # planet planet planet planet planet planet planet
    if keyevent == 'w':
        forward, upward = upward, -forward
        turn = radians(90)
        on_planet = None
        turn_axis = cross(forward, upward)
    # planet planet planet planet planet planet planet
    if keyevent == '':
        turn_axis = -cross(forward, upward)
        turn = 1/planets[on_planet].radius
        forward = forward.rotate(1/planets[on_planet].radius, -cross(forward, upward))
        print(forward)
    # planet planet planet planet planet planet planet
    keyevent = ''
    return forward, upward, turn, turn_axis, on_planet, planets

def main():
    ''' Main loop '''
    scene.bind('keydown', direction)

    global keyevent # Listening for key presses

    forward = vector(1, 0, 0)
    upward = vector(0, 1, 0)
    turn = 0
    turn_axis = vector(0, 1, 0)

    caterpillar_pos = []  # Initialize Caterpillar position. Head in origo
    for dummy in range(5):
        caterpillar_pos.append(vector(-dummy, 0, 0))

    head = make_head() # Make Caterpillar head
    body = make_body(caterpillar_pos, head) # Make Caterpillar body
    helmet = make_helmet()
    suit = make_suit(caterpillar_pos, helmet)
    sleep(0.01)
    planets = make_planets(10) # Makes planets
    make_food(planets) # Distribute food on the planets

    d_t = 0.2
    on_planet = None
    while True:
        if on_planet != None:
            helmet.visible = False
            for segment in suit:
                segment.visible = False
            upward = norm(head.pos-planets[on_planet].pos)
            forward, upward, turn, turn_axis, on_planet, planets = planet_direction(forward, upward, turn, turn_axis, on_planet, planets)
        else:
            helmet.visible = True
            for segment in suit:
                segment.visible = True
            forward, upward, turn, turn_axis = change_direction(forward, upward, turn, turn_axis)

            for num1, planet in enumerate(planets): # Checking if a planet is reached
                if mag(planet.pos-head.pos) <= planet.radius:
                    on_planet = num1
                    core_to_head = norm(head.pos-planet.pos)*planet.radius
                    head.pos = core_to_head + planet.pos + 0.5*norm(core_to_head)
                    caterpillar_pos[0] = head.pos
                    new_forward = norm(forward - proj(forward, core_to_head))
                    if new_forward == 0: # If incomming is vertical new_forward = 0
                        new_forward = upward
                        turn = radians(90)
                    turn = acos(dot(forward, new_forward) / (mag(forward)*mag(new_forward)))
                    upward = norm(core_to_head)
                    forward = norm(new_forward)
                    turn_axis = cross(forward, upward)

        if dot(forward, upward) > 1:
            print(forward, upward)
            return

        old_caterpillar_pos = caterpillar_pos[:]  # Moving the caterpillar
        caterpillar_pos[0] += forward
        body[0].rotate(angle=turn, axis=turn_axis)
        body[0].pos = caterpillar_pos[0]
        suit[0].rotate(angle=turn, axis=turn_axis)
        suit[0].pos = caterpillar_pos[0]
        for num, segment in enumerate(body):
            if num == 0:
                continue
            segment.pos = old_caterpillar_pos[num - 1]
            suit[num].pos = old_caterpillar_pos[num - 1]
            # if turn > 0:
            segment.rotate(angle=turn, axis=turn_axis)
            suit[num].rotate(angle=turn, axis=turn_axis)
            caterpillar_pos[num] = old_caterpillar_pos[num - 1]
        scene.center = caterpillar_pos[0]
        turn = 0
        sleep(d_t)

box()

main()
