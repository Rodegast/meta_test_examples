from dsl import *

TEST["Nested Frames"](
	URL("/nested_frames")
	
	, "Проверяем тескт в фрейме BOTTOM"
	, ONE(FP("name::frame-bottom", "body")) == "BOTTOM"
	
	, "Проверяем тескт в фрейме LEFT"
	, FRAME("name::frame-top", "name::frame-left")
	, ONE("body") == "LEFT"
	, FRAME
	
	, "Проверяем тескт в фрейме MIDDLE"
	, FRAME("name::frame-top", "name::frame-middle")
	, ONE("#content") == "MIDDLE"
	, FRAME
	
	, "Проверяем тескт в фрейме RIGHT"
	, FRAME("name::frame-top", "name::frame-right")
	, ONE("body") == "RIGHT"
	
	, tags = "frame"
)

TEST["iFrames"](
	URL("/iframe")
	, "Закрываем предупреждение редактора"
	, CLICK(".tox-notifications-container >* button")
	
	, "Проверка текста в редакторе"
	, ONE(FP("#mce_0_ifr", "#tinymce")) == "Your content goes here."
	
	, tags = "frame"
)
