class Matrix:
  def __init__(self, data):
    self.data = data
  
  def __repr__(self):
    return f"Matrix{self.data}"
  
  def __add__(self, other):
    assert (len(self.data) == len(other.data)) & (len(self.data[0]) == len(other.data[0]))
    tmp = [0] * len(self.data)       
    for i in range(len(self.data)):
      tmp[i] = [0] * len(self.data[0])
    for i in range(len(self.data)):
      for j in range(len(self.data[0])):
        tmp[i][j] = self.data[i][j] + other.data[i][j]
    return Matrix(tmp)

  def __sub__(self, other):
    assert (len(self.data) == len(other.data)) & (len(self.data[0]) == len(other.data[0]))
    tmp = [0] * len(self.data)       
    for i in range(len(self.data)):
      tmp[i] = [0] * len(self.data[0])
    for i in range(len(self.data)):
      for j in range(len(self.data[0])):
        tmp[i][j] = self.data[i][j] - other.data[i][j]
    return Matrix(tmp)

  def __mul__(self, other):
    if type(other) == Matrix:
      assert len(self.data[0]) == len(other.data)
      tmp = [0] * len(self.data)       
      for i in range(len(self.data)):
        tmp[i] = [0] * len(other.data[0])
      for i in range(len(self.data)):
        for j in range(len(other.data[0])):
          for k in range(len(self.data[0])):
            tmp[i][j] += self.data[i][k] * other.data[k][j]
      return Matrix(tmp)

    else:
      tmp = [0] * len(self.data)       
      for i in range(len(self.data)):
        tmp[i] = [0] * len(self.data[0])
      for i in range(len(self.data)):
        for j in range(len(self.data[0])):
          tmp[i][j] = self.data[i][j] * other
      return Matrix(tmp)

  def __rmul__(self, other):
    tmp = [0] * len(self.data)       
    for i in range(len(self.data)):
      tmp[i] = [0] * len(self.data[0])
    
    for i in range(len(self.data)):
      for j in range(len(self.data[0])):
        tmp[i][j] = self.data[i][j] * other
    return Matrix(tmp)