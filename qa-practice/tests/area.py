from dsl import *

TEST["Textarea"](
	URL("/elements/textarea/single")
	
	, "Field name is \"Text area\""
	, ONE("//label[@for=\"id_text_area\"]") == "Text area*"
	
	, "This is a required field"
	, ONE("#id_text_area", "required") == True
	
	, "User should be able to enter any text into this field"
	, DATA("#id_text_area", "Text")
	
	, "The result can be sent using the Submit button"
	, CLICK("#submit-id-submit")
	
	, "After submitting the form, the text entered by the user is displayed on the page"
	, ONE("#result-text") == "Text"
	
	, tags="area"
)

TEST["Multiple textareas"](
	URL("/elements/textarea/textareas")
	
	, "There should be 3 fields"
	, ONE("//label[@for=\"id_first_chapter\"]")  == "First chapter*"
	, ONE("//label[@for=\"id_second_chapter\"]") == "Second chapter"
	, ONE("//label[@for=\"id_third_chapter\"]")  == "Third chapter"
	
	, "The field First chapter is required"
	, ONE("#id_first_chapter", "required") == True
	
	, "User should be able to enter any text in each field"
	, DATA("#id_first_chapter", "First")
	, DATA("#id_second_chapter", "Second")
	, DATA("#id_third_chapter", "Third")
	
	, "The result can be sent using the Submit button"
	, CLICK("#submit-id-submit")
	
	, "After submitting the form, the text entered by the user into all fields is displayed on the page"
	, ONE("#result-text", "innerText") == "First\nSecond\nThird"
	
	, tags="area"
)
