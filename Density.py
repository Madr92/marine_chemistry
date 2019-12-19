#this function calculates the density of brackish seawater according to Millero and Huang 2009

#import section
import math


def rho0(T):
    '''This function calculates the density of fresh water of salinity = 0 in kg m-3'''
    rho0=[]
    for i in xrange(len(T)):
        rho0.append((1-(T[i]+288.9414)/(508929*(T[i]+68.12963))*(T[i]-3.9863)**2)*1000)
    return(rho0)

def rho(T,Sal,rho0):
    '''This function calculates the density rho in kg m-3 for brackish sea water for given T in C and Sal in psu.
    It requires rho0 the density of fresh water at same T. Get rho0 from the function rho0()'''
    A=[]
    B=[]
    rho=[]
    a0=0.8174451
    a1=-0.00363877
    a2=0.00006480811
    a3=-0.0000007312404
    a4=0.000000005330431
    a5=-0.00000000001657628
    b0=0.005481436
    b1=0.00003486075
    b2=-0.000003049727
    c0=0.000536196
    if len(T)==len(Sal):
        if len(T)==len(rho0):
            for i in xrange(len(rho0)):
                A.append(a0+a1*T[i]+a2*T[i]**2+a3*T[i]**3+a4*T[i]**4+a5*T[i]**5)
                B.append(b0+b1*T[i]+b2*T[i]**2)
                rho.append(A[i]*Sal[i]+B[i]*Sal[i]**(1.5)+c0*Sal[i]+rho0[i])
            return(rho)
        else:
            print("data array length mismatch for T and rho")
    else:
        print("data array length mismatch for T and Sal")

#equations and parameters were taken from: 
#F. J. Millero and F. Huang, The density of seawater as a function of salinity (5 to 70 g kg −1 ) and temperature (273.15 to 363.15 K),Ocean Sci., 5, 91–100, 2009.
