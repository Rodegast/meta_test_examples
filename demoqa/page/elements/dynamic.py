from dsl import *

TEST["This text has random Id"](
	URL("/dynamic-properties")
	, NOT("#enableAfter", "disabled", wait_timeout=5)
	, tags = "button,dinamic"
)

TEST["Color Change"](
	URL("/dynamic-properties")
	, ONE("#colorChange", "css::color", wait_timeout=5) != "rgba(255, 255, 255, 1)"
	, tags = "button,dinamic"
)

TEST["Visible After 5 Seconds"](
	URL("/dynamic-properties")
	, ONE("#visibleAfter", wait_timeout=5)
	, tags = "button,dinamic"
)
