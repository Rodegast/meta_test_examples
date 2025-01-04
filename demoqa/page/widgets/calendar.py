from dsl import *

TEST["Select Date"](
	URL("/date-picker")
##	, ARG("idx", 0)
##	, ARG("day", "31")
##	, ARG("month", 11)
##	, ARG("year", "1999")
##	, SCRIPT("datepicker")
	, SCRIPT("datepicker", idx=0, day="31", month=11, year="1999")
	, ONE("#datePickerMonthYearInput") == "12/31/1999"
	, tags="widget,calendar"
	, active=False
)

TEST["Select Date"](
	URL("/date-picker")
	, CLICK("[0]::.react-datepicker-wrapper")
	, DATA("select.react-datepicker__month-select", 0, wait_timeout=0)
	, DATA("select.react-datepicker__year-select", "1990", wait_timeout=0)
	, CLICK("[0]::.react-datepicker__day--001")
	, ONE("#datePickerMonthYearInput") == "01/01/1990"
	, tags="widget,calendar"
	, active=False
)

TEST["Select date-time"](
	URL("/date-picker")
	, SCRIPT("react-datepicker", idx=1, day="31", month="December", time="12:00", year=2022)
	, ONE("#dateAndTimePickerInput", "attr::value") == "December 31, 2022 12:00 PM"
	, tags="widget,calendar"
)
