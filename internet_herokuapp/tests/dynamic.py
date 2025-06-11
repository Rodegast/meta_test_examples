from dsl import *

# Нам всё равно скрывается элемент или создаётся, по этому 2 теста почти одинаковые.

TEST["Element on page that is hidden"](
	URL("/dynamic_loading")
	, CLICK("Example 1")
	
	, "Start"
	, CLICK("#start > button")
	, ONE("#loading", "css::display") == "block"
	
	, "Finish"
	, ONE("#loading", "css::display", timeout=5) == "none"
	, ONE("#finish") == "Hello World!"
	
	, tags = "dinamic"
)

TEST["Element rendered after the fact"](
	URL("/dynamic_loading")
	, CLICK("Example 2")
	
	, "Start"
	, CLICK("#start > button")
	, ONE("#loading", "css::display") == "block"
	
	, "Finish"
	, ONE("#loading", "css::display", timeout=5) == "none"
	, ONE("#finish") == "Hello World!"
	
	, tags = "dinamic"
)
