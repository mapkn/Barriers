  
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 20:31:42 2019
@author: patemi
"""

from QuantLib import *

#import QuantLib as ql

import matplotlib.pyplot as plt
import numpy as np

S=list(np.arange(107,109.99,0.01))

V=[]

for s in S:
        
    barrier , barrierType , optionType , rebate = (110.0 , Barrier.UpOut , Option.Call , 0.0)
    
    underlying=s    
    
    
    strike , rf , sigma , maturity , divYield = (105 , 5e-2 , 20e-2 , 0.25 , 0.0)
    
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
    V.append(trueValue)





