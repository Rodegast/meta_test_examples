from dsl import *

TEST["nestedframes"](
	URL("/nestedframes")
	, ONE(FP("#frame1", "body")) == "Parent frame"
	, ONE(FP("#frame1", "iframe", "body")) == "Child Iframe"
	, tags="frame"
)

TEST["frames"](
	URL("/frames")
	, ONE(FP("#frame1", "html")) == "This is a sample page"
	, ONE(FP("#frame2", "html")) == "This is a sample page"
	, tags="frame"
)
