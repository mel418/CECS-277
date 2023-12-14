from puppy_state import PuppyState

class StateAsleep(PuppyState):
    def feed(self, puppy):
        puppy.change_state(StateEat())
        puppy.inc_feeds()
        return '\nThe puppy wakes up and comes running to eat.'
    
    def play(self, puppy):
        return '\nThe puppy is asleep. It doesn\'t want to play right now.'

from state_eat import StateEat
