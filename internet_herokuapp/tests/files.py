import os
from dsl import *

TEST["File Download"](
	URL("/download")
	
	, "Проверяем скачивание файла по первой ссылке"
	, CLICK("[1]::.example > a")
	, CHECK_DOWNLOAD(ONE("[1]::.example > a"))
	
	, tags = "files,download"
)

TEST["File Uploader"](
	URL("/upload")
	, UPLOAD("#file-upload", "scope::resurs/kote.jpg")
	, CLICK("#file-submit")
	, ONE("#uploaded-files") == "kote.jpg"
	
	, tags = "files,upload"
)
