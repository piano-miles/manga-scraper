page = "<!DOCTYPE html>\n<html>\n<head>\n<link rel=\"stylesheet\" href=\"styles.css\">\n</head>\n<body>\n"

for i in range(87):
    page += "<img src=\"images/img"+str(i+1)+".jpg\" class=\"a\">\n"

page += "</body>\n</html>"

f = open("index.html", "w")
f.write(page)
f.close()
