from dsl import *

TEST["Buttons"](
	URL("/buttons")
	
	, "You have done a dynamic click"
	, CLICK("text::Click Me")
	, ONE("#dynamicClickMessage") == "You have done a dynamic click"
	
	, "You have done a right click"
	, RIGHT_CLICK("#rightClickBtn")
	, ONE("#rightClickMessage") == "You have done a right click"
	
	, "You have done a double click"
	, DOUBLE_CLICK("#doubleClickBtn")
	, ONE("#doubleClickMessage") == "You have done a double click"
	
	, tags = ["button", "mouse_button"]
)
