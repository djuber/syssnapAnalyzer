import process

import sys, csv

""" 
'ps a' and 'ps x' display the short options, 'ps' alone skips STAT, and 'ps u' gives the extended version 

These aren't
"""

pscolumns = ['PID', 'TTY', 'TIME', 'CMD']
psxcolumns = ['PID', 'TTY', 'STAT', 'TIME', 'COMMAND']
psucolumns = ['USER', 'PID', '%CPU', '%MEM', 'VSZ', 'RSS', 'TTY', 'STAT', 'START', 'TIME', 'COMMAND']


if __name__ == '__main__':
    """ process stdin: """
    reader = csv.reader(sys.stdin, delimiter=' ')
    columntype = None
    for row in reader:
        while '' in row:
            row.remove('')
        if columntype:
            processDict = {}
            for index, col in enumerate(columntype):
                processDict[col] = row[index]
            """ get command list """
            processDict[col] = [processDict[col]] + row[index+1:]
            print processDict
        else:
            columntype = row




    


