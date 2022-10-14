class Array_Seq:
  def __init__(self):       # O(1)
    self.A = []
    self.size = 0
  
  
  def __len__(self):        # O(1)
    return self.size
  
  
  def __iter__(self):       # O(n) iter_seq
    yield from self.A
    
    
  def build(self, X):
    self.A = [a for a in X]     # pretend this builds a static array
    self.size = len(size.A)
    
    
  def get_at(self, i):      # O(1)
    return self.A[i]
  
  
  def set_at(self, i, x):   # O(1)
    self.A[i] = x
    
    
  def _copy_forward(self, i, n, A, j):
    ...
    
  
  def _copy_backward(self, i, n, A, j):
    ...
    
    
  def insert_at(self, i, x):
    ...
    
    
  def delete_at(self, i):
    ...
    
  
  def insert_first(self, x):
    self.insert_at(0, x)
    
    
  def delete_first(self):
    return self.delete_at(0)
    
    
  def insert_last(self, x):
    self.insert_at(len(self), x)
    
    
  def delete_last(self):
    return self.delete_at(len(self) - 1)
