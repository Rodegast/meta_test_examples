from dsl import *

@command
def IS_SORT(browser, data_list, sort_type="ASC"):
	return all(map(lambda x, y: x <= y if sort_type == "ASC" else x >= y, data_list[0::2], data_list[1::2]))

@command
def PRICE_SORT(browser, list_prise, sort_type="ASC"):
	return IS_SORT([ float(x[1:]) for x in list_prise ], sort_type)

test = TEST["Сортировка"](
	URL(ARG("url"))
	, COUNT(".product-item") > 1
	
	, "Сортировка по возростанию цены"
	, DATA("[1]::#sorter", "position")
	, DATA("[1]::#sorter", "price")
	, PRICE_SORT(ALL("[data-price-type=\"finalPrice\"]>.price")) == True
	
	, "Сортировка по убыванию цены"
	, CLICK("[1]::[data-role=\"direction-switcher\"]")
	, PRICE_SORT(ALL("[data-price-type=\"finalPrice\"]>.price"), "DESC") == True
	
	, "Сортировка по убыванию наименования"
	, DATA("[1]::#sorter", "position")
	, DATA("[1]::#sorter", "name")
	, IS_SORT(ALL(".product-item-name"), "DESC") == True
	
	, "Сортировка по возростанию наименования"
	, CLICK("[1]::[data-role=\"direction-switcher\"]")
	, IS_SORT(ALL(".product-item-name")) == True
	
	, single_thread=False
	, fatality=False
	, tags="sort"
)
test(url="/women/tops-women/hoodies-and-sweatshirts-women.html")
test(url="/women/bottoms-women/shorts-women.html")
test(url="/women/bottoms-women/pants-women.html")
test(url="/women/tops-women/jackets-women.html")
test(url="/women/tops-women/tanks-women.html")
test(url="/women/tops-women/tees-women.html")
test(url="/men/tops-men/hoodies-and-sweatshirts-men.html")
test(url="/men/tops-men/jackets-men.html")
test(url="/men/tops-men/tanks-men.html")
test(url="/men/tops-men/tees-men.html")
test(url="/men/bottoms-men/shorts-men.html")
test(url="/men/bottoms-men/pants-men.html")
test(url="/gear/fitness-equipment.html")
test(url="/gear/watches.html")
test(url="/gear/bags.html")
