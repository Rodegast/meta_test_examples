from dsl import *

SCRIPT["in_element"]( # проверяем что элемент "internal" находитсяв нутри элемента "external"
	POS_X(ARG("external")) < POS_X(ARG("internal"))
	, POS_X(ARG("external")) + WIDTH(ARG("external")) > POS_X(ARG("internal"))
	, POS_Y(ARG("external")) < POS_Y(ARG("internal"))
	, POS_Y(ARG("external")) + HEIGHT(ARG("external")) > POS_Y(ARG("internal"))
)
