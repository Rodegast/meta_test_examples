from dsl import *

##TEST["Alerts"](
##	URL("/alerts")
##	
##	, "Click Button to see alert"
##	, CLICK("#alertButton")
##	, ALERT_TEXT == "You clicked a button"
##	, ALERT_CLOSE
##	
##	
##	, browser= "firefox"
##	, tags = "alert"
##)
