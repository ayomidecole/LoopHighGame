from gameclasses import Engine
from gameclasses import Scene
from random import randint
from sys import exit
from textwrap import dedent

class LoopCity(Engine):
    def __init__(self, scene_map, game_duration=300):
        super().__init__(scene_map)
        self.game_duration = game_duration

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class GameEnd(Scene):
    def enter(self):
        print('You have tried hard to find your way out of this loop. You give up trying to find your way out. You surrendered to the loop')
        exit(1)

class HallwayEnter(Scene):
    def enter(self):
        print(dedent("""
        You walk into school from the front door. You realize it is familiar. 
        This is the big basketball game day. 
        You've been here before, the exact same people streaming through the hallway, 
        the exact same scene.
        You realize that you need to find a way to get out of this loop.

        You join the crowd, you see the side exit door to your right and the cafeteria 
        to your left. You could go through any of these doors to try and figure out 
        your way out. Or choose to follow the crowd down the hallway
        """))

        action = input('What would you do? > ').lower()

        if 'side exit door' in action or 'side door' in action or 'exit' in action or 'exit door' in action or 'door' in action or 'side' in action:
            print(dedent("""
            You rush out of the building through the side exit door
            """))
            return 'side_exit_door'

        elif 'cafeteria' in action:
            print(dedent('''
            You storm into the cafeteria; it is empty.
            A perfect place for you to look for any clues.
            '''))
            return 'cafe'

        else:
            print(dedent("""
            You keep walking down the hallway, you walk past the side exit door to your 
            right and the cafeteria to your left. You keep walking down the crowded 
            hallway streaming towards the gym.
            """))
            return 'hallway_cont'





class SideExitDoor(Scene):

    def enter(self):
        print(dedent('''
        The light hits your face. There is nothing apart from the cars, 
        you look into the cars parked outside the school and there is no clue to why 
        this is happening. You considering going into the hallway or going into the gym.
        The gym is crowded for the game. Hopefully you can find a clue 
        '''))

        action = input('Gym or Hallway? > ').lower()

        if 'gym' in action or 'game' in action:
            print(dedent("""
            You decide to go to the gym, it would be ahrd  for you to figure things out 
            and find the source of this loop due to it being gameday. A situation 
            like this does not give you many choices so you decide to risk it
            """))
            return 'gym'

        if 'hallway' in action or 'hall' in action:
            print(dedent("""
            You decide to go back into the hallway, you think it is better to search the
            less crowded parts of the school for the cause of the loop before going to
            the gym
            """))
            return 'hallway_cont'

class Cafeteria(Scene):
    def enter(self):
        print(dedent('''
        You start searching the cafeteria for signs, 
        It is a large cafeteria so it takes you time to work through the room. No leads.
        You are discouraged, do you give up or go back into the hallway.
        '''))

        action = input('Do you give up? Yes or No? > ').lower()

        if 'yes' in action:
            print(dedent("""
            You decide to keep searching. You decide to head back into the hallway.
            You are determined to find out what's going on
            """))
            return 'hallway_cont'

        else:
            return 'gameend'



class HallwayCont(Scene):

    def enter(self):
        print(dedent('''
        You rejoin the cloud and keep walking down the hallway.
        You run into the Seyi. She is drunk screaming about how excited she is for the
        game.
        You tell her your whole loop situation and she sounds bored. She remarks that 
        this is a science room type of problem. She enthusiastically asks you to join
        her and go to the gym for the game.
        It clicks that there is a physics lab nearby
        '''))

        action = input('You think about what she says, Physics lab or Gym > ').lower()
        if 'physics' in action or 'lab' in action:
            print(dedent("""
            You decide to go to the physics lab. Maybe Drunk Seyi was onto something.
            """))
            return 'physics_lab'

        else:
          print(dedent("""
          You decide to go to the gym. 
          You are determined to find out what's going on"""))
          return 'gym'
          

class Gym(Scene):

    def enter(self):
        print(dedent("""
        You follow Seyi into the crowded gym. You leaver her in a daze.
        You scramble around the gym without a sense of the occasion
        lookig for a potential clue to why this crazy loop is going on.
        """))

        action = input('What do you do next? > ').lower()
        if 'physics' in action or 'lab' in action:
          print(dedent("""
          You remember Seyi talking about the pyshics lab.
          You are sarting to lose hope. This is the last room 
          you have the heart to search
          """))
          return 'physics_lab'
        else:
          return "gameend"

class PhysicsLab(Scene):
    def enter(self):
        print(dedent("""
        How did you not come in here any sooner. You see an unfamiliar machine.
        You notice the time is moving weird. You decide this is it.
        If the machine does not end the loop you give up.
        There is a number pad on the machine and the screen says
        Enter command from 1-10
        """))
    
        number = randint(1,10)
        guess = int(input('Enter a number from 1-10 > '))

        if int(guess) != number:
            print(dedent("""
            'The machine malfunctions. When the countdown goes down
            The loop starts again but the machine does not allow you enter a command
            The loop starts again. You are trapped'
            """))
            return 'gameend'  

        else:
          print(dedent("""
          The machine processes for a bit
          """))
          return 'finished'




class Finished(Scene):

    def enter(self):
        print(dedent("""
        You see on the screen.
        Timeline Reset. Machine off.
        BOOOM! You wake up after the game ends.
        You defeated the loop.
        OR ARE YOU?
        IN ANOTHER LOOP.
        """))
        exit(0)
  
class Map(object):
    scenes = {
        'hallway_enter': HallwayEnter(),
        'side_exit_door': SideExitDoor(),
        'cafe': Cafeteria(),
        'hallway_cont': HallwayCont(),  # Add this line
        'gym': Gym(),
        'gameend' : GameEnd(),
        'physics_lab': PhysicsLab(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('hallway_enter')
a_game = Engine(a_map)
a_game.play()