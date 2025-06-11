from dsl import *

TEST["Typos"](
	URL("/typos")
	, IF(ONE("[0]::.example > p", timeout=0.1) < "won't", (
		PRINT("На странице есть опечатка, перезагружаем пока не пропадёт")
		, WHILE(ONE("[0]::.example > p", timeout=0.1) < "won't", REFRESH, iteration=10)
	), PRINT("На странице нет опечатки"))
	
	, description="This example demonstrates a typo being introduced. It does it randomly on each page load."
	, tags="page,typos"
	, test_id = 1
)

TEST["Infinite Scroll"](
	URL("/infinite_scroll")
	, ARG("scroll", HEIGHT(scroll=True))
	, SCROLL(HEIGHT * 2)
	, HEIGHT(scroll=True) > ARG("scroll")
	, tags="page,scroll"
)
