class routine():
  sos = []
  def __init__(self,name,description=''):
    self.name = name
    self.description = description 
  #sequence of slots
  def __repr__(self):
    return f'{self.name}: {self.description} with {self.sos}'
    
  def mean(self):
    return [((1440-slot.interval[0] + slot.interval[1])/2) if slot.interval[0] > slot.interval[1] else sum(slot.interval)/2 for slot in self.sos]
    
  def create_key(self):
    a = list(zip(self.mean(),self.sos))
    return {s:m for s,m in a}
    
  def sort(self):
    sorted_list = self.quickSort(self.mean())
    meanSlot = self.create_key()
    self.sos = [meanSlot[mean] for mean in sorted_list]

  def delete(self,slot):
    self.sos.remove(slot)

  def quickSort(self,arr):
    less = []
    pivotList = []
    more = []

    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = self.quickSort(less)
        more = self.quickSort(more)
        return less + pivotList + more
      
  def set_start(self,start):
    return self.sos[self.sos.index(start):] + self.sos[:self.sos.index(start)]

  def check_conflict(self):
    #fix last > first
    for num,e in enumerate(self.sos):
      #print(num,len(self.sos))
      if num == 0: 
        p=e
      
      else:
        if (p.interval[1]>e.interval[0]):
          return True
        else:
          p=e
    if self.sos[-1].interval[1]>self.sos[0].interval[0]:
      return True
    
    return False

  def display_interval(self):
    print(tuple(slot.interval for slot in self.sos))

  def append_slots(self,*slots):
    for slot in slots:
      self.sos.append(slot)

  def merge(self):
    for num,e in enumerate(self.sos):
      
      if num == 0: 
        p=e
      else:
        if (p.interval[1]>=e.interval[0] and p.tag==e.tag):
          p.interval[1]=e.interval[1]
          self.sos.remove(e)
        else:
          p=e
    end = self.sos[-1]
    start = self.sos[0]
    
    if end.interval[1]>=start.interval[0] and end.tag == start.tag:
      self.sos[-1].interval[1]=self.sos[0].interval[1]
      self.sos.remove(self.sos[0])
    return False