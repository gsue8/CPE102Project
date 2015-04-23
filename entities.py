import point

class Entity(object):
   def __init__(self, name, imgs):
      self.name = name
      self.imgs = imgs
      self.current_img = 0

   def get_images(self):
      return self.imgs

   def get_image(self):
      return self.imgs[self.current_img]

   def get_name(self):
      return self.name

   def next_image(self):
      self.current_img = (self.current_img + 1) % len(self.imgs)


class Background(Entity):
   def __init__(self, name, imgs):
      super(Background, self).__init__(name, imgs)
      

class Subject(Entity):
   def __init__(self, name, position, imgs):
      super(Subject, self).__init__(name, imgs)
      self.position = position

   def set_position(self, point):
      self.position = point

   def get_position(self):
      return self.position




class Obstacle(Subject):
   def __init__(self, name, position, imgs):
      super(Obstacle, self).__init__(name, position, imgs)

   def entity_string(self):
      return ' '.join(['obstacle', self.name, str(self.position.x),
         str(self.position.y)])


class SubjectActing(Subject):
   def __init__(self, name, position, imgs, rate):
      super(SubjectActing, self).__init__(name, position, imgs)
      self.rate = rate 
      self.pending_actions = []

   def get_rate(self):
      return self.rate

   def remove_pending_action(self, action):
      if hasattr(self, "pending_actions"):
         self.pending_actions.remove(action)

   def add_pending_action(self, action):
      if hasattr(self, "pending_actions"):
         self.pending_actions.append(action)

   def get_pending_actions(self):
      if hasattr(self, "pending_actions"):
         return self.pending_actions
      else:
         return []

   def clear_pending_actions(self):
      if hasattr(self, "pending_actions"):
         self.pending_actions = []


class SubjectMobile(SubjectActing):
   def __init__(self, name, position, imgs, rate, animation_rate):
      super(SubjectMobile, self).__init__(name, position, imgs, rate)
      self.animation_rate = animation_rate

   def get_animation_rate(self):
      return self.animation_rate

   
class SubjectWRD(SubjectActing):
   def __init__(self, name, position, imgs, rate,
      resource_distance=1):
      super(SubjectWRD, self).__init__(name, position, imgs, rate)
      self.resource_distance = resource_distance

   def get_resource_distance(self):
      return self.resource_distance
   
   
class Quake(Subject):
   def __init__(self, name, position, imgs, animation_rate):
      super(Quake, self).__init__(name, position, imgs)
      self.animation_rate = animation_rate
      self.pending_actions = []

   def get_animation_rate(self):
      return self.animation_rate

   def remove_pending_action(self, action):
      if hasattr(self, "pending_actions"):
         self.pending_actions.remove(action)

   def add_pending_action(self, action):
      if hasattr(self, "pending_actions"):
         self.pending_actions.append(action)

   def get_pending_actions(self):
      if hasattr(self, "pending_actions"):
         return self.pending_actions
      else:
         return []

   def clear_pending_actions(self):
      if hasattr(self, "pending_actions"):
         self.pending_actions = []

   

class Miner(SubjectMobile):
   def __init__(self, name, resource_limit, position, rate, imgs,
      animation_rate):
      super(Miner, self).__init__(name, position, imgs, rate,
         animation_rate)
      self.resource_limit = resource_limit

   def set_resource_count(self, n):
      self.resource_count = n

   def get_resource_count(self):
      return self.resource_count

   def get_resource_limit(self):
      return self.resource_limit


class MinerNotFull(Miner):
   def __init__(self, name, resource_limit, position, rate, imgs,
      animation_rate):
      super(MinerNotFull, self).__init__(name, resource_limit, position,
         rate, imgs, animation_rate)
      self.resource_count = 0

   def entity_string(self):
      return ' '.join(['miner', self.get_name, str(self.get_position.x),
         str(self.get_position.y), str(self.get_resource_limit),
         str(self.get_rate), str(self.get_animation_rate)])


class MinerFull(Miner):
   def __init__(self, name, position, rate, imgs,
      animation_rate, resource_limit):
      super(MinerFull, self).__init__(name, position, rate,
         imgs, animation_rate, resource_limit)
      self.resource_count = resource_limit


class Ore(SubjectActing):
   def __init__(self, name, position, imgs, rate=5000):
      super(Ore, self).__init__(name, position, imgs, rate)

   def entity_string(self):
      return ' '.join(['ore', self.name, str(self.position.x),
         str(self.position.y), str(self.rate)])


class Vein(SubjectWRD):
   def __init__(self, name, rate, position, imgs, resource_distance=1):
      super(Vein, self).__init__(name, position, imgs, rate,
         resource_distance=1)

   def entity_string(self):
      return ' '.join(['vein', self.name, str(self.position.x),
         str(self.position.y), str(self.rate),
         str(self.resource_distance)])


class OreBlob(SubjectMobile):
   def __init__(self, name, position, rate, imgs, animation_rate):
      super(OreBlob, self).__init__(name, position, imgs, rate, animation_rate)


class Blacksmith(SubjectWRD):
   def __init__(self, name, position, imgs, resource_limit, rate,
      resource_distance=1):
      super(Blacksmith, self).__init__(name, position, imgs, rate,
      resource_distance=1)
      self.resource_limit = resource_limit
      self.resource_count = 0

   def set_resource_count(self, n):
      self.resource_count = n

   def get_resource_count(self):
      return self.resource_count

   def get_resource_limit(self):
      return self.resource_limit



