from dsl import *

TEST["Slider"](
	URL("/horizontal_slider")
	
	, "Центр"
	, CLICK("input")
	, ONE("#range") == 2.5
	
	, "Левый край"
	, CLICK("input", offset_x=WIDTH("input")/-2)
	, ONE("#range") == 0
	
	, "Правый край"
	, CLICK("input", offset_x=WIDTH("input")/2)
	, ONE("#range") == 5
	
	, tags="form,slider"
)

TEST["Login Page"](
	URL("/login")
	
	, "Логин без заполненных данных"
	, CLICK("button")
	, ONE("#flash-messages") << "Your username is invalid!"
	
	, "Логин под некорректным паролем"
	, DATA("#username", "tomsmith")
	, DATA("#password", "password")
	, CLICK("button")
	, ONE("#flash-messages") << "Your password is invalid!"
	
	, "Логин под некорректным именем"
	, DATA("#username", "username")
	, DATA("#password", "SuperSecretPassword!")
	, CLICK("button")
	, ONE("#flash-messages") << "Your username is invalid!"
	
	, "Удачный логин пользователя"
	, DATA("#username", "tomsmith")
	, DATA("#password", "SuperSecretPassword!")
	, CLICK("button")
	, ONE("#flash-messages") << "You logged into a secure area!"
	
	, "Выход"
	, CLICK("a.button")
	, ONE("#flash-messages") << "You logged out of the secure area!"
	
	, tags="form,login"
)

TEST["Add/Remove Elements"](
	URL("/add_remove_elements/")
	
	, "Добавляем 3 элемента"
	, CLICK("div.example > button")
	, CLICK("div.example > button")
	, CLICK("div.example > button")
	, COUNT("#elements > button") == 3
	
	, "Удаляем элементы"
	, CLICK("#elements > button", multi_selector=True)
	, NOT("#elements > button")
	
	, tags="form,element"
)

TEST["Dropdown List"](
	URL("/dropdown")
	
	, "Option 1"
	, DATA("#dropdown", 1)
	, ONE("#dropdown > option[selected=\"selected\"]", "value") == "1"
	
	, "Option 2"
	, DATA("#dropdown", 2)
	, ONE("#dropdown > option[selected=\"selected\"]", "value") == "2"
	
	, tags="form,dropdown"
)
