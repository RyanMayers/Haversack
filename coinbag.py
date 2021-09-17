from consts import coinValue

def addCoins(Copper = 0, Silver = 0, Electrum = 0, Gold = 0, Platinum = 0):
    newWealth = 0
    newWealth += (Copper) + (Silver * 10) + (Electrum * 50) + (Gold * 100) + (Platinum * 1000)
    return newWealth

def sortCoins(Copper = 0, Silver = 0, Electrum = 0, Gold = 0, Platinum = 0):
    # 1,000 Copper = 100 Silver = 50 Electrum = 10 Gold = 1 Platinum
    
    # First, convert all wealth to the smallest value, copper.
    totalWealth = addCoins(Copper, Silver, Electrum, Gold, Platinum)

    # Now give us a list to iterate through
    coinIDs = ["pp", "gp", "ep", "sp", "cp"]
    
    # This dict will have our sorted coin amounts.
    sortedBag = {}
    
    # Get ready for the loop-de-loop
    # Wheeeee!
    for i in coinIDs:
        numCoins = (totalWealth // coinValue[i])
        sortedBag[i] = numCoins
        totalWealth -= (numCoins * coinValue[i])
    return sortedBag