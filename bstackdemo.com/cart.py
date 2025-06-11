from dsl import *

SCRIPT["iPhone_XR_to_cart"](
	IF(PAGE_URL != CONFIG.BASE_URL, URL)
	, "Добавляем в корзину iPhone XR"
	, CLICK("[1]::span.checkmark")
	, DATA(".sort > select", "lowestprice")
	, ONE("[1]::.shelf-item__title") < "iPhone XR"  # Ждём окончания сортировки товаров
	, CLICK("[1]::Add to cart")
)

TEST["Товар в корзине"](
	SCRIPT("iPhone_XR_to_cart")
	
	, "Проверка товара корзине"
	, COUNT(".float-cart__shelf-container > .shelf-item") == 1
	, ONE(".desc") < "Quantity: 1"
	, ONE(".shelf-item__details") < "iPhone XR"
	, ONE(".float-cart__shelf-container .shelf-item__price") < "499.00"
	
	, "Товар удаляется из корзины"
	, CLICK(".shelf-item__del")
	, NOT(".float-cart__shelf-container > .shelf-item")
	
	, tags="cart"
)

TEST["Заказываем iPhone XR"](
	SCRIPT("login", "iPhone_XR_to_cart")
	
	, "Проверка формы заказа"
	, CLICK(".buy-btn")
	, ONE(".layout-cart") > ALL_LIST("iPhone XR", "499.00")
	
	, "Заполнение формы заказа"
	, DATA("#firstNameInput", "Владимир")
	, DATA("#lastNameInput", "Ульянов")
	, DATA("#addressLine1Input", "Красная пл., 1")
	, DATA("#provinceInput", "Москва")
	, DATA("#postCodeInput", "109012")
	
	, "Заказываем"
	, CLICK("#checkout-shipping-continue")
	, ONE("#confirmation-message") == "Your Order has been successfully placed."
	
	, "Можно скачать confirmation.pdf"
	, CLICK("#downloadpdf")
	, CHECK_DOWNLOAD("confirmation.pdf")
	
	, "Кнопка \"Continue Shopping\" перенаправляет на главную страницу"
	, CLICK(".continueButtonContainer > a")
	, PAGE_URL == CONFIG.BASE_URL
	
	, tags="cart"
)
