from dsl import *

TEST["Small Modal"](
	URL("/modal-dialogs")
	, CLICK("#showSmallModal")
	, ONE("div.modal-content")
	, CLICK("#closeSmallModal")
	, NOT("div.modal-content")
	, tags = "modal,dialogs"
)

TEST["Large Modal"](
	URL("/modal-dialogs")
	, CLICK("#showLargeModal")
	, ONE("div.modal-content")
	, CLICK("button.close")
	, NOT("div.modal-content")
	, tags = "dialogs,modal"
)
