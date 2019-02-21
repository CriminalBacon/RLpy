import tcod as libtcod

from games_states import GamesStates


def kill_player(player):
    player.char = '%'
    player.color = libtcod.dark_red

    return 'You died!', GamesStates.PLAYER_DEAD


def kill_monster(monster):
    death_message = '{0} is dead!'.format(monster.name.capitalize())

    monster.char = '%'
    monster.color = libtcod.dark_red
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.name = 'remains of ' + monster.name

    return death_message