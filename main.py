#import random
from routine import routine
from slot import slot
from tag import tag

# class app():  
routines = []
#   tags = [tag('school'),tag('eating'),tag('sleeping'),tag('housework')]

def create_routine():
  temp = routines
  temp.append(routine(input(),input()))
  
def create_tag():
  tags.append(tag(input(),input()))
  
def create_slot():
  tag = choose_option(tags)
  start_time = input('start time:')
  end_time = input('end time:')
  return slot(tag, start_time, end_time)
  
def choose_option(list):
  #strlist = [for option in list]
  for num,option in enumerate(list):
    print(num,option)
  answer = input()
  while int(answer) not in range(num+1):
    print('please try again')
    answer = input()
  return list[int(answer)]
    
    







#schedule = app()
#schedule.choose_option(schedule.tags)


tags = [tag('school'),tag('eating'),tag('sleeping'),tag('housework'),tag('homework'),tag('break'),tag('reading'),tag('shower'),tag('project')]

default = routine('default','default routine')


# response = 'y'
# while response == 'y':
#   default.append_slots(create_slot())
#   response = input("Would you like to create another?: ")
  



#default.sort()
#print(default.check_conflict())
#default.merge()
print(default.sos)
