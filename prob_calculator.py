import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for k in kwargs:
      for i in range(kwargs[k]):
        self.contents.append(k)
  
  def draw(self, n):
    i = 0
    result = []
    while self.contents and i < n:
      r = random.randint(0, len(self.contents) - 1)
      result.append(self.contents[r])
      del self.contents[r]
      i = i + 1
    return result


def countExperiment(result, expected_balls):
  for k in expected_balls:
      n = sum(1 for i in result if i == k)
      if n < expected_balls[k]:
        return False
  return True

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  experimentsOK = 0
  for _ in range(num_experiments):
    hatExp = copy.deepcopy(hat)
    result = hatExp.draw(num_balls_drawn)
    if countExperiment(result, expected_balls):
      experimentsOK = experimentsOK + 1
  return experimentsOK / num_experiments