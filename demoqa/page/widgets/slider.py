from dsl import *

TEST["Слайдер"](
	URL("/slider")
	
	, ARG("1%", WIDTH(".range-slider__wrap") / 100)
	
	, "Начальное положение 25%"
	, ONE(".range-slider__wrap") == "25"
	
	, "Середина 50%"
	, CLICK(".range-slider__wrap")
	, ONE(".range-slider__wrap") == "50"
	
	, "Начало 0%"
	, CLICK(".range-slider__wrap", offset_x=(-50 * ARG("1%")))
	, ONE(".range-slider__wrap") == "0"
	
	, "Конец 100%"
	, CLICK(".range-slider__wrap", offset_x=(50 * ARG("1%")))
	, ONE(".range-slider__wrap") == "100"
	
	, tags="slider"
)
