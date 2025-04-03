from dsl import *

TEST["Links"](
	URL("/links")
	, "Home"
	, CLICK("#simpleLink")
	, PAGE_URL == CONFIG.BASE_URL
	, CLOSE
	
	, "Created"
	, CLICK("#created")
	, ONE("[1]::#linkResponse > b") == "201"
	
	, "No Content"
	, CLICK("#no-content")
	, ONE("[1]::#linkResponse > b") == "204"
	
	, "Moved Permanently"
	, CLICK("#moved")
	, ONE("[1]::#linkResponse > b") == "301"
	
	, "Bad Request"
	, CLICK("#bad-request")
	, ONE("[1]::#linkResponse > b") == "400"
	
	, "Unauthorized"
	, CLICK("#unauthorized")
	, ONE("[1]::#linkResponse > b") == "401"
	
	, "Forbidden"
	, CLICK("#forbidden")
	, ONE("[1]::#linkResponse > b") == "403"
	
	, "Not Found"
	, CLICK("#invalid-url")
	, ONE("[1]::#linkResponse > b") == "404"
	
	, tags = "links"
)
