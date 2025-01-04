from dsl import *

SCRIPT["datepicker"](
	CLICK("["+ARG("idx", default="0")+"]::.react-datepicker-wrapper")
	, DATA("select.react-datepicker__month-select", ARG("month"))
	, DATA("select.react-datepicker__year-select", ARG("year"))
	, CLICK("["+ARG("idx", default="0")+"]::.react-datepicker__day--0"+ARG("day"))
)

SCRIPT["react-datepicker"](
	CLICK("["+ARG("idx")+"]::.react-datepicker-wrapper")
	, CLICK(".react-datepicker__month-read-view--selected-month")
	, CLICK("//div[text()='"+ARG("month")+"']")
	, IF(ARG("year"), (
		CLICK(".react-datepicker__year-read-view--selected-year")
		, CLICK("//div[@class='react-datepicker__year-option' and text()='"+ARG("year")+"']")
	))
	, CLICK(ARG("day"))
	, CLICK(ARG("time"))
)
