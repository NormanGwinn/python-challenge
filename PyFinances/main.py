import csv
import sys

# A function to print election results
def PrintReport(fOut, netProfit, nMonths, maxIncrease, maxDecrease):
    fOut.write(f"Months:  {nMonths}\nNet Profit:  ${netProfit:,.2f}\nAverage Monthly PnL:  ${netProfit/nMonths:,.2f}\n")
    fOut.write(f"The largest month-over-month increase, ${maxIncrease[1]:,.2f}, occured in {maxIncrease[0]}\n")
    fOut.write(f"The largest month-over-month decrease, ${maxDecrease[1]:,.2f}, occured in {maxDecrease[0]}\n")

# Read the election results
sDataFile = r"C:\Users\norma\HDD_Documents\BootCamp\RU-HOU-DATA-PT-12-2019-U-C\Homework\03-Python-Challenge\Instructions\PyFinances\Resources\budget_data.csv"
with open(sDataFile, newline='', encoding='utf-8') as csvDataFile:
    rdrDataFile = csv.reader(csvDataFile)
    iRow = 0
    dNetProfit = 0.0
    dLastPnL = 0.0
    maxIncrease = ['Jan-1999', 0.0]
    maxDecrease = ['Jan-1999', 0.0]
    for row in rdrDataFile:
        if iRow > 0:
            dPnL = float(row[0])
            dNetProfit = dNetProfit + dPnL
            if dPnL - dLastPnL > maxIncrease[1]:
                maxIncrease = [row[1], dPnL - dLastPnL]
            if dPnL - dLastPnL < maxDecrease[1]:
                maxDecrease = [row[1], dPnL - dLastPnL]
            dLastPnL = dPnL
        iRow = iRow + 1

PrintReport(sys.stdout, dNetProfit, iRow - 1, maxIncrease, maxDecrease)
with open(r'\Users\norma\HDD_Documents\BootCamp\Assignments\03-Python-Challenge\python-challenge\PyFinances\BudgetReport.txt', 'w') as fReport:
    PrintReport(fReport, dNetProfit, iRow - 1, maxIncrease, maxDecrease)
