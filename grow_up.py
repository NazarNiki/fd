from assistant_class import *
from vegatable_class import *
import time
name=input()
position=input()
player=Assistant(name,position)
corn=vegetable('Corn',0,0,0)
tomato=vegetable('Potato',0,0,0)
time=8
end_time=20
while time!=end_time:
    print('Time', str(time)+':00')
    sample = input('Chooce sample:\n1-Corn\n2-Tomato\n3-Potato')
    if sample == '1':
        plant = corn
    elif sample=='2':
        plant == tomato
    else:
        plant == tomato
    action = input('Chooce action:\n1-water\n2-ferti')
    if action=='1':
        player.water(plant)
    elif:
        action=='2'
         
