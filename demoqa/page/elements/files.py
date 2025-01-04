import os
from dsl import *

TEST["Закачка"](
	URL("/upload-download")
	, UPLOAD("#uploadFile", __file__)
	, ONE("#uploadedFilePath") == "C:\\fakepath\\"+os.path.basename(__file__)
	, tags="file1"
)

TEST["Загрузка"](
	URL("/upload-download")
	, CLICK("#downloadButton")
	, CHECK_DOWNLOAD("sampleFile.jpeg", "24c004606d9c7a2a2f0a4d1b69562c3e")
	, CHECK_DOWNLOAD("sampleFile.jpeg", 4096)
	
	, tags="file"
)

