
from tkinter import TRUE
import QuantLib as ql
from QuantLib import *

day =  Date(2, 1, 2019)
Settings_instance().evaluationDate = day


side = ql.Protection.Buyer
nominal = 10e6
spread = 34.6 / 10000
r1 = SimpleQuote(0.01)
r2 = 0.05
dayCounter = Actual365Fixed()
effective_date = day
termination_date = Date(20, 12, 2024)
frequency = Period('3M')

cdsSchedule = MakeSchedule(effective_date, termination_date, frequency)

cds = CreditDefaultSwap(side, nominal, spread, cdsSchedule, ql.Following, ql.Actual365Fixed())

expiry = Date(15,6,2020)
exercise = EuropeanExercise(expiry)

swaption = CdsOption(cds, exercise, True)

rate = 0.03
compounding = Compounded
frequency = Annual

curve = FlatForward(day, rate, dayCounter, compounding, frequency)
curveHandle = YieldTermStructureHandle(curve)

engine = BlackSwaptionEngine(curveHandle, QuoteHandle(SimpleQuote(rate)))
swaption.setPricingEngine(engine)
swaption.NPV()







