#this routine calculates the Schmidt-numbers for the trace gases CO2, CH4 and N2O for a given Temperature T in C
#and the salinity Sal in psu
#coefficients A0-E0 and A35 to E35 are derived from Waninkhof 2014

def ScCO2(T,Sal):
    A0=1923.6
    A35=2116.8
    B0=-125.06
    B35=-136.25
    C0=4.3773
    C35=4.7353
    D0=-0.085681
    D35=-0.092307
    E0=0.00070284
    E35=0.0007555
    Sc0CO2=[]
    Sc35CO2=[]
    ScCO2=[]
    if len(T)==len(Sal):
        for i in xrange(len(T)):
            Sc0CO2.append(A0+B0*T[i]+C0*T[i]**2+D0*T[i]**3+E0*T[i]**4)
            Sc35CO2.append(A35+B35*T[i]+C35*T[i]**2+D35*T[i]**3+E35*T[i]**4)
            ScCO2.append(Sc0CO2[i]+((Sc35CO2[i]-Sc0CO2[i])/35)*Sal[i])
    else:
        print("Array fields do not match up in length, check your data.")
    return (ScCO2)

def ScCH4(T,Sal):
    A0=1909.4
    A35=2101.2
    B0=-120.78
    B35=-131.54
    C0=4.1555
    C35= 4.4931
    D0=-0.080578
    D35= -0.08676
    E0=0.00065777
    E35=0.00070663
    Sc0CH4=[]
    Sc35CH4=[]
    ScCH4=[]
    if len(T)==len(Sal):
        for i in xrange(len(T)):
            Sc0CH4.append(A0+B0*T[i]+C0*T[i]**2+D0*T[i]**3+E0*T[i]**4)
            Sc35CH4.append(A35+B35*T[i]+C35*T[i]**2+D35*T[i]**3+E35*T[i]**4)
            ScCH4.append(Sc0CH4[i]+((Sc35CH4[i]-Sc0CH4[i])/35)*Sal[i])
    else:
        print("Array fields do not match up in length, check your data.")
    return (ScCH4)

def ScN2O(T,Sal):
    A0= 2141.2
    A35=2356.2
    B0=-152.56
    B35=-166.38
    C0=5.8963
    C35=6.3952
    D0=-0.12411
    D35= -0.13422
    E0=0.0010655
    E35=0.0011506
    Sc0N2O=[]
    Sc35N2O=[]
    ScN2O=[]
    if len(T)==len(Sal):
        for i in xrange(len(T)):
            Sc0N2O.append(A0+B0*T[i]+C0*T[i]**2+D0*T[i]**3+E0*T[i]**4)
            Sc35N2O.append(A35+B35*T[i]+C35*T[i]**2+D35*T[i]**3+E35*T[i]**4)
            ScN2O.append(Sc0N2O[i]+((Sc35N2O[i]-Sc0N2O[i])/35)*Sal[i])
    else:
        print("Array fields do not match up in length, check your data.")
    return (ScN2O)
    
    #Waninkhof, R., Relationship between wind speed and gas exchange over the ocean revisited,Limnol. Oceanogr.: Methods 12, 2014, 351–362.
