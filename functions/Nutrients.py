#contains a list of functions for nutrient related informations

import math
from MolarMasses import*

def fNH3(TK,pH):
    '''This function calculates the fraction of NH3 fNH3 in a water sample at given Temperature in K and pH
    according to emerson 1975'''
    pKa=[]
    fNH3=[]
    if len(TK)==len(pH):
        for i in xrange(len (TK)):
            pKa.append(0.09018+2729.92/(TK[i]))
            fNH3.append(1/(math.pow(10,(pKa[i]-pH[i]))+1))
        return(fNH3)
    else:
        print("data arry lenght mismatch in TK and pH")

#Emerson, K., R. C. Russo, R. E. Lund and R. V. Thurston 1975. Aqueous ammonia equilibrium calculations: effect of pH and temperature. J. Fish. Res. Board Can. 32. 2379-2383

def DIN(NH4,NO2,NO3):
    '''This function outputs the DIN concentration requiring NH4, NO2 and NO3 in the same units of molarity/molality'''
    DIN=[]
    if len(NH4)==len(NO2):
        if len(NO2)==len(NO3):
            for i in xrange(len(NO3)):
                DIN.append(NH4[i]+NO2[i]+NO3[i])
            return(DIN)
        else:
            print ("data array length mismatch in NO2 and NO3")
    else:
        print ("data array length mismatch in NH4 and NO2")

