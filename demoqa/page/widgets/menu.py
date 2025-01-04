from dsl import *

TEST["Провенрка открывания меню"](
	URL("/menu")
	, ONE("#nav > li> ul", "css::display") == "none"
	, HOVER("Main Item 2")
	, ONE("#nav > li> ul", "css::display") == "block"
	, tags="widget,menu"
)


