from dsl import *

TEST["Simple button"](
	URL("/elements/button/simple")
	, "The user should be able to click the button."
	, CLICK("#submit-id-submit")
	
	, "After pressing the button, the user should be shown confirmation that the button was pressed."
	, ONE("#result-text") == "Submitted"
	
	, "The button should be labeled Click."
	, ONE("#submit-id-submit", "attr::value") == "Click"
	
	, tags="button"
	, single_thread=False
)

TEST["Looks like a button"](
	URL("/elements/button/like_a_button")
	, "The user should be able to click the button."
	, CLICK(".a-button")
	
	, "After pressing the button, the user should be shown confirmation that the button was pressed."
	, ONE("#result-text") == "Submitted"
	
	, "The button should be labeled Click."
	, ONE(".a-button") == "Click"
	
	, tags="button"
	, single_thread=False
)

TEST["Disabled"](
	URL("/elements/button/disabled")
	, "Submit button should be disabled by default."
	, ONE("#submit-id-submit", "disabled") == True
	
	, "User should be able to enable and then disable the button using the options of the Select state dropdown."
	, DATA("#id_select_state", "enabled")
	, ONE("#submit-id-submit", "disabled") == False
	, DATA("#id_select_state", "disabled")
	, ONE("#submit-id-submit", "disabled") == True
	
	, "After pressing the button, the user should be shown confirmation that the button was pressed."
	, DATA("#id_select_state", "enabled")
	, CLICK("#submit-id-submit")
	
	, ONE("#result-text") == "Submitted"
	
	, tags="button"
	, single_thread=False
)

