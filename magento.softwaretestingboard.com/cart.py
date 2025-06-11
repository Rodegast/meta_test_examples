from dsl import *

TEST["Добавляем товар в корзину и удаляем его"](
	URL
	, STEP["Выбор товара"](
		CLICK("link::Hero Hoodie")
		, "Размер XL"
		, CLICK("#option-label-size-143-item-170")
		, "Цвет чёрный"
		, CLICK("#option-label-color-93-item-49")
	)
	, "Добавляем товар в корину"
	, CLICK("#product-addtocart-button")
	, ONE(".counter-number") == 1
	
	, "Открываем диалог корзины и удаляем товар"
	, CLICK(".showcart")
	, CLICK(".delete")
	, CLICK(".action-accept")
	, ONE(".subtitle.empty") == "You have no items in your shopping cart."
	
	, "Закрываем диалог корзины"
	, CLICK("#btn-minicart-close")
	, NOT("#ui-id-1")
	
	, tags="cart"
)

