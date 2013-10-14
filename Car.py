"""
author: imcgr001@gmail.com
dataetc.wordpress.com
"""


class car:

    '''maintains the car's wait time'''

    def __init__(self, timer):

        self.timer = timer

        #debug:
        #print("car wait time: {}".format(timer))
        
    def det_time(self):

        self.timer = self.timer - 1
        
    def get_time(self):

        return self.timer
