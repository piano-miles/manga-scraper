from bs4 import BeautifulSoup


def write(title):
    A = '<!DOCTYPE html><html><head><link rel="stylesheet" href="page.css"><title>' + \
        title+'</title></head><body><h1 class="header">'+title+'</h1>'

    for C in range(391):
        A += f'<img src="../images/img{str(C+1)}.jpg" class="image">'

    with open('builder/page.html', 'w')as B:
        B.write(BeautifulSoup(f"{A}</body></html>", 'html.parser').prettify())


write('Omniscient Reader')
