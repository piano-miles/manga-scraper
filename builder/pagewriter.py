from bs4 import BeautifulSoup
# from bs4.formatter import HTMLFormatter


def write(title):
    A = '<!DOCTYPE html><html><head><link rel="stylesheet" href="page.css"><title>' + \
        title+'</title></head><body><h1 class="header">'+title+'</h1>'

    for C in range(41):
        A += '<img src="images/img'+str(C+1)+'.jpg" class="image">'

    B = open('page.html', 'w')
    # B.write(
    #    BeautifulSoup(A+'</body></html>',
    #                  'html.parser').prettify(formatter=HTMLFormatter(indent=4))
    # )

    B.write(
        BeautifulSoup(A+'</body></html>',
                      'html.parser').prettify()
    )
    B.close()
