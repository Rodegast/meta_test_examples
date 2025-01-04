from dsl import *

test = TEST["text-box"](
	URL("/text-box")
	, "Заполняем"
	, DATA("#userName", "scope::data/фио")
	, DATA("#userEmail", "scope::data/email")
	, DATA("#currentAddress", "scope::data/адрес1")
	, DATA("#permanentAddress", "scope::data/адрес2")
	, CLICK("#submit")
	
	, "Проверяем"
	, ONE("#name") == "Name:" + NP("data", "фио")
	, ONE("#email") == "Email:" + NP("data", "email")
	, ONE("p#currentAddress") == "Current Address :" + NP("data", "адрес1")
	, ONE("p#permanentAddress") == "Permananet Address :" + NP("data", "адрес2")
	, tags = "form"
)
#for x in range(100): test(nnn=x)
