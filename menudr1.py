import os

while(1):
	print('''

		Hello ,What you want to open
		1) VLC media player
		2) Chrome
		3) Notepad
		4) Enter "Stop" to exit''')
	ch=input("Enter your choice: ")
	if ('vlc' or'VLC'or 'Vlc') in ch:
		os.system("vlc")
	elif ('chrome' or 'Chrome' or 'CHROME') in ch:
		os.system('chrome')
	elif ('Notepad' or 'notepad' or 'NOTEPAD') in ch:
		os.system('notepad')
	elif ('stop' or 'STOP' or 'Stop') in ch:
		break
	else:
		print(" Sorry your choice is not valid!!")

