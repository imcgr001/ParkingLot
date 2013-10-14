"""
author: imcgr001@gmail.com
dataetc.wordpress.com
"""

import random, math, threading, os
from Car import car
from Wait import wait
from multiprocessing import Process, Queue





#simulation does each second between 11 AM - 2  PM



def runner(Total_Spots,base,avg,avg_start,
           start_dev,base_dev=.002,inc_dev=.002):
    """(Total_Spots,base%,totalavg%,base std=.002,increment std=.002"""
    
    random.seed()
    
    #initalize variables
    no_init = 0
    allc = 0
    total = []
    spot_que = []
    wait_que = []
    timer = 0
    incz = 0
    values = []
    wait_time = []
    total_wait = []

    #average and sigma for taking a spot
    wait_mu = 20*60
    wait_sig = 4*60
    
    
    increment = random.gauss((2*(avg-base)),inc_dev)/5400
    base = random.gauss(base,base_dev)
    
    attempt_prob = base

    #print(base) #debug
    
    #Initialize parking lot to values assigned in function call and assign
    #to no_init for analysis
    no_init = int(random.gauss(avg_start,start_dev))
    for i in range(0, no_init):
        spot_que.append(car(random.gauss(wait_mu,wait_sig)))
                   
    while timer <= 10800:

        #assign a value to attempt_prob variable for this iteration
        #attempt_prob = random.gauss(0,1)

        
        if timer <= 5400:  #<= 5400: 
            #increase value mu by increment value until *12:30 PM
            attempt_prob = attempt_prob + increment

    
        else: #elif timer > (peak + peak_width):
            #bring value mu back down to levels started at
            attempt_prob = attempt_prob - increment
            
     
     
        if (attempt_prob > random.uniform(0,1)):
            allc = allc + 1

            #A car wants a spot so if there is room then put it in the lot
            if len(spot_que) < Total_Spots:
                #assign the car a random time before it leaves and add it to lot
                spot_que.append(car(random.gauss(wait_mu,wait_sig)))
                total.append(1)

                #If there is more room and more cars wanting spots
                #get the number and add them to lot
                i = Total_Spots - len(spot_que) 
                for k in range(0,i):

                    #only add them if they are waiting for a spot
                    if len(wait_que) > 0:
                        
                        #grab the amount of time they waited 
                        wait_time.append( wait_que[0].get_time())
                        #remove them from the wait_que
                        wait_que.pop(0)
                        
                        spot_que.append(car(random.gauss(wait_mu,wait_sig)))
                        total.append(1)
                        
            #If no spots available car is now driving around for a spot
            else:
                wait_que.append(wait())
                total_wait.append(1)
       
        #Go through cars currently parked in lot
        for j in spot_que:
            #if timer is above 0, decrement timer
            if j.get_time() > 0:
                j.det_time()

            #if timer == 0 remove car from spot    
            else:
                spot_que.remove(j)

                #Since a car left, if there are cars waiting for a spot
                #add them to the lot
                if len(wait_que) > 0:
                    wait_time.append( wait_que[0].get_time())
                    wait_que.pop(0)
                    spot_que.append(car(random.gauss(wait_mu,wait_sig)))
                    total.append(1)
                    
        #For all the cars now waiting for a spot, incremement their timers            
        for i in wait_que:
            i.inc_time()
        """  
        print("Time: {}".format(timer))
        print("Spots taken: {}".format(len(spot_que)))
        print("Cars waiting: {}".format(len(wait_que)))
        
        if timer == 10800:
            print("Total cars: {}".format(len(total)))
            print("Total waiting: {}".format(len(total_wait)))
            print("Total time spent waiting: {}".format(sum(wait_time)))
            if len(total_wait) > 0:
                print("Average wait time: {} seconds".format(sum(wait_time)/len(total_wait)))
                print("Max wait time: {} seconds.".format(max(wait_time)))
        """        
        timer = timer + 1

    if len(total_wait) > 0:    
        return([len(total),len(total_wait),(sum(wait_time)/len(total_wait)),
                max(wait_time),len(wait_que),allc,no_init])
    else:
        return([len(total),len(total_wait),0, 0,0,allc,no_init])
    
def plist(lis):
    """write data to csv file"""
    
    outf = open("run_analysis_uniform.csv","wt")
    outf.write("Total Cars:,Total Waiting:,Average Wait:,Max Wait:,")
    outf.write("Remaining:,All:,Start:\n")
    for i in lis:
        #print("{0},{1}".format(i[0],i[1]))
        outf.write("{0},{1},{2},{3},{4},{5},{6}\n".format(i[0],i[1],i[2],
                                                  i[3],i[4],i[5],i[6]))
    outf.close()

if __name__=='__main__':

    vals =  []

    for i in range(0,2000):
        print(i)
        vals.append( runner(80,.02,.04,20,4))
        
    #plist(vals)
    print("Done!")


