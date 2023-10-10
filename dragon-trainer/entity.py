import abc

class Entity(abc.ABC):
    '''
    Attributes: _name – entity’s name, _hp – entity’s hit points, _max_hp – entity’s starting hp.
    '''
    def __init__(self, name, max_hp) -> None:
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp

    def take_damage(self, dmg):
        self._hp = max(self._hp - dmg, 0)

    @property
    def name(self):
        return self._name
    
    @property
    def hp(self):
        return self._hp
    
    @abc.abstractmethod
    def basic_attack(self, other):
        pass

    @abc.abstractmethod
    def special_attack(self, other):
        pass

    

    def __str__(self) -> str:
        return f"{self._name}: {self._hp}/{self._max_hp}"
    
    