from dsl import *


TEST["browser-windows"](
	URL("/browser-windows")
	
	, "New Tab"
	, CLICK("#tabButton")
	, ONE("h1") == "This is a sample page"
	, WINDOW
	
	, "New Window"
	, CLICK("#windowButton")
	, ONE("#sampleHeading") == "This is a sample page"
	, WINDOW
	
	, "New Window Message"
	, CLICK("#messageWindowButton")
	, ONE("body") == "Knowledge increases by sharing but not by saving. Please share this website with your friends and in your organization."
	
	, "Закрываем"
	, CLOSE
	
	, WINDOW
	, CLOSE
	
	, WINDOW
	, CLOSE
	
	, browser="firefox"
	, tags = "window"
)
