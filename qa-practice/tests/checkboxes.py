from dsl import *

TEST["Single checkbox"](
	URL("/elements/checkbox/single_checkbox")
	, "There should be one checkbox on the page"
	, ONE("//*[@type=\"checkbox\"]")
	
	, "The label of the checkbox should be \"Select me or not\""
	, ONE("//*[@for=\"id_checkbox_0\"]") == "Select me or not"
	
	, "The Submit button should always be enabled"
	, ONE("#submit-id-submit", "disabled") == False
	, CLICK("#id_checkbox_0")
	, ONE("#submit-id-submit", "disabled") == False
	
	, "if a checkbox has been selected, the name of the selected checkbox is displayed to the user"
	, CLICK("#submit-id-submit")
	, ONE("#result-text") == "select me or not"
	
	, "if the checkbox was not selected, then the result is not displayed"
	, CLICK("#submit-id-submit")
	, NOT("#result-text")
	
	, tags="checkboxes"
	, single_thread=False
)

TEST["Checkboxes"](
	URL("/elements/checkbox/mult_checkbox")
	, "There should be three checkboxes on the page."
	, COUNT("//*[@type=\"checkbox\"]")
	
	, "The label of the checkboxes should be: One, Two, Three"
	, ONE("//*[@for=\"id_checkboxes_0\"]") == "One"
	, ONE("//*[@for=\"id_checkboxes_1\"]") == "Two"
	, ONE("//*[@for=\"id_checkboxes_2\"]") == "Three"
	
	, "The Submit button should always be enabled"
	, CLICK("#id_checkboxes_0")
	, ONE("#submit-id-submit", "disabled") == False
	, CLICK("#id_checkboxes_1")
	, ONE("#submit-id-submit", "disabled") == False
	, CLICK("#id_checkboxes_2")
	, ONE("#submit-id-submit", "disabled") == False
	
	, "if a checkbox has been selected, the name(s) of the selected checkbox(es) is(are) displayed to the user"
	, CLICK("#submit-id-submit")
	, ONE("#result-text") == "one, two, three"
	
	, "if no checkbox was selected, then the result is not displayed"
	, CLICK("#submit-id-submit")
	, NOT("#result-text")
	
	, tags="checkboxes"
	, single_thread=False
)
