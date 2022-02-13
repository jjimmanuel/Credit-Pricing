
from bdb import effective
import QuantLib as ql
from QuantLib import *

day =  Date(20, 12, 2020)
Settings_instance().evaluationDate = day


side = ql.Protection.Buyer
nominal = 10e6
spread = 34.6 / 10000
r1 = SimpleQuote(0.01)
r2 = 0.05
dayCounter = Actual365Fixed()
effective_date = day
termination_date = Date(20, 12, 2025)
frequency = Period('6M')

cdsSchedule = ql.MakeSchedule(effective_date, termination_date, frequency)

cds = ql.CreditDefaultSwap(side, nominal, spread, cdsSchedule, ql.Following, ql.Actual365Fixed())

hazard_rate = FlatHazardRate(day, QuoteHandle(r1), dayCounter)
flat_forward = FlatForward(day, r2, dayCounter)

defaultProbability = ql.DefaultProbabilityTermStructureHandle(hazard_rate)

yts = ql.YieldTermStructureHandle(flat_forward)

recoveryRate = 0.4

engine = ql.IsdaCdsEngine(defaultProbability, recoveryRate, yts)
cds.setPricingEngine(engine)
print(cds.NPV())





