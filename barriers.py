  
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 20:31:42 2019
@author: patemi
"""

#from QuantLib import *

import QuantLib as ql

import matplotlib.pyplot as plt
import numpy as np

S=list(np.arange(107,109.99,0.01))

S_up=[]

delta_shift_up=0.01
delta_shift_down=-0.01

S_up=[s*delta_shift_up for s in S]

barrier = 110.0
barrierType = ql.Barrier.UpOut
optionType = ql.Option.Call
rebate = 0.0

strike = 105
rf =5e-2
sigma = 20e-2
maturity = 0.25
divYield = 0.0


V=[]
delta=[]

for s in S:
            
    underlying=s    
        
#    Grids = (5 , 10 , 25 , 50 , 100 , 1000 , 5000)
#    maxG = Grids [ -1]
#    
    today = ql.Settings.instance().evaluationDate
    maturity_date = today + int ( maturity * 12)
    process = ql.BlackScholesMertonProcess(ql.QuoteHandle(ql.SimpleQuote(underlying)) ,
    ql.YieldTermStructureHandle(ql.FlatForward(today , divYield , ql.Thirty360())) ,
    ql.YieldTermStructureHandle(ql.FlatForward(today , rf , ql.Thirty360())) ,
    ql.BlackVolTermStructureHandle(ql.BlackConstantVol(today,ql.NullCalendar() , sigma , ql.Thirty360 ())))
    option = ql.BarrierOption( barrierType , barrier , rebate , ql.PlainVanillaPayoff( optionType , strike), ql.EuropeanExercise(maturity_date))
    option.setPricingEngine(ql.AnalyticBarrierEngine(process))
    trueValue = option.NPV()
    #trueDelta=option.delta()w
    V.append(trueValue)
    #delta.append(trueDelta)

plt.plot(V)

#plt.plot(delta)
