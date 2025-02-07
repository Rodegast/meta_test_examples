from dsl import *

TEST["Single select"](
	URL("/elements/select/single_select")
	, "Field name is \"Choose language\""
	, ONE("//label[@for=\"id_choose_language\"]") == "Choose language*"
	
	, "This is a required field"
	, ONE("#id_choose_language", "required") == True
	
	, "The result can be sent using the Submit button"
	, DATA("#id_choose_language", "Python")
	, CLICK("#submit-id-submit")
	
	, "After submitting the form, the option selected by the user is displayed on the page"
	, ONE("#result-text") == "Python"
	
	, tags="select"
	, single_thread=False
)

TEST["Multiple selects"](
	URL("/elements/select/mult_select")
	, "There should be 3 fields, All the fields are required"
	, ONE("#id_choose_when_you_want_to_go", "required") == True
	, ONE("#id_choose_the_place_you_want_to_go", "required") == True
	, ONE("#id_choose_how_you_want_to_get_there", "required") == True
	
	, "User should be able to select any option in each field"
	, DATA("#id_choose_the_place_you_want_to_go", "Sea")
	, DATA("#id_choose_how_you_want_to_get_there", "Car")
	, DATA("#id_choose_when_you_want_to_go", "Today")
	
	, "The result can be sent using the Submit button"
	, CLICK("#submit-id-submit")
	
	, "After submitting the form, the option selected by the user should be placed into the resulting phrase and displayed to the user"
	, ONE("#result-text") == "to go by car to the sea today"
	
	, tags="select"
	, single_thread=False
)
