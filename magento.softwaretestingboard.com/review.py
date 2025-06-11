from dsl import *

TEST["Reviews"](
	URL
	, "Выбираем последний товар на странице"
	, CLICK("[0]::.product-item-link")
	
	, "Открываем вкладку с отзывами"
	, CLICK("#tab-label-reviews")
	# скрываем блок с отзывами что бы он не мешал вводу
	, DATA_ATTR("#product-review-container", "style", "display:none")
	
	, "Устанавливаем рейтинг"
	# смещаем клик на конец элемента
	, CLICK("#Rating_5_label", offset_x=WIDTH("#Rating_5_label")/2-16)
	, ONE("#Rating_5", "checked") == True
	
	, "Добавляем отзыв"
	, DATA("#nickname_field", "Meta Test")
	, DATA("#summary_field", "WaW")
	, DATA("#review_field", "5 star")
	, CLICK(".submit")
	, ONE(".page.messages") == "You submitted your review for moderation."
	
	, tags="review"
)
