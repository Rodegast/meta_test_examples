from dsl import *

TEST["DND"](
	URL("/drag_and_drop")
	
	, "Проверка позиции элементов"
	, ALL("#columns > .column") == ["A", "B"]
	
	, "Меняем местами элементы A и B"
	, DND("#column-a", 200)
	, ALL("#columns > .column") == ["B", "A"]
	
	, "Возвращает элементы A и B на прежние места"
	, DND("#column-a", "#column-b")
	, ALL("#columns > .column") == ["A", "B"]
	
	, tags = "dnd"
)
