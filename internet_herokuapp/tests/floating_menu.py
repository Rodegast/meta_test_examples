from dsl import *

TEST["floating_menu"](
	URL("/floating_menu")
	
	, "Меню не смещено"
	, ONE("#menu", "offsetTop") == 0
	
	, "Прокрутка"
	, SCROLL(1000)
	
	, "Меню смещено"
	, ONE("#menu", "offsetTop") > 0
	
	, "Меню кликабельно"
	, CLICK("#menu > * a", multi_selector=True)
	
	, tags = "scroll,menu"
)
