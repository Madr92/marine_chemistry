#this routine calculates the transfer coefficients from the u10 given in m/s for various models.
#it therefore requires in-situ Sc
#Other models were taken from Wrobel et al., 2016

#import section
import math

#k Wanninkhof 2014:
def kW14(u10,Sc):
    '''calculates the transfer velocity k in cm/h according to Wanninkhof 2014. Requires wind speed at 10 m height
    u10 (m/s) and in situ Schmidt number Sc'''
    k14=[]
    if len(u10)==len(Sc):
        for i in xrange(len(u10)):
            k14.append(math.pow((660.0/Sc[i]),0.5)*0.251*math.pow(u10[i],2))
        return(k14)
    else:
        print("data arrays don't match up. Please check your input")

#k Nightingale 2000:
def kN00(u10,Sc):
    '''calculates the transfer velocity k in cm/h according to Nightingale et al., 2000. Requires wind speed at 10 m height
    u10 (m/s) and in situ Schmidt number Sc'''
    kN00=[]
    if len(u10)==len(Sc):
        for i in xrange(len(u10)):
            kN00.append(math.pow((660.0/Sc[i]),0.5)*0.212*math.pow(u10[i],2)+0.318*u10[i])
        return(kN00)
    else:
        print("data arrays don't match up. Please check your input")

#k Wanninkhof and Mc Gillis 1999:
def kWMG99(u10,Sc):
    '''calculates the transfer velocity k in cm/h according to Wanninkhof and Mc Gillis, 1999. Requires wind speed at 10 m height
    u10 (m/s) and in situ Schmidt number Sc'''
    kWMG99=[]
    if len(u10)==len(Sc):
        for i in xrange(len(u10)):
            kWMG99.append(math.pow((660.0/Sc[i]),0.5)*0.0283*math.pow(u10[i],3))
        return(kWMG99)
    else:
        print("data arrays don't match up. Please check your input")

#k Ho et al., 2006:
def kHo06(u10,Sc):
    '''calculates the transfer velocity k in cm/h according to Ho et al., 2006. Requires wind speed at 10 m height
    u10 (m/s) and in situ Schmidt number Sc'''
    kHo2006=[]
    if len(u10)==len(Sc):
        for i in xrange(len(u10)):
            kHo2006.append(math.pow((660.0/Sc[i]),0.5)*0.254*math.pow(u10[i],2))
        return(kHo2006)
    else:
        print("data arrays don't match up. Please check your input")

#k Mc Gillis et al., 2001:
def kMcG01(u10,Sc):
    '''calculates the transfer velocity k in cm/h according to Mc Gillis et al. 2001. Requires wind speed at 10 m height
    u10 (m/s) and in situ Schmidt number Sc'''
    kMcG01=[]
    if len(u10)==len(Sc):
        for i in xrange(len(u10)):
            kMcG01.append(math.pow((660.0/Sc[i]),0.5)*(3.3+0.026*math.pow(u10[i],3)))
        return(kMcG01)
    else:
        print("data arrays don't match up. Please check your input")
