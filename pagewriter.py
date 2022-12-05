from bs4 import BeautifulSoup
from bs4.formatter import HTMLFormatter

A = '<!DOCTYPE html><html><head><link rel="stylesheet" href="styles.css"></head><body>'

for C in range(87):
    A += '<img src="images/img'+str(C+1)+'.jpg" class="image">'

B = open('index.html', 'w')
B.write(
    BeautifulSoup(A+'</body></html>',
                  'html.parser').prettify(formatter=HTMLFormatter(indent=4))
)
B.close()
