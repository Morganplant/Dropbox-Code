import pprint
import random
import json
import sys

from Objects_2 import Obj, Room

filename = 'test'
save_file = filename + "_SAVE.json"
filename = filename + ".json"


def not_valid(array, user_opt):
    while not user_opt in array:
        print("'%s' Not a Valid Option"%(user_opt))
        user_opt = str(input('\n:'))
    return user_opt

def save(overwrite_data):
    with open(save_file, 'w') as fh:
        json.dump(overwrite_data, fh, indent=4, sort_keys=True)



def Enter_Room(Story_data, RoomID):
    print()
    print("Now Entering Room:", RoomID)
    room = Room(Room_data[RoomID])

    print('\n', room.Description, '\n')

    if 'Items' in room.__dict__:
        for item_i in room.Items:
                item = Obj(item_i)
                if item.used == 1:
                    room.Items.remove(item_i)
        if len(room.Items) != 0:
            print("\n%s) xp: %s"%(Player.name,Player.xp))
            opt_arr = []
            while len(room.Items) != 0:
                for item_index in range(len(room.Items)):
                    print("%s) %s" % (item_index+1, room.Items[item_index]["Attributes"]["name"]))
                    opt_arr.append(str(item_index+1))
                print('Q) None')
                opt_arr.append('Q')
                user_opt_i = input(":")
                user_opt_i = not_valid(opt_arr, user_opt_i)
                if user_opt_i == 'Q':
                    break
                item = Obj(room.Items[int(user_opt_i)-1])
                popped = room.Items.pop(int(user_opt_i)-1)
                print(room.Items)
                print(popped)
                opt_arr = []
                for action_index in range(len(item.actions)):
                    print("%s) %s" % (action_index+1, item.actions[action_index][0]))
                    opt_arr.append(str(action_index+1))
                user_opt = input(":")
                user_opt = not_valid(opt_arr, user_opt)

                if  (getattr(Player, 'xp') + item.actions[0][1]["Attributes"]['xp']) < 0:
                    for attr in item.actions[0][1]["Attributes"]:
                        before = getattr(Player, attr)
                        setattr(Player, attr, (getattr(Player, attr) + item.actions[0][1]["Attributes"][attr]))
                        print("your '%s' was '%s' and is now '%s'"%(attr, before, getattr(Player, attr)))
                    setattr(item, 'used', 1)
                    Story_data["Rooms"][RoomID]["Items"][int(user_opt)-1]["Attributes"] = item.__dict__
                    save(Story_data)
                print("I can't waste my time on you if you aren't spending anything")
    if 'NPCs' in room.__dict__:
        for npc in room.NPCs:
            try:
                NPc = Obj(npc)
                print(NPc.description)
                opt_arr = []
                for question_index in range(len(NPc.questions)):
                    print("%s) %s"%(question_index+1, NPc.questions[question_index][0]))
                    opt_arr.append(str(question_index+1))
                print("%s) None"%(question_index+2))
                opt_arr.append(str(question_index+2))

                user_opt = input('\n:')
                user_opt = not_valid(opt_arr, user_opt)

                print("%s) %s"%(Player.name, NPc.questions[int(user_opt)-1][0]))
                print("%s) %s"%(NPc.name, NPc.questions[int(user_opt)-1][1]))
            
            except IndexError:
                pass

    if 'Enemies' in room.__dict__:
        for enemies in room.Enemies:
            enemy = Obj(enemies)
            print(enemy.name)
    
    if 'Exits' in room.__dict__:
        opt_arr = []
        for exit_index in range(len(room.Exits)):
            print("%s) %s"%(exit_index+1, room.Exits[exit_index][0]))
            opt_arr.append(str(exit_index+1))

        user_opt = input('\n:')
        not_valid(opt_arr, user_opt)
        print(str(room.Exits[int(user_opt)-1][1]))
        Enter_Room(Story_data, str(room.Exits[int(user_opt)-1][1]))



try:
    with open(save_file, 'r') as fh:
        Story_data = json.load(fh)
except FileNotFoundError:
    with open(filename,'r') as fh:
        Story_data = json.load(fh)
    with open(save_file, 'w') as fh:
        json.dump(Story_data, fh, indent=4, sort_keys=True)
    # setattr(Player, 'name', input('Enter your name: '))

Room_data = Story_data["Rooms"]
Player_data = Story_data['Player']
Player = Obj(Player_data)
print(Player.__dict__)

Enter_Room(Story_data, '5')






