from datetime import time
class slot():
  def __init__(self,tag, start_time, end_time, description=''):
    self.tag = tag
    self.description = description
    self.interval = [self.to_integer(time.fromisoformat(start_time)),self.to_integer(time.fromisoformat(end_time))]
  def __repr__(self):
    return f"{self.tag}: {self.display_millitary_time()}"

  def to_integer(self,time):
    return time.hour*60+time.minute
#print(to_integer(time.fromisoformat('23:00')))
  
  def display_millitary_time(self):
    interval = []
    for t in self.interval:
      hour = int(t/60)
      minute = round(60*((t/60)-hour))
      interval.append(time(hour,minute).isoformat('minutes'))
    return interval
  