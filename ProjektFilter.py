# ## = Markierung für mögliche Folgefehler


listeMitDsI = getCollection()
listErgebnisse = queryIDs(listeMitDsI) #[:] , weil lists mutable und unsicher wegen methode ob listeitIDs beeinflusst wird..

FilterTypeBool = False

FilterCostGThenBool = False
FilterCostLThenBool = False
FilterCostEqualBool = False

FilterToughnessGThenBool = False
FilterToughnessLThenBool = False
FilterToughnessEqualBool = False

FilterPowerGThenBool = False
FilterPowerLThenBool = False
FilterPowerEqualBool = False

FilterColorRed = False
FilterColorBlue = False
FilterColorGreen = False
FilterColorBlack = False
FilterColorWhite = False

FilterType = "none"


FilterCostGThenInt = -254
FilterCostLThenInt = -254
FilterCostEqualInt = -254


FilterToughnessGThenInt = -254
FilterToughnessLThenInt = -254
FilterToughnessEqualInt = -254


FilterPowerGThenInt = -254
FilterPowerLThenInt = -254
FilterPowerEqualInt = -254



def FilterShowColor (color = "none"): #
    color = str(color)
    color = color.lower()
    global FilterColorRed
    global FilterColorBlue
    global FilterColorGreen 
    global FilterColorBlack 
    global FilterColorWhite 
    
    if (color != "red" and color != "white" and color != "black" and color != "blue" and color != "green" and color != "none" ):
        #bleibt beim alten da ungültiger Wert!
        
    elif (color == "none" ):
        FilterColorRed = False
        FilterColorBlue = False
        FilterColorGreen = False
        FilterColorBlack = False
        FilterColorWhite = False
        ReFilter()
        #eingebaute ResetColorFunktion
        
    else:
        newListErgebnisse = []
        global listErgebnisse
        
        counterAllListElements = 0
        while counterAllListElements < len(listErgebnisse):
            counter = 0 #counter steht für Position in der List, des Dict.Eintrags "colors" - gibt ja Multicolor!
            while counter < len(listErgebnisse[counterAllListElements]["colors"]):
                if ( listErgebnisse[counterAllListElements]["colors"][counter] == color):
                    newListErgebnisse.append(listErgebnisse[counterAllListElements] )
                    
                counter += 1
                
            counterAllListElements += 1
        

        if ( color == "green"):
            FilterColorGreen = True       
        if ( color == "blue"):
            FilterColorBlue = True         
        if ( color == "black"):
            FilterColorBlack = True         
        if ( color == "white"):
            FilterColorWhite = True         
        if ( color == "red"):
            FilterColorRed = True    
            
        listErgebnisse = newListErgebnisse[:]
    
    
    
    
    
def FilterShowType (type = "none"):
    type = str(type)
    type = type.lower()
    global FilterTypeBool
    global FilterType
    
    
    
    if (type != "artifact"   and type != "creature" and type != "enchantment" and type != "instant" and type != "land"  and type != "phenomenon" and type != "plane" and type != "planeswalker" and type != "scheme"  and type != "sorcery" and type != "tribal" and type != "vanguard"  and type != "none" ):
        #bleibt beim alten da ungültiger Wert!
    
    elif (color == "none" ):       
        FilterTypeBool = False        
        FilterType = "none"
        ReFilter()
        # wieder eingebaute ResetTypeFunktion
   
    else :
        
        if (FilterTypeBool == False):
            FilterType = type
            newListErgebnisse = []
            global listErgebnisse
            
            counterAllListElements = 0
            while counterAllListElements < len(listErgebnisse):
                counter = 0 
                while counter < len(listErgebnisse[counterAllListElements]["type"]):
                    if ( listErgebnisse[counterAllListElements]["type"][counter] == FilterType):
                       newListErgebnisse.append(listErgebnisse[counterAllListElements] ) 
                    counter += 1
                counterAllListElements += 1

            FilterTypeBool = True
            listErgebnisse = newListErgebnisse[:]
            
        else:
            FilterType = type
            ReFilter()
    

def FilterToughnessReset():
    global FilterToughnessGThenBool 
    global FilterToughnessLThenBool 

    global FilterToughnessEqualBool 
            
    global FilterToughnessGThenInt 
    global FilterToughnessLThenInt 

    global FilterToughnessEqualInt 
            
    FilterToughnessGThenInt = -254
    FilterToughnessLThenInt = -254
    FilterToughnessEqualInt = -254
    FilterToughnessGThenBool = False
    FilterToughnessLThenBool = False
    FilterToughnessEqualBool = False
            
    ReFilter()
    
def FilterToughness (IntT = -1, Operator = ">"):
    Operator = str(Operator)
    if ( isinstance( IntT, ( int, long ) ) or (IntT == "*" and Operator == "=")) :
        if (Operator == "<" or Operator == "=" or Operator == ">") :
        
            global listErgebnisse
            
            global FilterToughnessGThenBool 
            global FilterToughnessLThenBool 
            global FilterToughnessEqualBool 
            
            global FilterToughnessGThenInt 
            global FilterToughnessLThenInt 
            global FilterToughnessEqualInt 
            
            if (Operator == "="):
                if ( FilterToughnessGThenBool == True or FilterToughnessLThenBool == True):
                    FilterToughnessGThenInt = -254
                    FilterToughnessLThenInt = -254
                    FilterToughnessGThenBool = False
                    FilterToughnessLThenBool = False
                    FilterToughnessEqualInt = IntT
                    FilterToughnessEqualBool = True
                    ReFilter()

             
            elif (Operator == "<" or Operator == ">"):
                if ( FilterToughnessEqualBool == True ):
                    FilterToughnessEqualInt = -254
                    FilterToughnessEqualBool = False
                    if (Operator == "<"):
                        FilterToughnessLThenInt = IntT
                        FilterToughnessLThenBool = True
                    if (Operator == ">"):
                        FilterToughnessGThenInt = IntT
                        FilterToughnessGThenBool = True
                    ReFilter()

                    
            
            else:
                newListErgebnisse = []
                counterAllListElements = 0
                
                while counterAllListElements < len(listErgebnisse):
                    if (Operator == "<"):
                        if (int(listErgebnisse[counterAllListElements]["toughness"]) < IntT or listErgebnisse[counterAllListElements]["toughness"] == "*"):
                            newListErgebnisse.append(listErgebnisse[counterAllListElements] ) 
                    
                    if (Operator == ">"):
                        if (int(listErgebnisse[counterAllListElements]["toughness"]) > IntT or listErgebnisse[counterAllListElements]["toughness"] == "*"):
                            newListErgebnisse.append(listErgebnisse[counterAllListElements] ) 
                            
                    if (Operator == "=" and IntT != "*"):
                        if (int(listErgebnisse[counterAllListElements]["toughness"]) == IntT):
                            newListErgebnisse.append(listErgebnisse[counterAllListElements] )  
                            
                    if (Operator == "=" and IntT == "*"):        
                        if (listErgebnisse[counterAllListElements]["toughness"] == "*"):
                            newListErgebnisse.append(listErgebnisse[counterAllListElements] )  
                        
                    counterAllListElements += 1
                    
                listErgebnisse = newListErgebnisse[:]
                if (Operator == "<"):
                    FilterToughnessLThenInt = IntT
                    FilterToughnessLThenBool = True
                if (Operator == ">"):
                    FilterToughnessGThenInt = IntT
                    FilterToughnessGThenBool = True
                if (Operator == "="):
                    if (IntT != "*"):
                        FilterToughnessEqualInt = IntT
                    FilterToughnessEqualBool = True
                    
                
            
    elif (Operator == "!=" and  IntT == "*"):
        global listErgebnisse
        newListErgebnisse = []
        counterAllListElements = 0
        
        while counterAllListElements < len(listErgebnisse):
            if ( listErgebnisse[counterAllListElements]["toughness"] != "*"):
               newListErgebnisse.append(listErgebnisse[counterAllListElements] ) 
            counterAllListElements += 1
        listErgebnisse = newListErgebnisse[:]
    
    
    
def FilterPowerReset():
    global FilterPowerGThenBool 
    global FilterPowerLThenBool 

    global FilterPowerEqualBool 
            
    global FilterPowerGThenInt 
    global FilterPowerLThenInt 

    global FilterPowerEqualInt 
            
    FilterPowerGThenInt = -254
    FilterPowerLThenInt = -254
    FilterPowerEqualInt = -254
    FilterPowerGThenBool = False
    FilterPowerLThenBool = False
    FilterPowerEqualBool = False
            
    ReFilter()
    
def FilterPower (IntT = -1, Operator = ">"):
    Operator = str(Operator)
    if ( isinstance( IntT, ( int, long ) ) or (IntT == "*" and Operator == "=")) :
        if (Operator == "<" or Operator == "=" or Operator == ">") :
        
            global listErgebnisse
            
            global FilterPowerGThenBool 
            global FilterPowerLThenBool 
            global FilterPowerEqualBool 
            
            global FilterPowerGThenInt 
            global FilterPowerLThenInt 
            global FilterPowerEqualInt 
            
            if (Operator == "="):
                if ( FilterPowerGThenBool == True or FilterPowerLThenBool == True):
                    FilterPowerGThenInt = -254
                    FilterPowerLThenInt = -254
                    FilterPowerGThenBool = False
                    FilterPowerLThenBool = False
                    FilterPowerEqualInt = IntT
                    FilterPowerEqualBool = True
                    ReFilter()

             
            elif (Operator == "<" or Operator == ">"):
                if ( FilterPowerEqualBool == True ):
                    FilterPowerEqualInt = -254
                    FilterPowerEqualBool = False
                    if (Operator == "<"):
                        FilterPowerLThenInt = IntT
                        FilterPowerLThenBool = True
                    if (Operator == ">"):
                        FilterPowerGThenInt = IntT
                        FilterPowerGThenBool = True
                    ReFilter()

                    
            
            else:
                newListErgebnisse = []
                counterAllListElements = 0
                while counterAllListElements < len(listErgebnisse):
                    if (Operator == "<"):
                        if (int(listErgebnisse[counterAllListElements]["power"]) < IntT or listErgebnisse[counterAllListElements]["power"]== "*"):
                            newListErgebnisse.append(listErgebnisse[counterAllListElements] ) 
                    
                    if (Operator == ">"):
                        if (int(listErgebnisse[counterAllListElements]["power"]) > IntT or listErgebnisse[counterAllListElements]["power"]== "*"):
                            newListErgebnisse.append(listErgebnisse[counterAllListElements] ) 
                            
                    if (Operator == "=" and IntT != "*"):
                        if (int(listErgebnisse[counterAllListElements]["power"]) == IntT):
                            newListErgebnisse.append(listErgebnisse[counterAllListElements] )  
                            
                    if (Operator == "=" and IntT == "*"):        
                        if (listErgebnisse[counterAllListElements]["power"] == "*"):
                            newListErgebnisse.append(listErgebnisse[counterAllListElements] )  
                        
                    counterAllListElements += 1
                    
                listErgebnisse = newListErgebnisse[:]
                
                if (Operator == "<"):
                    FilterPowerLThenInt = IntT
                    FilterPowerLThenBool = True
                if (Operator == ">"):
                    FilterPowerGThenInt = IntT
                    FilterPowerGThenBool = True
                if (Operator == "="):
                    if (IntT != "*"):
                        FilterPowerEqualInt = IntT
                    FilterPowerEqualBool = True
            
    elif (Operator == "!=" and  IntT == "*"):
        global listErgebnisse
        newListErgebnisse = []
        counterAllListElements = 0
        
        while counterAllListElements < len(listErgebnisse):
            if ( listErgebnisse[counterAllListElements]["power"] != "*"):
               newListErgebnisse.append(listErgebnisse[counterAllListElements] ) 
            counterAllListElements += 1
        listErgebnisse = newListErgebnisse[:]
    
    
    
def FilterCostReset():
    global FilterCostGThenBool 
    global FilterCostLThenBool 

    global FilterCostEqualBool 
            
    global FilterCostGThenInt 
    global FilterCostLThenInt 

    global FilterCostEqualInt 
            
    FilterCostGThenInt = -254
    FilterCostLThenInt = -254
    FilterCostEqualInt = -254
    FilterCostGThenBool = False
    FilterCostLThenBool = False
    FilterCostEqualBool = False
            
    ReFilter()
    
def FilterCost (IntT = -1, Operator = ">"):
    
    if ( isinstance( IntT, ( int, long ) )) :
        if (Operator == "<" or Operator == "=" or Operator == ">") :
        
            global listErgebnisse
            
            global FilterCostGThenBool 
            global FilterCostLThenBool 
            global FilterCostEqualBool 
            
            global FilterCostGThenInt 
            global FilterCostLThenInt 
            global FilterCostEqualInt 
            
            if (Operator == "="):
                if ( FilterCostGThenBool == True or FilterCostLThenBool == True):
                    FilterCostGThenInt = -254
                    FilterCostLThenInt = -254
                    FilterCostGThenBool = False
                    FilterCostLThenBool = False
                    FilterCostEqualInt = IntT
                    FilterCostEqualBool = True
                    ReFilter()

             
            elif (Operator == "<" or Operator == ">"):
                if ( FilterCostEqualBool == True ):
                    FilterCostEqualInt = -254
                    FilterCostEqualBool = False
                    if (Operator == "<"):
                        FilterCostLThenInt = IntT
                        FilterCostLThenBool = True
                    if (Operator == ">"):
                        FilterCostGThenInt = IntT
                        FilterCostGThenBool = True
                    ReFilter()

                    
            
            else:
                newListErgebnisse = []
                counterAllListElements = 0
                while counterAllListElements < len(listErgebnisse):
                    costSum = listErgebnisse[counterAllListElements]["cmc"]
                    if (Operator == "<"):
                        if (costSum < IntT ):
                            newListErgebnisse.append(listErgebnisse[counterAllListElements] ) 
                    
                    if (Operator == ">"):
                        if (costSum > IntT ):
                            newListErgebnisse.append(listErgebnisse[counterAllListElements] ) 
                               
                    if (Operator == "="):        
                        if (costSum == IntT):
                            newListErgebnisse.append(listErgebnisse[counterAllListElements] )  
                        
                    counterAllListElements += 1
                    
                listErgebnisse = newListErgebnisse[:]
                
                if (Operator == "<"):
                    FilterCostLThenInt = IntT
                    FilterCostLThenBool = True
                if (Operator == ">"):
                    FilterCostGThenInt = IntT
                    FilterCostGThenBool = True
                if (Operator == "="):
                    FilterCostEqualInt = IntT
                    FilterCostEqualBool = True
            
    

def ReFilter():
    global listErgebnisse
    global FilterTypeBool

    global FilterCostGThenBool
    global FilterCostLThenBool
    global FilterCostEqualBool

    global FilterToughnessGThenBool
    global FilterToughnessLThenBool
    global FilterToughnessEqualBool

    global FilterPowerGThenBool
    global FilterPowerLThenBool
    global FilterPowerEqualBool

    global FilterColorRed
    global FilterColorBlue
    global FilterColorGreen
    global FilterColorBlack
    global FilterColorWhite

    global FilterType


    global FilterCostGThenInt
    global FilterCostLThenInt
    global FilterCostEqualInt


    global FilterToughnessGThenInt
    global FilterToughnessLThenInt
    global FilterToughnessEqualInt


    global FilterPowerGThenInt
    global FilterPowerLThenInt
    global FilterPowerEqualInt

    listErgebnisse = queryIDs(listeMitDsI)
    
    if (FilterTypeBool == True):
        
        newListErgebnisse = []
        
        
        counterAllListElements = 0
        while counterAllListElements < len(listErgebnisse):
            counter = 0 
            while counter < len(listErgebnisse[counterAllListElements]["type"]):
                if ( listErgebnisse[counterAllListElements]["type"][counter] == FilterType):
                   newListErgebnisse.append(listErgebnisse[counterAllListElements] ) 
                counter += 1
            counterAllListElements += 1

        listErgebnisse = newListErgebnisse[:]

    if (FilterColorBlack == True):
        
        newListErgebnisse = []
        
        
        counterAllListElements = 0
        while counterAllListElements < len(listErgebnisse):
            counter = 0 
            while counter < len(listErgebnisse[counterAllListElements]["colors"]):
                if ( listErgebnisse[counterAllListElements]["colors"][counter] == "black"):
                   newListErgebnisse.append(listErgebnisse[counterAllListElements] ) 
                counter +=1
            counterAllListElements += 1

        listErgebnisse = newListErgebnisse[:]

    if (FilterColorBlue == True):
        
        newListErgebnisse = []
        
        
        counterAllListElements = 0
        while counterAllListElements < len(listErgebnisse):
            counter = 0 
            while counter < len(listErgebnisse[counterAllListElements]["colors"]):
                if ( listErgebnisse[counterAllListElements]["colors"][counter] == "blue"):
                   newListErgebnisse.append(listErgebnisse[counterAllListElements] ) 
                counter +=1
            counterAllListElements += 1

        listErgebnisse = newListErgebnisse[:]

    if (FilterColorGreen == True):
        
        newListErgebnisse = []
        
        
        counterAllListElements = 0
        while counterAllListElements < len(listErgebnisse):
            counter = 0 
            while counter < len(listErgebnisse[counterAllListElements]["colors"]):
                if ( listErgebnisse[counterAllListElements]["colors"][counter] == "green"):
                   newListErgebnisse.append(listErgebnisse[counterAllListElements] ) 
                counter +=1
            counterAllListElements += 1

        listErgebnisse = newListErgebnisse[:]
    
    if (FilterColorRed == True):
        
        newListErgebnisse = []
        
        
        counterAllListElements = 0
        while counterAllListElements < len(listErgebnisse):
            counter = 0 
            while counter < len(listErgebnisse[counterAllListElements]["colors"]):
                if ( listErgebnisse[counterAllListElements]["colors"][counter] == "red"):
                   newListErgebnisse.append(listErgebnisse[counterAllListElements] ) 
                counter +=1
            counterAllListElements += 1

        listErgebnisse = newListErgebnisse[:]

    if (FilterColorWhite == True):
        newListErgebnisse = []
        counterAllListElements = 0
        while counterAllListElements < len(listErgebnisse):
            counter = 0 
            while counter < len(listErgebnisse[counterAllListElements]["colors"]):
                if ( listErgebnisse[counterAllListElements]["colors"][counter] == "white"):
                   newListErgebnisse.append(listErgebnisse[counterAllListElements] ) 
                counter +=1
            counterAllListElements += 1
        listErgebnisse = newListErgebnisse[:]

    if (FilterCostGThenBool == True):       
        newListErgebnisse = []
        counterAllListElements = 0
        while counterAllListElements < len(listErgebnisse):
            costSum = listErgebnisse[counterAllListElements]["cmc"]
            if (costSum > FilterCostGThenInt ):
                newListErgebnisse.append(listErgebnisse[counterAllListElements] ) 
            counterAllListElements += 1           
        listErgebnisse = newListErgebnisse[:]
    if (FilterCostLThenBool == True):       
        newListErgebnisse = []
        counterAllListElements = 0
        while counterAllListElements < len(listErgebnisse):
            costSum = listErgebnisse[counterAllListElements]["cmc"]
            if (costSum < FilterCostLThenInt ):
                newListErgebnisse.append(listErgebnisse[counterAllListElements] ) 
            counterAllListElements += 1           
        listErgebnisse = newListErgebnisse[:]
    if (FilterCostEqualBool == True):       
        newListErgebnisse = []
        counterAllListElements = 0
        while counterAllListElements < len(listErgebnisse):
            costSum = listErgebnisse[counterAllListElements]["cmc"]
            if (costSum == FilterCostEqualInt ):
                newListErgebnisse.append(listErgebnisse[counterAllListElements] ) 
            counterAllListElements += 1           
        listErgebnisse = newListErgebnisse[:]
        
    if (FilterToughnessGThenBool == True):       
        newListErgebnisse = []
        counterAllListElements = 0
        while counterAllListElements < len(listErgebnisse):
            if (int(listErgebnisse[counterAllListElements]["toughness"]) > FilterToughnessGThenInt or listErgebnisse[counterAllListElements]["toughness"]== "*"):
                newListErgebnisse.append(listErgebnisse[counterAllListElements] ) 
            counterAllListElements += 1           
        listErgebnisse = newListErgebnisse[:]
    if (FilterToughnessLThenBool == True):       
        newListErgebnisse = []
        counterAllListElements = 0
        while counterAllListElements < len(listErgebnisse):
            if (int(listErgebnisse[counterAllListElements]["toughness"]) < FilterToughnessLThenInt or listErgebnisse[counterAllListElements]["toughness"]== "*"):
                newListErgebnisse.append(listErgebnisse[counterAllListElements] ) 
            counterAllListElements += 1           
        listErgebnisse = newListErgebnisse[:]
    if (FilterToughnessEqualBool == True):       
        newListErgebnisse = []
        counterAllListElements = 0
        while counterAllListElements < len(listErgebnisse):
            if (int(listErgebnisse[counterAllListElements]["toughness"]) == FilterToughnessEqualInt ):
                newListErgebnisse.append(listErgebnisse[counterAllListElements] ) 
            counterAllListElements += 1           
        listErgebnisse = newListErgebnisse[:]

        
    if (FilterPowerGThenBool == True):       
        newListErgebnisse = []
        counterAllListElements = 0
        while counterAllListElements < len(listErgebnisse):
            if (int(listErgebnisse[counterAllListElements]["power"]) > FilterPowerGThenInt or listErgebnisse[counterAllListElements]["power"]== "*" ):
                newListErgebnisse.append(listErgebnisse[counterAllListElements] ) 
            counterAllListElements += 1           
        listErgebnisse = newListErgebnisse[:]
    if (FilterPowerLThenBool == True):       
        newListErgebnisse = []
        counterAllListElements = 0
        while counterAllListElements < len(listErgebnisse):
            if (int(listErgebnisse[counterAllListElements]["power"]) < FilterPowerLThenInt or listErgebnisse[counterAllListElements]["power"]== "*" ):
                newListErgebnisse.append(listErgebnisse[counterAllListElements] ) 
            counterAllListElements += 1           
        listErgebnisse = newListErgebnisse[:]
    if (FilterPowerEqualBool == True):       
        newListErgebnisse = []
        counterAllListElements = 0
        while counterAllListElements < len(listErgebnisse):
            if (int(listErgebnisse[counterAllListElements]["power"]) == FilterPowerEqualInt):
                newListErgebnisse.append(listErgebnisse[counterAllListElements] ) 
            counterAllListElements += 1           
        listErgebnisse = newListErgebnisse[:]