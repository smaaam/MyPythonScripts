import webbrowser, sys, pyperclip

sys.argv

#Check if command line arguments were passed
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:]) # this part joins the given argument as a one string and doesnt include the mapit.py

else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
