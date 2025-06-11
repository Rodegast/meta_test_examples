from dsl import *

TEST["Keys"](
	URL("/key_presses")
	
	, "TAB"
	, KEY("#target", KEY.TAB)
	, ONE("#result") == "You entered: TAB"
	
	, "F"
	, KEY("#target", "f")
	, ONE("#result") == "You entered: F"
	
	, tags="key,input"
)

TEST["Number"](
	URL("/inputs")
	
	, "Ввод цифр с клавиатуры"
	, DATA("input", "123")
	, ONE("input") == "123"
	
	, "Выбор цифр"
	, CLEAR("input")
	, KEY("input", KEY.UP)
	, ONE("input") == "1"
	
	, tags="number,input"
)
