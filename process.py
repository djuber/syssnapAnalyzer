class ProcessLine(object):
    """ hold information from `ps x` about a process 
    contains : 
    process id (pid)
    tty id
    Process State
    Clock Time
    Command (base command + options)
    """

    def process_psx_line(self, line):
        """check if this line is the output from ps x"""
        content  = line.strip().split(" ")
        # strip out blanks
        while '' in content:
            content.remove('')
        if len(content) < 5: # must be at least this long
            return (None, None, None, None, None)
        else:
            pid, tty, state, clock= content[:4]
            command = content[4:]
            if ':' in clock: # clock will have a colon
                return (pid,tty,state,clock,command)
            else: # or it's not a ps line
                return (None, None, None, None, None)
                

    def __init__(self, psx):
        self.pid, self.tty, self.state, self.clock, self.command =  self.process_psx_line(psx)
        if self.command:
            self.base_command = self.command[0]
            self.command_options = self.command[1:]
        else:
            self.base_command = None
            self.command_options = None

    def is_empty(self):
        return self.pid == None
    def is_valid(self):
        return not self.is_empty()
        