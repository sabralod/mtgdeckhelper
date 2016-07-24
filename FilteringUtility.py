# Static utility for filtering by certain params

import json
# - filterByType - V
# - filterByColor -
# - filterByOverallCost
# - filterByToughness
# - filterByPower

# constant values for the key params
TAG_TYPES = "types"
TAG_COLORS = "colors"
TAG_OVERALLCOST = "cmc"
TAG_POWER = "power"
TAG_TOUGHNESS = "toughness"

def filterByType(oldList, searchedType):
    # this list will contain all the results
    # which have the fitting type
    resultList = []

    # work through all cards in the list
    for card in oldList:
        # check, whether the card has a "types" attribute (card represented as dictionary)
        if TAG_TYPES in card:
            # search all types of a card for the searched type
            for currentType in card.get(TAG_TYPES):
                # well, in this case the current card contains the desired type
                if (currentType == searchedType):
                    # add card to result list
                    resultList.append(card)
                    # leave the current for loop
                    break

    # processed all cards and return the list
    return resultList

def filterByColor(oldList, searchedColor):
    resultList = []

    for card in oldList:
        if TAG_COLORS in card:
            for currentColor in card.get(TAG_COLORS):
                if(currentColor == searchedColor):
                    resultList.append(card)
                    break;

    return resultList

# min: boolean
# if min = true: only values greater or equal
# if max = true: only values smaller or equal
def filterByToughness(oldList, toughnessThreshold, min):
    resultList = []

    for card in oldList:
        if TAG_TOUGHNESS in card:
            toughness = int(card.get(TAG_TOUGHNESS)
            # if toughness values greater or equal are desired
            if min:
                # if toughness is higher or equal
                if(toughness >= toughnessThreshold):
                    resultList.append(card)
            # if t val smaller or equal is desired
            else:
                if(toughness <= toughness):
                    resultList.append(card)

    return resultList
