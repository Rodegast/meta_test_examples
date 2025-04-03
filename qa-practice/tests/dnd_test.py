from dsl import *

rect_droppable = "#rect-droppable"
rect_fixed     = "#rect-draggable"

TEST["Boxes"](
	URL("/elements/dragndrop/boxes")
	
	, "There should be two squares on the page"
	, ONE(rect_droppable)
	, ONE(rect_fixed)
	
	, "The bottom square must be draggable"
	, ONE(rect_fixed, "attr::class") < "ui-draggable-handle"
	
	, "When dragging the bottom square to the top one, the text \"Dropped!\" should appear in the top square."
	, DND(rect_fixed, rect_droppable)
	, ONE("#text-droppable") == "Dropped!"
	
	, "The bottom square can only be dragged once"
	, ONE(rect_droppable, "attr::class") < "ui-state-highlight"
	, DND(rect_fixed, "#req_header")
	, SCRIPT("in_element", external=rect_droppable, internal=rect_fixed)
	
	, tags="dnd"
)

droppable1 = "#rect-droppable1"
droppable2 = "#rect-droppable2"

TEST["Images"](
	URL("elements/dragndrop/images")
	
	, "There should be two squares on the page"
	, ONE(droppable1)
	, ONE(droppable2)
	
	, "There should be a smiley in the bottom square"
	, SCRIPT("in_element", external=droppable1, internal="//img[@src='/static/home/smile.png']")
	
	, "When dropping the smiley into any of the squares, the text is \"Dropped!\" should appear in this square"
	, DND(droppable1, droppable2)
	, ONE("#rect-droppable2 .text-droppable") == "Dropped!"
	
	, DND(droppable2, droppable1)
	, ONE("#rect-droppable1 .text-droppable") == "Dropped!"
	
	, tags="dnd"
)

