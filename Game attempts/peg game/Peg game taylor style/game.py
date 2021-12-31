import world
from player import Player
from collections import OrderedDict


def play():
    print()
    print()
    print("Peg Game!")
    world.load_tiles()
    player = Player()
    while player.is_alive() and not player.victory:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        room.modify_player(player)
        if player.is_alive() and not player.victory:
            choose_action(room, player)
        elif not player.is_alive():
            print("You've ran out of moves! Theres nothing else to do. ")


def get_available_actions(room, player):
    actions = OrderedDict()
    print("Choose an action: ")
    if world.tile_at(room.x, room.y - 1):
        action_adder(actions, 'n', player.move_north, "Jump Above")
    if world.tile_at(room.x, room.y + 1):
        action_adder(actions, 's', player.move_south, "Jump Below")
    if world.tile_at(room.x + 1, room.y):
        action_adder(actions, 'e', player.move_east, "Jump Right")
    if world.tile_at(room.x - 1, room.y):
        action_adder(actions, 'w', player.move_west, "Jump Left")
    return actions


def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{} : {}".format(hotkey, name))


def choose_action(room, player):
    action = None
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input("Action: ")
        action = available_actions.get(action_input)
        if action:
            action()
        else:
            print("Invalid action!")


play()