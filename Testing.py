import RestProvider.RestProvider as Rest
import FilteringUtility as Filter
import RestProvider.FormattingUtility as Format

def printResults(results):
    for element in results:
        print(element["name"])




deckbrew = Rest.RestProvider()

# get testing collection
# cho-manno (white), blackcleave (black) and bloodcrazed goblin (red) have type creature
# goblin assault (red) has type enchantment
res = deckbrew.queryIDs(["cho-manno-revolutionary", "blackcleave-goblin", "bloodcrazed-goblin", "goblin-assault"])
#print(res)

# filter the results by type (other parameters)
processedRes = list(Filter.filterByType(res, "creature"))
processedRes2 = list(Filter.filterByType(res, "enchantment"))

processedRes3 = list(Filter.filterByColor(res, "white"))
processedRes4 = list(Filter.filterByColor(res, "red"))
processedRes5 = list(Filter.filterByColor(res, "black"))

# sort by toughness higher/equal 2
processedRes6 = list(Filter.filterByToughness(res, 2, true))
processedRes7 = list(Filter.filterByToughness(res, 2, false))

printResults(processedRes)
print(" ")
printResults(processedRes2)

print(" ")
print(" ")

printResults(processedRes3)
print(" ")
printResults(processedRes4)
print(" ")
printResults(processedRes5)

print(" ")
print(" ")

printResults(processedRes6)
print(" ")
printResults(processedRes7)
