import numpy as np


class SequentialDownSampler(object):
  def __init__(self, X, Y, dclass=1, ratio=3):
    self.X = X
    self.Y = Y
    self.X_new = []
    self.Y_new = []
    self.counter = 0
    self.dclass = dclass
    self.ratio = ratio
  
  def downsample(self):
    for i, _ in enumerate(self.X):
      if self.Y[i] == self.dclass:
        self.counter += 1
        if self.counter % self.ratio == 0:
          self.X_new.append(self.X[i])
          self.Y_new.append(self.Y[i])
      else:
        self.X_new.append(self.X[i])
        self.Y_new.append(self.Y[i])
    return np.array(self.X_new), np.array(self.Y_new)
