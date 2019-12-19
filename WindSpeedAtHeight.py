#this calculates the windspeed at height x=10 meters if measured at height y in meters

import math
from UniversalConstants import*

def u_10(u,h):
    u10=[]
    K=0.41
    c10=0.0013
    for i in xrange(len(u)):
        u10.append(u[i]*(1+c10**(0.5)/K*math.log(10/h,e)))
    return (u10)
    print("m/s")
    
#this function is based on Crusis, J. and Waninkhof, R., Gas transfer velocities measured at low wind speed over a lake, Limnol. Oceanogr., 48(3), 2003, 1010–1017.

def u2kn(ms):
    ukn=[]
    kn=1.943844
    for i  in xrange(len(ms)):
        ukn.append(ms[i]*kn)
    return(ukn)

def u2ms(ukn):
    ums=[]
    kn=1.943844
    for i  in xrange(len(kn)):
        ums.append(ukn[i]*kn)
    return(ukn)
