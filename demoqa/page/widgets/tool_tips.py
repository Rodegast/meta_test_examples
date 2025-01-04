from dsl import *

TEST["Tool Tips"](
	URL("/tool-tips")
	, "Кнопка"
	, HOVER("#toolTipButton")
	, ONE("#buttonToolTip") == "You hovered over the Button"
	
	, "Текстовое поле"
	, HOVER("#toolTipTextField")
	, ONE("#textFieldToolTip") == "You hovered over the text field"
	, tags = "tool"
)
