from dsl import *

TEST["Проверка страниц при переходе из меню"](
	URL
	
	, "What's New"
	, CLICK("#ui-id-3")
	, PAGE_TITLE == "What's New"
	, PAGE_URL <= "what-is-new.html"
	
	, "Women -> Top -> Jackets"
	, HOVER("#ui-id-4")
	, HOVER("#ui-id-9")
	, CLICK("#ui-id-11")
	, PAGE_TITLE == "Jackets - Tops - Women"
	, PAGE_URL <= "women/tops-women/jackets-women.html"
	
	, "Men -> Top -> Jackets"
	, HOVER("#ui-id-5")
	, HOVER("#ui-id-17")
	, CLICK("#ui-id-19")
	, PAGE_TITLE == "Jackets - Tops - Men"
	, PAGE_URL <= "men/tops-men/jackets-men.html"
	
	, "Gear -> Bags"
	, HOVER("#ui-id-6")
	, CLICK("#ui-id-25")
	, PAGE_TITLE == "Bags - Gear"
	, PAGE_URL <= "gear/bags.html"
	
	, "Training -> Download"
	, HOVER("#ui-id-7")
	, CLICK("#ui-id-28")
	, PAGE_TITLE == "Video Download - Training"
	, PAGE_URL <= "training/training-video.html"
	
	, "Sale"
	, CLICK("#ui-id-8")
	, PAGE_TITLE == "Sale"
	, PAGE_URL <= "sale.html"
	
	, tags="menu"
)
