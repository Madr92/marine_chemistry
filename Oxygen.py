#this calculates the concentration of oxygen in various other dimensions
from UniversalConstants import*
from Solubilities import*


def conc2massconc(O2):
    '''converts the concentration of O2 in mumol/L to mg/L'''
    mO2=[]
    for i in xrange(len(O2)):
        mO2.append(O2[i]*2*mO/1000)
    return(mO2)

def massconc2conc(mO2):
    '''converts an oxygen concentration in mg/L to mumol/L'''
    O2=[]
    for i in xrange(len(mO2)):
        O2.append(mO2[i]/(2*mO)*1000)
    return(O2)

def massconc2pO2(KO2,mO2):
    '''converts Oxygen concentration in mg/L to partial pressure (mbar). Requires solubility beta termed KO2 here from KO2 function'''
    O2pp=[]
    for i in xrange(len(mO2)):
        O2pp.append((mO2[i]/KO2[i])*Vm0/(2*mO))
    return(O2pp)

def mO2toSat(mO2,KO2,patm):
    '''converts a given oxygen concentration (mg/L) to saturation in per cent. It requires beta from KO2 function termed KO2 here
    and atmospheric pressure (patm in hPa)'''
    sat=[]
    O2eq=[]
    for i in xrange(len(mO2)):
        O2eq.append((KO2[i]/Vm0)*pairO2*patm[i]*2*mO) #equilibrium concentration in mumol/L
        sat.append((mO2[i]/O2eq[i])*100)
    return(sat)
    print("%")
