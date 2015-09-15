import random

class BernoulliArm():
  def __init__(self, p):
    self.p = p
    print("init %0.2f" % p)
  
  def draw(self):
    if random.random() > self.p:
      return 0.0
    else:
      return 1.0
  

