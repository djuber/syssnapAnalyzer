"""
from the horses mouth : man 1 ps : 

PROCESS STATE CODES
       Here are the different values that the s, stat and state output specifiers (header "STAT" or "S") will display to describe the
       state of a process:

               D    uninterruptible sleep (usually IO)
               R    running or runnable (on run queue)
               S    interruptible sleep (waiting for an event to complete)
               T    stopped, either by a job control signal or because it is being traced
               W    paging (not valid since the 2.6.xx kernel)
               X    dead (should never be seen)
               Z    defunct ("zombie") process, terminated but not reaped by its parent

       For BSD formats and when the stat keyword is used, additional characters may be displayed:

               <    high-priority (not nice to other users)
               N    low-priority (nice to other users)
               L    has pages locked into memory (for real-time and custom IO)
               s    is a session leader
               l    is multi-threaded (using CLONE_THREAD, like NPTL pthreads do)
               +    is in the foreground process group

"""

states = {'D' : "uninterruptible sleep (usually IO)",
          'R' : "running or runnable (on run queue)",
          'S' : "interruptible sleep (waiting for an event to complete)",
          'T' : "stopped, either by a job control signal or because it is being traced",
          'W' : "paging (not valid since the 2.6.xx kernel)",
          'X' : "dead (should never be seen)",
          'Z' : "defunct ('zombie') process, terminated but not reaped by its parent"}

secondary_states = {
    
    '<' :   "high-priority (not nice to other users)",
    'N' :   "low-priority (nice to other users)",
    'L' :    "has pages locked into memory (for real-time and custom IO)",
    's' :   "is a session leader",
    'l' :    "is multi-threaded (using CLONE_THREAD, like NPTL pthreads do)",
    '+' :    "is in the foreground process group"
}

class StateCode(object):
    """ handle the state code in the ps output """
    def __init__(self, state_string):
        self.string = state_string
        self.state = states[state_string[0]]
        self.secondary = []
        if len(state_string) > 1:
            for ss in state_string[1:]:
                self.secondary.append(secondary_states[ss])
    