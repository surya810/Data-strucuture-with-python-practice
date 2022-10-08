class heap:
  def __init__(self,L):
    self.values = L
    
  def insert_first(self,L,X):
    self.value = X
    nlist = []
    nlist = L.insert(0,X)
    self.new_list = nlist

  def delete_max(self,L):
    max_val = max(L)
    self.myvalue = max(L)
    self.remove = L.remove(max_val)
    

L = [1,2,34,6]
h=heap(L)
h.insert_first(L,0)
h.delete_max(L)
print(h.values)
print(h.value)
print(h.new_list)
print(h.myvalue)
print(h.remove)
