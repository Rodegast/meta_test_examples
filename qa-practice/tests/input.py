from dsl import *

text_fild = "#id_text_string"

TEST["Text input"](
	URL("/elements/input/simple")
	, "This is a required field"
	, ONE(text_fild, "required") == True
	
	, "Max: 25 characters"
	, DATA(text_fild, "1"*30)
	, KEY(text_fild, "ENTER")
	, ONE("#error_1_id_text_string") == "Please enter no more than 25 characters"
	
	, "Min: 2 characters"
	, DATA(text_fild, "1")
	, KEY(text_fild, "ENTER")
	, ONE("#error_1_id_text_string") == "Please enter 2 or more characters"
	
	, "After submitting the form, the text entered by the user is displayed on the page"
	, DATA(text_fild, "123")
	, KEY(text_fild, "ENTER")
	, ONE("#result-text") == "123"
	
	, tags="intput"
	, single_thread=False
)

TEST["Text input"](
	URL("/elements/input/email")
	, "Entered text should be a valid email address"
	, DATA("#id_email", "123")
	, KEY("#id_email", "enter")
	, ONE("#error_1_id_email") == "Enter a valid email address."
	
	, "After submitting the form, the text entered by the user is displayed on the page"
	, DATA("#id_email", "user@examaple.com")
	, KEY("#id_email", "enter")
	, ONE("#result-text") == "user@examaple.com"
	
	, tags="intput"
	, single_thread=False
)

TEST["Password field"](
	URL("/elements/input/passwd")
	, "Has minimum 8 characters in length"
	, DATA("#id_password", "123")
	, KEY("#id_password", "enter")
	, ONE("#error_1_id_password") == "Low password complexity"
	
	, "At least one uppercase English letter"
	, DATA("#id_password", "a#123456789")
	, KEY("#id_password", "enter")
	, ONE("#error_1_id_password") == "Low password complexity"
	
	, "At least one lowercase English letter"
	, DATA("#id_password", "A#123456789")
	, KEY("#id_password", "enter")
	, ONE("#error_1_id_password") == "Low password complexity"
	
	, "At least one special character"
	, DATA("#id_password", "Aa123456789")
	, KEY("#id_password", "enter")
	, ONE("#error_1_id_password") == "Low password complexity"
	
	, "After submitting the form, the text entered by the user is displayed on the page"
	, DATA("#id_password", "Aa#123456789")
	, KEY("#id_password", "enter")
	, ONE("#result-text") == "Aa#123456789"
	
	, tags="intput"
	, single_thread=False
)
