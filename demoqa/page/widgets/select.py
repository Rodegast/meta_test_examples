from dsl import *

TEST["Select Value"](
	URL("/select-menu")
	, "Выбор"
	, CLICK("#withOptGroup")
	, CLICK("#react-select-2-option-2")
	, CLICK("h1")
	, "Проверка"
	, ONE("#withOptGroup") == "A root option"
	, tags = "select"
)

TEST["Select One"](
	URL("/select-menu")
	, "Выбор"
	, CLICK("#selectOne")
	, CLICK("#react-select-3-option-0-4")
	, CLICK("h1")
	, ONE("#selectOne") == "Prof."
	, tags = "select"
)

TEST["Old Style Select Menu"](
	URL("/select-menu")
	, "Выбор"
	, DATA("#oldSelectMenu", "2")
	, ONE("#oldSelectMenu") == "2"
	, tags = "select"
)

TEST["Standard multi select"](
	URL("/select-menu")
	, "Выбор"
	, DATA("#cars", [0, 2])
	, ONE("option[value='volvo']", "selected") == True
	, ONE("option[value='saab']", "selected")  == False
	, ONE("option[value='opel']", "selected")  == True
	, ONE("option[value='audi']", "selected")  == False
	, tags = "select"
)
