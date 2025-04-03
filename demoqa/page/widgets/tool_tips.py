from dsl import *

TEST["Tool Tips"](
	URL("/tool-tips")
	
	, "Кнопка"
	, HOVER("#toolTipButton")
	, ONE("#buttonToolTip") == "You hovered over the Button"
	
	, "Текстовое поле"
	, HOVER("#toolTipTextField")
	, ONE("#textFieldToolTip") == "You hovered over the text field"
	
	, "Ссылка"
	, HOVER("text::Contrary")
	, ANY("Contrary", "attr::aria-describedby") == "contraryTexToolTip"
	, ONE("[role=\"tooltip\"]") == "You hovered over the Contrary"
	
	, tags = "tooltip"
)
