# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 19:59:51 2022

@author: aidut

Generate a dungeon room with random properties (size, quality, traps/effects, monsters)
"""

from random import randint

import csv

# Lists of properties are kept in local csv files
# Read these files to get the lists from which random elements are chosen

with open(r'C:/Users/aidut/projects/dungeon_generator/room_property_files/room_quality.txt') \
as room_quality_file:
    room_quality_list = []
    for line in room_quality_file:
        room_quality_list.append(line.strip())

with open(r'C:/Users/aidut/projects/dungeon_generator/room_property_files/room_type.txt') \
as room_type_file:
    room_type_list = []
    for line in room_type_file:
        room_type_list.append(line.strip())
        
with open(r'C:/Users/aidut/projects/dungeon_generator/room_property_files/danger.txt') \
as danger_file:
    effect_list = []
    for line in danger_file:
        effect_list.append(line.strip())
       
room_size_list = ['tiny','small','medium-sized','large','huge']

harm_level_list = ['trivial', 'inconvenient', 'dangerous', 'deadly']

# Each 'get' function determines a random index value,
# then chooses the element from the list with that value
# generate_room determines the size and kind of room
# lets_get_dangerous determines the effects the room is under
        
def get_size():
    size_index = randint(0,(len(room_size_list)-1))
    size = room_size_list[size_index]
    return size
    
def get_quality():
    quality_index = randint(0,(len(room_quality_list)-1))
    quality = room_quality_list[quality_index]
    return quality

def get_type():
    type_index = randint(0,(len(room_type_list)-1))
    room_type = room_type_list[type_index]
    return room_type

def generate_room(size,quality,room_type):
    size = room_size
    quality = room_quality
    room_type = room_type
    result = "A {}, {} {}".format(size,quality,room_type)
    return result
    
def get_harm_level():
    harm_index = randint(0,(len(harm_level_list)-1))
    harm = harm_level_list[harm_index]
    return harm

def get_effect():
    effect_index = randint(0,(len(effect_list)-1))
    effect = effect_list[effect_index]
    return effect

def lets_get_dangerous(harm,effect):
    if 'trap' in effect:
        danger = effect.format(harm)
        return danger
    else:
        return effect
    
room_size = get_size()
room_quality = get_quality()
room_type = get_type()
    
room = generate_room(room_size,room_quality,room_type)

harm = get_harm_level()
effect = get_effect()

effect = lets_get_dangerous(harm,effect)

print(room + ' ' + effect)

