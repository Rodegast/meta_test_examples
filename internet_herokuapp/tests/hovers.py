from dsl import *

TEST["Hovers"](
	URL("/hovers")
	
	, "Проверка первой картинки"
	, ONE("[1]::.figcaption", "css::display") == "none"
	, HOVER("[1]::div .figure")
	, ONE("[1]::.figcaption", "css::display") == "block"
	
	, "Проверка второй картинки"
	, ONE("[2]::.figcaption", "css::display") == "none"
	, HOVER("[2]::div .figure")
	, ONE("[2]::.figcaption", "css::display") == "block"
	
	, "Проверка третьей картинки"
	, ONE("[3]::.figcaption", "css::display") == "none"
	, HOVER("[3]::div .figure")
	, ONE("[3]::.figcaption", "css::display") == "block"
	
	, tags = "hover"
)
