DOKUMENTATION Provider Deckbrew API

This class offers two different methods for getting data from deckbrew:

queryName(String card title[english])
<description>
Allows the user to search for a card with a certain title. The search is „fuzzy“, which means, it will retrieve also matches below 100%

Planned Context of Use: Simple interface for searching cards with a certain name in deckbrew. 

Returns: List of JSON Objects, which are delivered as results for the query.
</description>

queryIDs([Strings]card ids)
<description>
Collects all JSON Data for cards with certain ids.

Planned Context of Use: Get all Card Data for the user collection

Returns: List of JSON Objects for the IDs of the requested cards.
</description>