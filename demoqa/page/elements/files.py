import os
from dsl import *

TEST["Закачка"](
	URL("/upload-download")
	, UPLOAD("#uploadFile", "scope::data/image")
	, ONE("#uploadedFilePath") == "C:\\fakepath\\"+NP("data", "image_name")
	
	, tags="file"
)

TEST["Загрузка"](
	URL("/upload-download")
	, CLICK("#downloadButton")
	, CHECK_DOWNLOAD("sampleFile.jpeg", "24c004606d9c7a2a2f0a4d1b69562c3e")
	, CHECK_DOWNLOAD("sampleFile.jpeg", 4096)
	
	, tags="file"
)
