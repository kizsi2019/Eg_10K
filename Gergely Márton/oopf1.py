class Negyzet:
  def __init__(self, oldalhossz):
    self.oldalhossz = oldalhossz
    
  def kerulet(self):
    return 4 * self.oldalhossz
    
  def terulet(self):
    return self.oldalhossz ** 2
    
s = Negyzet(5)
print(s.kerulet()) 
print(s.terulet()) 
