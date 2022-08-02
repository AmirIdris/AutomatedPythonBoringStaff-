backonFile = open('backon.txt', 'w')
backonFile.write('Hello World \n')


content = backonFile.read()
backonFile.close()
print(content)