class Car(object):
  def __init__(self, name='General', model='GM', cartype=None, speed=0):
    self.name = name
    self.model = model
    self.cartype = cartype
    self.speed = speed


    if self.name in ['Porshe', 'Koenigsegg']:
      self.num_of_doors = 2
    else:
      self.num_of_doors = 4

    if self.cartype == 'trailer':
      self.num_of_wheels = 8
    else:
      self.num_of_wheels = 4


  def is_saloon(self):
    if self.cartype is not 'trailer':
      self.cartype == 'saloon'
      return True
    return False

  def drive(self, speed):
    if speed == 3:
      self.speed = 1000
    elif speed == 7:
      self.speed = 77
    return self




