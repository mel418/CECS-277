from puppy_state import PuppyState

class StateEat(PuppyState):
    def feed(self, puppy):
        puppy.inc_feeds()
        if puppy.feeds <= 2:
            return '\nThe puppy continues to eat as you add another scoop of kibble to its bowl.'
        else:
            puppy.change_state(StateAsleep())
            puppy.reset()
            return '\nThe puppy continues to eat as you add another scoop of kibble to its bowl. \nThe puppy ate so much it fell asleep!'
        
    
    def play(self, puppy):
        puppy.change_state(StatePlay())
        puppy.reset()
        puppy.inc_plays()
        return '\nThe puppy looks up from its food and chases the ball you threw.'

  
from state_asleep import StateAsleep
from state_play import StatePlay

        
