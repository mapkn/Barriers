# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 20:31:42 2019

@author: patemi
"""

#from QuantLib import *

import QuantLib as ql

import matplotlib . pyplot as plt
barrier , barrierType , optionType , rebate = (80.0 , Barrier. DownOut , Option.Call , 0.0)

underlying , strike , rf , sigma , maturity , divYield = (100 , 105 , 5e-2 , 20e-2 , 1.0 , 0.0)

Grids = (5 , 10 , 25 , 50 , 100 , 1000 , 5000)

maxG = Grids [ -1]

today = Settings.instance().evaluationDate
maturity_date = today + int ( maturity * 12)
process = BlackScholesMertonProcess(QuoteHandle(SimpleQuote(underlying)) ,
YieldTermStructureHandle(FlatForward(today , divYield , Thirty360())) ,
YieldTermStructureHandle(FlatForward(today , rf , Thirty360())) ,
BlackVolTermStructureHandle( BlackConstantVol(today,NullCalendar() , sigma , Thirty360 ())))
option = BarrierOption( barrierType , barrier , rebate , PlainVanillaPayoff( optionType , strike), EuropeanExercise(maturity_date))
option.setPricingEngine(AnalyticBarrierEngine(process))
trueValue = option.NPV()





uErrors = []
tErrors = []

for Grid in Grids :
    option.setPricingEngine (FdBlackScholesBarrierEngine(process , maxG , Grid ))
    uErrors.append ( abs ( option . NPV ()/ trueValue -1))
    option.setPricingEngine (FdBlackScholesBarrierEngine(process , Grid , maxG ))
    tErrors.append ( abs ( option . NPV ()/ trueValue -1))
plt.loglog (Grids , uErrors , 'r-', Grids , tErrors , 'b--')
plt.xlabel ('No of Grid Points ( Log Scale )')
plt.ylabel ('Relative Error ( Log Scale )')
plt.legend (['Asset Grid Points ', 'Time Grid Points '])
plt.title ('Increasing Asset or Time Grid Keeping the Other Grid at ' + str ( maxG ))