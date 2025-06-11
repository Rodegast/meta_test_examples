from dsl import *

start_data = "todo"*25
input_data = "123"

TEST["react-todo"](
	URL("/examples/react/dist/")
	
	, "Ввод первого TODO"
	, DATA("#todo-input", start_data, press="ENTER")
	
	, "Редактирование"
	, DOUBLE_CLICK("label[data-testid='todo-item-label']")
	, DATA("[2]::#todo-input", input_data, press="ENTER")
	, ALL("label[data-testid='todo-item-label']") == input_data
	
	, "Отметка завершения"
	, CLICK("input[data-testid=\"todo-item-toggle\"]")
	, ONE("li[data-testid=\"todo-item\"]", "classList") < "completed"
	
	, "Удаление"
	, CLICK("button.destroy")
	, NOT("li[data-testid=\"todo-item\"]")
	
	, test_id="react"
)

TEST["react-redux-todo"](
	URL("/examples/react-redux/dist/")
	
	, "Ввод первого TODO"
	, DATA("input[data-testid=\"text-input\"]", start_data, press="ENTER")
	
	, "Редактирование"
	, DOUBLE_CLICK("label[data-testid='todo-item-label']")
	, DATA("input.edit", input_data, press="ENTER")
	, ALL("label[data-testid='todo-item-label']") == input_data
	
	, "Отметка завершения"
	, CLICK("input[data-testid=\"todo-item-toggle\"]")
	, ONE("li[data-testid=\"todo-item\"]", "classList") < "completed"
	
	, "Удаление"
	, CLICK("button.destroy")
	, NOT("li[data-testid=\"todo-item\"]")
	
	, test_id="redux"
)

TEST["vue-todo"](
	URL("/examples/vue/dist/")
	
	, "Ввод первого TODO"
	, DATA(".new-todo", start_data, press="ENTER")
	
	, "Редактирование"
	, DOUBLE_CLICK("[1]::.view > label")
	, DATA("#edit-todo-input", input_data, press="ENTER")
	, ALL("[1]::.view > label") == input_data
	
	, "Отметка завершения"
	, CLICK("[1]::.view > input.toggle")
	, ONE("[1]::ul.todo-list > li", "classList") < "completed"
	
	, "Удаление"
	, CLICK("[1]::button.destroy")
	, NOT("ul.todo-list > li")
	
	, test_id="vue"
)

TEST["preact-todo"](
	URL("/examples/preact/dist/")
	
	, "Ввод первого TODO"
	, DATA("pht::What needs to be done?", start_data, press="ENTER")
	
	, "Редактирование"
	, DOUBLE_CLICK("[1]::.view > label")
	, DATA("#edit-todo-input", input_data, press="ENTER")
	, ALL("[1]::.view > label") == input_data
	
	, "Отметка завершения"
	, CLICK("[1]::input.toggle")
	, ONE("[1]::ul.todo-list > li", "classList") < "completed"
	
	, "Удаление"
	, CLICK("[1]::button.destroy")
	, NOT("li[data-testid=\"todo-item\"]")
	
	, test_id="preact"
)

TEST["backbone-todo"](
	URL("/examples/backbone/dist/")
	
	, "Ввод первого TODO"
	, DATA("pht::What needs to be done?", start_data, press="ENTER")
	
	, "Редактирование"
	, DOUBLE_CLICK("[1]::.view > label")
	, DATA("[1]::input.edit", input_data, press="ENTER")
	, ALL("[1]::.view > label") == input_data
	
	, "Отметка завершения"
	, CLICK("[1]::input.toggle")
	, ONE("[1]::ul.todo-list > li", "classList") < "completed"
	
	, "Удаление"
	, CLICK("[1]::button.destroy")
	, NOT("li[data-testid=\"todo-item\"]")
	
	, test_id="backbone"
)

TEST["angular-todo"](
	URL("/examples/angular/dist/browser/")
	
	, "Ввод первого TODO"
	, DATA("pht::What needs to be done?", start_data, press="ENTER")
	
	, "Редактирование"
	, DOUBLE_CLICK("[1]::.view > label")
	, DATA("#edit-todo-input", input_data, press="ENTER")
	, ALL("[1]::.view > label") == input_data
	
	, "Отметка завершения"
	, CLICK("[1]::input.toggle")
	, ONE("[1]::.view > label", "css::text-decoration") < "line-through"
	
	, "Удаление"
	, CLICK("[1]::button.destroy")
	, NOT("[1]::ul.todo-list > app-todo-item")
	
	, test_id="angular"
)

TEST["jquery-todo"](
	URL("/examples/jquery/dist/")
	
	, "Ввод первого TODO"
	, DATA("pht::What needs to be done?", start_data, press="ENTER")
	
	, "Редактирование"
	, DOUBLE_CLICK("[1]::.view > label")
	, DATA("li.editing > input.edit", input_data, press="ENTER")
	, ALL("[1]::.view > label") == input_data
	
	, "Отметка завершения"
	, CLICK("[1]::input.toggle")
	, ONE("[1]::.view > label", "css::text-decoration") < "line-through"
	
	, "Удаление"
	, CLICK("[1]::button.destroy")
	, NOT("[1]::ul.todo-list > app-todo-item")
	
	, test_id="jquery"
)
