from random import choice
from enemy_factory import EnemyFactory
from easy_zombie import EasyZombie
from easy_skeleton import EasySkeleton
from easy_goblin import EasyGoblin


class BeginnerFactory(EnemyFactory):
    def create_random_enemy(self):
        name = choice([EasyZombie(), EasySkeleton(), EasyGoblin()])
        return name
