from enemy_factory import EnemyFactory
from goblin import Goblin
from skeleton import Skeleton
from zombie import Zombie
from random import choice

class ExpertFactory(EnemyFactory):
    def create_random_enemy(self):
        enemy = choice([
                            Goblin(),
                            Skeleton(),
                            Zombie(),
                        ])  
        return enemy      
        