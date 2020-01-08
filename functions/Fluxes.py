#this calculates the fluxes of each trace gas in mg m-2 h-1 for CO2 and mug m-2 h-1 for N2O and CH4
#it requires at least one specific k and the concentration gradient

#import section
import math

def FCO2(k,KCO2,xCO2,xCO2atm,patm):
    '''outputs the flux of CO2 in mg m-2 h-1, requires k (cm/h), atmospheric partial pressure of CO2 (xCO2atm) in ppm,
    mole fraction of CO2 (xCO2) in ppm in water, atmospheric pressure (patm) in atm and solubility (KCO2) in moles/(L atm).'''
    FCO2=[]
    if len(k)==len(KCO2):
        if len(KCO2)==len(xCO2):
            if len(xCO2)==len(patm):
                for i in xrange(len(xCO2)):
                    FCO2.append(k[i]*KCO2[i]*(xCO2[i]-xCO2atm)*patm[i]*4.4*10**(-4))
                    #conversion factors *44 to get from mol to g
                    #/100 to get from cm h-1 to m h-1
                    #/1000 to get from L to m-3
                return(FCO2)

            else:
                print("data array length mismatch in xCO2 and patm")
        else:
            print("data array length mismatch in KCO2 and xCO2")
    else:
        print("data array lenght mismatch in k and KCO2")



def FCH4(k,KCH4,xCH4,xCH4atm,patm):
    '''outputs the flux of CH4 in mug m-2 h-1, requires k (cm/h), atmospheric partial pressure of CH4 (xCH4atm) in ppb,
    mole fraction of CH4 (xCH4) in ppb in water, atmospheric pressure (patm) in atm and solubility (KCH4) in moles/(L atm).'''
    FCH4=[]
    if len(k)==len(KCH4):
        if len(KCH4)==len(xCH4):
            if len(xCH4)==len(patm):
                for i in xrange(len(xCH4)):
                    FCH4.append(k[i]*KCH4[i]*(xCH4[i]-xCH4atm)*patm[i]*1.6*10**(-4))
                    #conversion factors *16 to get from mol to g
                    #/100 to get from cm h-1 to m h-1
                    #/1000 to get from L to m-3
                return(FCH4)

            else:
                print("data array length mismatch in xCH4 and patm")
        else:
            print("data array length mismatch in KCH4 and xCH4")
    else:
        print("data array lenght mismatch in k and KCH4")



def FN2O(k,KN2O,xN2O,xN2Oatm,patm):
    '''outputs the flux of N2O in mug m-2 h-1, requires k (cm/h), atmospheric partial pressure of N2O (xatm) in ppm,
    mole fraction of N2O (xN2O) in water in ppb, atmospheric pressure (patm) in atm and solubility (KN2O) in moles/(L atm).'''
    FN2O=[]
    if len(k)==len(KN2O):
        if len(KN2O)==len(xN2O):
            if len(xN2O)==len(patm):
                for i in xrange(len(xN2O)):
                    FN2O.append(k[i]*KN2O[i]*(xN2O[i]-xN2Oatm)*patm[i]*4.4*10**(-4))
                    #conversion factors *44 to get from mol to g
                    #/100 to get from cm h-1 to m h-1
                    #/1000 to get from L to m-3
                return(FN2O)

            else:
                print("data array length mismatch in xN2O and patm")
        else:
            print("data array length mismatch in KN2O and xN2O")
    else:
        print("data array lenght mismatch in k and KN2O")
