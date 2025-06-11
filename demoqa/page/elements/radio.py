from dsl import *

TEST["Radio Button"](
	URL("/radio-button")
	
	, "Yes"
	, CLICK("[1]::div.custom-control.custom-radio.custom-control-inline")
	, ONE("[1]::.custom-radio") == "Yes"
	
	, "Impressive"
	, CLICK("[2]::div.custom-control.custom-radio.custom-control-inline")
	, ONE("[2]::.custom-radio") == "Impressive"
	
	, "No"
	, ONE("#noRadio", "disabled") == True
	
	, tags = "radio,button"
)
