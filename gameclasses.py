class Engine(object):
  def __init__(self, scene_map):
      self.scene_map = scene_map

  def play(self):
      current_scene = self.scene_map.opening_scene()
      last_scene = self.scene_map.next_scene('finished')

      while current_scene != last_scene:
          next_scene_name = current_scene.enter()
          current_scene = self.scene_map.next_scene(next_scene_name)

      current_scene.enter()



class Scene(object): #This is the base class that will have common things that all scenes do

  def enter(self):
      print('This scene is not yet configured.')
      print("Subclass it and implement eneter().")
      exit(1)

class Map(object):

  def __init__(self, start_scene):
      self.start_scene = start_scene

  def next_scene(self, scene_name):
      val = Map.scenes.get(scene_name)
      return val

  def opening_scene(self):
      return self.next_scene(self.start_scene)