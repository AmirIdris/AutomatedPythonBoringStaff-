import webbrowser, pyperclip, sys
if len(sys.argv) >1:
    address = ''.join(sys.argv[1:])

else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
webbrowser.open('https://www.facebook.com')



