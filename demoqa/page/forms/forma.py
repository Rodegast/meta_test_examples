from dsl import *

TEST["Practice Form"](
	URL("/automation-practice-form")
	, STEP["Заполнение"](
		"Name"
		, DATA("#firstName", "scope::data/фамилия")
		, DATA("#lastName", "scope::data/имя")
		
		, "Email"
		, DATA("#userEmail", "scope::data/email")
		
		, "Gender"
		, CLICK("[1]::.custom-control.custom-radio.custom-control-inline")
		
		, "Mobile"
		, DATA("#userNumber", "scope::data/mobile")
		
		, "Date of Birth"
		, SCRIPT("datepicker", day=31, month="11", year="1999")
		
		, "Subjects"
		, DATA("#subjectsInput", "Physics")
		, KEY("#subjectsInput", "ENTER")
		
		, "Hobbies"
		, CLICK("Sports")
		
		, "Picture"
		, UPLOAD("#uploadPicture", "scope::data/image")
		
		, "Current Address"
		, DATA("#currentAddress", "scope::data/address")
		
		, "State and City"
		, CLICK("#state")
		, CLICK("Haryana")
		, CLICK("#city")
		, CLICK("Panipat")
	), STEP["Проверка"](
		CLICK("#submit")
		, ALL("tr > td") == [
			"Student Name", NP("data", "фамилия") + " " + NP("data", "имя")
			, "Student Email", "scope::data/email"
			, "Gender", "Male"
			, "Mobile", "scope::data/mobile"
			, "Date of Birth", "31 December,1999"
			, "Subjects", "Physics"
			, "Hobbies", "Sports"
			, "Picture", "scope::data/image_name"
			, "Address", "scope::data/address"
			, "State and City", "Haryana Panipat"
	])
	, tags = ["student", "form"]
)
