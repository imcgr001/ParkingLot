"""
author: imcgr001@gmail.com
dataetc.wordpress.com
"""


class wait:

    '''to tally the total wait time not in a spot'''

    def __init__(self):

        self.timer = 0

        #debug:
        #print("car wait time: {}".format(timer))

    def inc_time(self):

        self.timer = self.timer + 1

    def get_time(self):

        return self.timer
