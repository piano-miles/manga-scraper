A = '<!DOCTYPE html>\n<html>\n<head>\n<link rel="stylesheet" href="styles.css">\n</head>\n<body>\n'

for C in range(87):
    A += '<img src="images/img'+str(C+1)+'.jpg" class="a">\n'
    
A += '</body>\n</html>'

B = open('index.html', 'w')
B.write(A)
B.close()
