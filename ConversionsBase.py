#Converts prefixes and dimensionless ratios such as ppm to a scientific number

import math

def ppb2sci(ppb):
    ppb2sci=[]
    '''multiplies a given mole fraction in ppb to scientific writing'''
    for i in xrange(len(ppb)):
        ppb2sci.append(ppb[i]*math.pow(10,-9))
    return(ppb2sci)

def ppm2sci(ppm):
    '''converts a given mole fraction in ppm to its scientific writing'''
    ppm2sci=[]
    for i in xrange(len(ppm)):
        ppm2sci.append(ppm[i]*math.pow(10,-6))
    return(ppm2sci)

def mu2sci(mu):
    '''converts prefix micro (mu) to its base unit in scientific writing'''
    mu2sci=[]
    for i in xrange(len(mu)):
        mu2sci.append(mu[i] * math.pow(10, -6))
    return (mu2sci)

def m2sci(m):
    '''converts prefix milli (m) to its base unit in scientific writing'''
    m2sci=[]
    for i in xrange(len(m)):
        m2sci.append(m[i] * math.pow(10, -3))
    return (m2sci)

def n2sci(n):
    '''converts prefix nano (n) to its base unit in scientific writing'''
    n2sci=[]
    for i in xrange(len(m)):
        n2sci.append(m[i] * math.pow(10, -9))
    return (n2sci)


