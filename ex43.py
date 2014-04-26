# code file for ex43
# Basic Object Oriented Analysis And Design 

## top dpwn -> abstract refine
## Game: Gothons From Plantet Percal #25

##############   tree of classes   #######################
# 
# * Map
#   - next_scene
#   - opening_scene
# * Engine
#   - play
# * Scene
#   - enter
#   * Death    
#   * Central Corridor
#   * Laser Weapon Armory
#   * The Bridge
#   * Escape Pod
#
#########################################################

## basic import 
from sys import exit
from random import randint

## define class trees
class Map(object):
    def __init__(self, start_scene):
        pass
    def next_scene(self, scene_name):
        pass
    def opening_scene(self):
        pass


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
    def play(self):
        current_scene = self.scene_map.opening_scene()
        
        while True:
            print "\n---------------------------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        
        
class Scene(object):
    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)
        pass
        
class Death(Scene): 
    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she was smarter.",
        "Such a luser.", 
        "I have a small puppy that is better at this."]
    def enter(self):
        print Death.quips[randict(0, len(self.quips)-1)]
        exit(1)
        
class CentralCorridor(Scene):
    def enter(self):
        pass

class Laser_Weapon_Armory(Scene):
    def enter(self):
        pass
    
class The_Bridge(Scene):
    def enter(self):
        pass
        
class Escape_Pod(Scene):
    def enter(self):
        pass   

## test info 
#a_map = Map('central_corridor')             
#a_game = Engine(a_map)
#a_game.play()

# 136





