#this calculates the Molar Masses of a compound from its sum formula. Currently only organic compounds
#with C,H,N,P,O and S are supported

from UniversalConstants import*

def Morg(C,H,O,N,P,S):
    '''defines molar mass for a compound with given sum formula. E.g. Morg(6,12,6,0,0,0,0) outputs molar mass
    for C6H12O6'''
    Morg=mC*C+mH*H+mO*O+mN*N+mP*P+mS*S
    return(Morg)

def X_C (Morg):
    '''This function calculates the conversion factor to express a mass of C in a compound. E.g. to convert CO2 to CO2-C'''
    X_C=(Morg[1]*mC/Morg[0])
    return(X_C)

def X_N (Morg):
    '''This function calculates the conversion factor to express a mass of C in a compound. E.g. to convert CO2 to CO2-C'''
    X_N=(Morg[4]*mN/Morg[0])
    return(X_N)

def m2n (m,Morg):
    m2n=[]
    '''converts a given mass of substance in g to the number of moles of that substance'''
    m2n.append(m/Morg[0])
    return(m2n)

def n2m (n,Morg):
    n2m=[]
    '''converts a given number of moles of a substance to the weight of the substance in g'''
    n2m.append(n[0] * Morg[0])
    return (n2m)
