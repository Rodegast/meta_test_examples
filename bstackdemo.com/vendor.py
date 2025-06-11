from dsl import *

TEST["Проверка фильтра производителей (одиночный выбор)"](
	URL
	
	, "При выборе Apple только телефоны iPhone"
	, CLICK("[1]::span.checkmark")
	, ALL(".shelf-item__title") < "iPhone"
	, CLICK("[1]::span.checkmark")
	
	, "При выборе Samsung только телефоны Galaxy"
	, CLICK("[2]::span.checkmark")
	, ALL(".shelf-item__title") < "Galaxy"
	, CLICK("[2]::span.checkmark")
	
	, "При выборе Google только телефоны Pixel"
	, CLICK("[3]::span.checkmark")
	, ALL(".shelf-item__title") < "Pixel"
	, CLICK("[3]::span.checkmark")
	
	, "При выборе OnePlus только телефоны One Plus"
	, CLICK("[4]::span.checkmark")
	, ALL(".shelf-item__title") < "One Plus"
	, CLICK("[4]::span.checkmark")
	
	, tags="vendor"
)

TEST["Проверка фильтра производителей (множественный выбор)"](
	URL
	, "Выбор Apple"
	, CLICK("[1]::span.checkmark")
	, ALL(".shelf-item__title") < "iPhone"
	
	, "Выбор Apple + Samsung"
	, CLICK("[2]::span.checkmark")
	, ALL(".shelf-item__title") < ANY_LIST("iPhone", "Galaxy")
	
	, "Выбор Apple + Samsung + Google"
	, CLICK("[3]::span.checkmark")
	, ALL(".shelf-item__title") < ANY_LIST("iPhone", "Galaxy", "Pixel")
	
	, "Выбор Samsung + Google + OnePlus"
	, CLICK("[4]::span.checkmark")
	, CLICK("[1]::span.checkmark")
	, ALL(".shelf-item__title") < ANY_LIST("Galaxy", "Pixel", "One Plus")
	
	, tags="vendor"
)
