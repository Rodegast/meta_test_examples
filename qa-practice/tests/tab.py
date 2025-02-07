from dsl import *

TEST["New tab link"](
	URL("/elements/new_tab/link")
	, "The link should open the page /elements/new_tab/new_page"
	, CLICK("#new-page-link")
	, PAGE_URL < "elements/new_tab/new_page"
	
	, "New page should be opened in a new tab"
	, ONE("#result-text") == "I am a new page in a new tab"
	, CLOSE
	, PAGE_URL < "elements/new_tab/link"
	
	, tags="tab"
	, single_thread=False
)

TEST["New tab button"](
	URL("/elements/new_tab/button")
	, "The button should open the page /elements/new_tab/new_page"
	, CLICK("#new-page-button")
	, PAGE_URL < "elements/new_tab/new_page"
	
	, "New page should be opened in a new tab"
	, ONE("#result-text") == "I am a new page in a new tab"
	, CLOSE
	, PAGE_URL < "elements/new_tab/button"
	
	, tags="tab"
	, single_thread=False
)
