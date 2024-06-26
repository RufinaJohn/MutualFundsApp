openindex = list(range(4, 20)) + list(range(23, 34)) + list(range(37, 43)) + list(range(46, 48)) + list(range(51, 55))
closedindex = list(range(61, 65)) + list(range(68, 70)) + [73]
intervalindex = [77, 79, 81]
opendict = {'Income/Debt Oriented Schemes':[
    'Overnight Fund',
    'Liquid Fund',
    'Ultra Short Duration Fund',
    'Low Duration Fund',
    'Money Market Fund',
    'Short Duration Fund',
    'Medium Duration Fund',
    'Medium to Long Duration Fund',
    'Long Duration Fund',
    'Dynamic Bond Fund',
    'Corporate Bond Fund',
    'Credit Risk Fund',
    'Banking and PSU Fund',
    'Gilt Fund',
    'Gilt Fund with 10 year constant duration',
    'Floater Fund'
],
'Growth/Equity Oriented Schemes':[
    'Multi Cap Fund',
    'Large Cap Fund',
    'Large & Mid Cap Fund',
    'Mid Cap Fund',
    'Small Cap Fund',
    'Dividend Yield Fund',
    'Value Fund/Contra Fund',
    'Focused Fund',
    'Sectoral/Thematic Funds',
    'ELSS',
    'Flexi Cap Fund'
],
'Hybrid Schemes':[
    'Conservative Hybrid Fund',
    'Balanced Hybrid Fund/Aggressive Hybrid Fund',
    'Dynamic Asset Allocation/Balanced Advantage Fund',
    'Multi Asset Allocation Fund',
    'Arbitrage Fund',
    'Equity Savings Fund'
],
'Solution Oriented Schemes':[
    'Retirement Fund',
    'Childrens Fund'
],
'Other Schemes':[
    'Index Funds',
    'GOLD ETF',
    'Other ETFs',
    'Fund of funds investing overseas'
]}

closedict = {
'Income/Debt Oriented Schemes':[
    'Fixed Term Plan',
    'Capital Protection Oriented Schemes',
    'Infrastructure Debt Fund',
    'Other Debt Scheme'
],
'Growth/Equity Oriented Schemes':[
    'ELSS',
    'Other Equity Schemes',
    'Other Schemes'
]
}

interval = [
    'Income/Debt Oriented Schemes',
    'Growth/Equity Oriented Schemes',
    'Other Schemes'
]
types = ['Open ended Schemes', 'Close Ended Schemes', 'Interval Schemes']
subtypes = ['Income/Debt Oriented Schemes', 'Growth/Equity Oriented Schemes', 'Hybrid Schemes','Solution Oriented Schemes','Other Schemes']
names = [
    'Overnight Fund',
    'Liquid Fund',
    'Ultra Short Duration Fund',
    'Low Duration Fund',
    'Money Market Fund',
    'Short Duration Fund',
    'Medium Duration Fund',
    'Medium to Long Duration Fund',
    'Long Duration Fund',
    'Dynamic Bond Fund',
    'Corporate Bond Fund',
    'Credit Risk Fund',
    'Banking and PSU Fund',
    'Gilt Fund',
    'Gilt Fund with 10 year constant duration',
    'Floater Fund',

    'Multi Cap Fund',
    'Large Cap Fund',
    'Large & Mid Cap Fund',
    'Mid Cap Fund',
    'Small Cap Fund',
    'Dividend Yield Fund',
    'Value Fund/Contra Fund',
    'Focused Fund',
    'Sectoral/Thematic Funds',
    'ELSS', #open ended
    'Flexi Cap Fund',

    'Conservative Hybrid Fund',
    'Balanced Hybrid Fund/Aggressive Hybrid Fund',
    'Dynamic Asset Allocation/Balanced Advantage Fund',
    'Multi Asset Allocation Fund',
    'Arbitrage Fund',
    'Equity Savings Fund',

    'Retirement Fund',
    'Childrens Fund',

    'Index Funds',
    'GOLD ETF',
    'Other ETFs',
    'Fund of funds investing overseas',

    'Fixed Term Plan',
    'Capital Protection Oriented Schemes',
    'Infrastructure Debt Fund',
    'Other Debt Scheme',

    'ELSS', #close ended
    'Other Equity Schemes',

    'Fund of Funds Scheme (Domestic) **'
]

typesdict = {
    'Overnight Fund': 'Open ended Schemes',
    'Liquid Fund': 'Open ended Schemes',
    'Ultra Short Duration Fund': 'Open ended Schemes',
    'Low Duration Fund': 'Open ended Schemes',
    'Money Market Fund': 'Open ended Schemes',
    'Short Duration Fund': 'Open ended Schemes',
    'Medium Duration Fund': 'Open ended Schemes',
    'Medium to Long Duration Fund': 'Open ended Schemes',
    'Long Duration Fund': 'Open ended Schemes',
    'Dynamic Bond Fund': 'Open ended Schemes',
    'Corporate Bond Fund': 'Open ended Schemes',
    'Credit Risk Fund': 'Open ended Schemes',
    'Banking and PSU Fund': 'Open ended Schemes',
    'Gilt Fund': 'Open ended Schemes',
    'Gilt Fund with 10 year constant duration': 'Open ended Schemes',
    'Floater Fund': 'Open ended Schemes',
    'Multi Cap Fund': 'Open ended Schemes',
    'Large Cap Fund': 'Open ended Schemes',
    'Large & Mid Cap Fund': 'Open ended Schemes',
    'Mid Cap Fund': 'Open ended Schemes',
    'Small Cap Fund': 'Open ended Schemes',
    'Dividend Yield Fund': 'Open ended Schemes',
    'Value Fund/Contra Fund': 'Open ended Schemes',
    'Focused Fund': 'Open ended Schemes',
    'Sectoral/Thematic Funds': 'Open ended Schemes',
    'ELSS': 'Open ended Schemes',
    'Flexi Cap Fund': 'Open ended Schemes',
    'Conservative Hybrid Fund': 'Open ended Schemes',
    'Balanced Hybrid Fund/Aggressive Hybrid Fund': 'Open ended Schemes',
    'Dynamic Asset Allocation/Balanced Advantage Fund': 'Open ended Schemes',
    'Multi Asset Allocation Fund': 'Open ended Schemes',
    'Arbitrage Fund': 'Open ended Schemes',
    'Equity Savings Fund': 'Open ended Schemes',
    'Retirement Fund': 'Open ended Schemes',
    'Childrens Fund': 'Open ended Schemes',
    'Index Funds': 'Open ended Schemes',
    'GOLD ETF': 'Open ended Schemes',
    'Other ETFs': 'Open ended Schemes',
    'Fund of funds investing overseas': 'Open ended Schemes',
'Fixed Term Plan': 'Close Ended Schemes',
    'Capital Protection Oriented Schemes': 'Close Ended Schemes',
    'Infrastructure Debt Fund': 'Close Ended Schemes',
    'Other Debt Scheme': 'Close Ended Schemes',
    'ELSS': 'Close Ended Schemes',
    'Other Equity Schemes': 'Close Ended Schemes'
}

subtypesdict = {
    'Overnight Fund': 'Income/Debt Oriented Schemes',
    'Liquid Fund': 'Income/Debt Oriented Schemes',
    'Ultra Short Duration Fund': 'Income/Debt Oriented Schemes',
    'Low Duration Fund': 'Income/Debt Oriented Schemes',
    'Money Market Fund': 'Income/Debt Oriented Schemes',
    'Short Duration Fund': 'Income/Debt Oriented Schemes',
    'Medium Duration Fund': 'Income/Debt Oriented Schemes',
    'Medium to Long Duration Fund': 'Income/Debt Oriented Schemes',
    'Long Duration Fund': 'Income/Debt Oriented Schemes',
    'Dynamic Bond Fund': 'Income/Debt Oriented Schemes',
    'Corporate Bond Fund': 'Income/Debt Oriented Schemes',
    'Credit Risk Fund': 'Income/Debt Oriented Schemes',
    'Banking and PSU Fund': 'Income/Debt Oriented Schemes',
    'Gilt Fund': 'Income/Debt Oriented Schemes',
    'Gilt Fund with 10 year constant duration': 'Income/Debt Oriented Schemes',
    'Floater Fund': 'Income/Debt Oriented Schemes',
    'Multi Cap Fund': 'Growth/Equity Oriented Schemes',
    'Large Cap Fund': 'Growth/Equity Oriented Schemes',
    'Large & Mid Cap Fund': 'Growth/Equity Oriented Schemes',
    'Mid Cap Fund': 'Growth/Equity Oriented Schemes',
    'Small Cap Fund': 'Growth/Equity Oriented Schemes',
    'Dividend Yield Fund': 'Growth/Equity Oriented Schemes',
    'Value Fund/Contra Fund': 'Growth/Equity Oriented Schemes',
    'Focused Fund': 'Growth/Equity Oriented Schemes',
    'Sectoral/Thematic Funds': 'Growth/Equity Oriented Schemes',
    'ELSS': 'Growth/Equity Oriented Schemes',
    'Flexi Cap Fund': 'Growth/Equity Oriented Schemes',
    'Conservative Hybrid Fund': 'Hybrid Schemes',
    'Balanced Hybrid Fund/Aggressive Hybrid Fund': 'Hybrid Schemes',
    'Dynamic Asset Allocation/Balanced Advantage Fund': 'Hybrid Schemes',
    'Multi Asset Allocation Fund': 'Hybrid Schemes',
    'Arbitrage Fund': 'Hybrid Schemes',
    'Equity Savings Fund': 'Hybrid Schemes',
    'Retirement Fund': 'Solution Oriented Schemes',
    'Childrens Fund': 'Solution Oriented Schemes',
    'Index Funds': 'Other Schemes',
    'GOLD ETF': 'Other Schemes',
    'Other ETFs': 'Other Schemes',
    'Fund of funds investing overseas': 'Other Schemes',
    'Fixed Term Plan': 'Income/Debt Oriented Schemes',
    'Capital Protection Oriented Schemes': 'Income/Debt Oriented Schemes',
    'Infrastructure Debt Fund': 'Income/Debt Oriented Schemes',
    'Other Debt Scheme': 'Income/Debt Oriented Schemes',
    'Other Equity Schemes': 'Growth/Equity Oriented Schemes',
    'ELSS': 'Growth/Equity Oriented Schemes'
}
fields = ["No. of Schemes", "No. of Folios", "Funds Mobilized (INR in crore)", "Repurchase/Redemption (INR in crore)", "Net Assets Under Management (INR in crore)", "Average Net Assets Under Management (INR in crore)", "No. of segregated portfolios created", "Net Assets Under Management in segregated portfolio (INR in crores)", "Net Inflow or Outflow", "Net Asset under Management per Scheme", "Net Inflow or Outflow per Scheme"]
allfields = ["No. of Schemes", "No. of Folios", "Funds Mobilized (INR in crore)", "Repurchase/Redemption (INR in crore)", "Net Assets Under Management (INR in crore)", "Average Net Assets Under Management (INR in crore)", "No. of segregated portfolios created", "Net Assets Under Management in segregated portfolio (INR in crores)", "Net Inflow or Outflow", "Net Asset under Management per Scheme", "Net Inflow or Outflow per Scheme"]
