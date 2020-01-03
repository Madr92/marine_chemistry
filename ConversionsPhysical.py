#this converts selected units of physical parameters such as Temperature, time, Area and pressure into other units.
from UniversalConstants import*

def hPa2atm(p):
    '''converts a given pressure in hPa to atm'''
    patm=[]
    for i in xrange(len(p)):
      patm.append(p[i]*hPa2atmp)
    return(patm)

def atm2hPa(p):
    '''converts a given pressure in atm to hPa'''
    phPa=[]
    for i in xrange(len(p)):
      phPa.append(p[i]/hPa2atmp)
    return(phPa)

def T2K(T):
    '''Calculates a given temperature T in C to absolute Temperature (Kelvin Scale)'''
    TinK=[]
    for i in xrange(len(T)):
        TinK.append(T[i]+TK)
    return(TinK)

def K2T(T):
    '''calculates a given absolute Temperature in K to temperature on Celsius scale'''
    KinC=[]
    for i in xrange(len(T)):
        KinC.append(T(i)-TK)
    return(KinC)

def bar2atm(pbar):
    '''converts a given pressure in bar to atm'''
    patm=[]
    for i in xrange(len(pbar)):
        patm.append(pbar*bar2atmp)
    return(patm)

def atm2bar(patm):
    '''converts a given pressure in atm to bar'''
    pbar=[]
    for i in xrange(len(patm)):
        pbar.append(patm/bar2atmp)
    return(patm)

