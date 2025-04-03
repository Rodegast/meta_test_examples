from dsl import *

TEST["Radio Button"](
	URL("/radio-button")
	
	, "Yes"
	, CLICK("[1]::div.custom-control.custom-radio.custom-control-inline")
	, ONE("p.mt-3>span") == "Yes"
	
	, "Impressive"
	, CLICK("[2]::div.custom-control.custom-radio.custom-control-inline")
	, ONE("p.mt-3>span") == "Impressive"
	
	, "No"
	, ONE("#noRadio", "disabled") == True
	
	, tags = "button"
)
