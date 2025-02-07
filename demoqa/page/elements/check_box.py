from dsl import *

TEST["Check Box"](
	URL("/checkbox")
	, "Сворачивание / разворачивание"
	, CLICK("button.rct-option.rct-option-expand-all")
	, COUNT("span.rct-text") == 17
	, CLICK("button.rct-option.rct-option-collapse-all")
	, COUNT("span.rct-text") == 1
	
	, "Нажимаем"
	, CLICK("button.rct-option.rct-option-expand-all")
	, CLICK("[0]::span.rct-checkbox")
	
	, "Проверяем"
	, ALL("span.rct-title") == ['Home', 'Desktop', 'Notes', 'Commands', 'Documents', 'WorkSpace', 'React', 'Angular', 'Veu', 'Office', 'Public', 'Private', 'Classified', 'General', 'Downloads', 'Word File.doc', 'Excel File.doc']
	
	, tags = "button,form"
)
