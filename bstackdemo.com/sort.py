from dsl import *

@command
def IS_SORT(browser, data_list, sort_type="ASC"):
	data_list = [ float(x) for x in data_list ]
	return all(map(lambda x, y: x < y if sort_type== "ASC" else x > y, data_list[0::2], data_list[1::2]))

TEST["Order by"](
	URL
	, DATA(".sort > select", "lowestprice")
	, IS_SORT(ALL(".val > b", unique=True)) == True
	
	, DATA(".sort > select", "highestprice")
	, IS_SORT(ALL(".val > b", unique=True), "DESC") == True
	
	, tags="sort"
)
