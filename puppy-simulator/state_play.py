from puppy_state import PuppyState

class StatePlay(PuppyState):
    def feed(self, puppy):
        return '\nThe puppy is too busy playing with the ball to eat right now.'

    def play(self, puppy):
        puppy.inc_plays()
        if puppy.plays >= 3:
            puppy.reset()
            puppy.change_state(StateAsleep())
            return '\nYou throw the ball again and the puppy excitedly chases it. \nThe puppy played so much it fell asleep!'
        return 'You throw the ball again and the puppy excitedly chases it.'

from state_asleep import StateAsleep

    
