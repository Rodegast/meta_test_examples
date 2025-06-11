from dsl import *

TEST["Избранное"](
	URL
	, SCRIPT("login")
	
	, "Список избранного пуст"
	, CLICK("#favourites")
	, COUNT(".shelf-item") == 0
	
	, "Выбираем первый телефон"
	, URL
	, ARG("favorit", ONE("[1]::.shelf-item"))
	, CLICK(["[1]::.shelf-item", "button"])
	, ONE(["[1]::.shelf-item", "button"], "classList") < "clicked"
	
	, "Проверяем телефон в списке избранного"
	, CLICK("#favourites")
	, COUNT(".shelf-item") == 1
	, ONE("[1]::.shelf-item") == ARG("favorit")
	
	, "Отменяем выбор телефона"
	, CLICK(["[1]::.shelf-item", "button"])
	
	, "Телефон больше не в списке"
	, COUNT(".shelf-item") == 0
	, URL
	, ~(ONE(["[1]::.shelf-item", "button"], "classList") < "clicked")
	
	, tags = "favorit"
)
