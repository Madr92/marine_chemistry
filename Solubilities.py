#this calculates the solubility K for the gases CO2 and N2O and the bunsen coefficient beta for CH4

#import
import math
from UniversalConstants import*


def KCO2(TK,Sal):
    A1 = -58.0931
    A2 = 90.5069
    A3 = 22.294
    B1 = 0.027766
    B2 = -0.025888
    B3 = 0.0050578
    LNKCO2 = []
    KCO2 = []
    if len(TK)==len(Sal):
        for i in xrange(len(TK)):
            LNKCO2.append(A1+A2*(100.0/TK[i])+A3*math.log((TK[i]/100.0),e)+Sal[i]*(B1+B2*(TK[i]/100)+B3*(TK[i]/100.0)**2))
            KCO2.append(math.pow(e,LNKCO2[i]))
    else:
        print("your data arrays do not match up, check your data!")
    return(KCO2)
    print("moles/(L atm)")

#R.F. WEISS, CARBONDIOXIDE IN WATER AND SEAWATER: THE SOLUBILITY OF A NON-IDEAL GAS, Marine Chemistry, 2 (1974) 203-215.

def KN2O(TK,Sal):
    A1 = -62.7062
    A2 = 97.3066
    A3 = 24.1406
    B1 = -0.05842
    B2 = 0.033193
    B3 = -0.0051313
    LNKN2O = []
    KN2O = []
    if len(TK)==len(Sal):
        for i in xrange(len(TK)):
            LNKN2O.append(A1+A2*(100.0/TK[i])+A3*math.log((TK[i]/100.0),e)+Sal[i]*(B1+B2*(TK[i]/100.0)+B3*(TK[i]/100.0)**2))
            KN2O.append(math.pow(e,LNKN2O[i]))
    else:
        print("your data arrays do not match up, check your data!")
    return(KN2O)
    print("moles/(L atm)")

#R. F. WEISS and B. A. PRICE, NITROUS OXIDE SOLUBILITY IN WATER AND SEAWATER, Marine Chemistry, 8 (1980) 347-359.

def KCH4(TK,Sal):
    A1 = -68.8862
    A2 = 101.4956
    A3 = 28.7314
    B1 = -0.076146
    B2 = 0.04397
    B3 = -0.0068672
    LNKCH4 = []
    KCH4 = []
    if len(TK)==len(Sal):
        for i in xrange(len(TK)):
            LNKCH4.append(A1+A2*(100.0/TK[i])+A3*math.log((TK[i]/100.0),e)+Sal[i]*(B1+B2*(TK[i]/100.0)+B3*(TK[i]/100.0)**2))
            KCH4.append(math.pow(e,LNKCH4[i])/Vm0)
    else:
        print("your data arrays do not match up, check your data!")
    return(KCH4)
    print("moles/(L atm)")

#Wiesenburg, D. A. and Gulnasso, N. L., Equilibrium Solubilities of Methane, Carbon monoxide, and hydrogen in water and sea water, Journal of Chemical Engineering, 24,4,1979.

def KO2(TK,Sal):
    A1O2 = -58.3877
    A2O2 = 85.8079
    A3O2 = 23.8439
    B1O2 = -0.034892
    B2O2 = 0.015568
    B3O2 = -0.0019387
    lnbeta=[]
    beta=[]
    O2pp=[]
    if len(TK)==len(Sal):
        for i in xrange(len(TK)):
            lnbeta.append(A1O2 + A2O2 * (100 / TK[i]) + A3O2 * math.log((TK[i] / 100)) + Sal[i] * (
                        B1O2 + B2O2 * (TK[i] / 100) + B3O2 * (TK[i] / 100)**2))
            beta.append(math.pow(e, lnbeta[i]))
    return(beta)
    print("returned beta")

#Weiss, R.F., The solubility of nitrogen, oxygen and argon in water and seawater, Deep-Sea Research,17,721-735,1970.
