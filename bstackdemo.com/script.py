from dsl import *

SCRIPT["login"](
	"Вход под учётной записью demouser"
	, CLICK("#signin")
	, DATA("#username input", "demouser", press=KEY.ENTER, click=False)
	, DATA("#password input", "testingisfun99", press=KEY.ENTER, click=False)
	, CLICK("#login-btn")
)
