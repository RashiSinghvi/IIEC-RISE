import os

start_list=['open','use','enter','run','launch','load','reload','start','set up','innovate','initiate','create','produce','begin','start off','commence','institute','inaugurate','instigate']

not_list=['not', "don't",'do not','never','unload']


while True:
	print('''
	  It is a platform, where you can easily chat with the system and perform some task.
	  What you have to do is:
	  Enter your choice in one statement.
	  (For now) you can perform only limited task as:
	  			1) Launch notepad
	  			2) Run Google chrome
	  			3) Use Discord
	  			4) Create new directory
	  			5) Open VLC Player
	  			6) List of all directory
	   You can also termainate the program using exit or stop.
	''')
	p=input("What do you want to do?  : ")
	print()
	p=p.lower()

	flag=0
	for i in not_list:
		if i in p:
			flag=flag+1
			break

	if flag>=1:
		print("okay ... as you wish....you denied....")
	elif ('exit' in p) or ('stop' in p) or ('terminate' in p):
		break
	else:
		count=0
		for j in start_list:
			if j in p:
				count=count+1
				break
		if count>=1:
			if ('notepad' in p) or ('text editor' in p) or ('text file' in p) or ('text' in p):
				os.system("notepad")
			elif ('chrome' in p) or ('google chrome' in p) or ('browser' in p) or ('search' in p):
				os.system("chrome")
			elif ('discord' in p):
				os.system("discord")
			elif ('directory' in p) :
				os.system("mkdir new")
			elif ('video player' in p) or ('media player' in p) or ('vlc' in p):
				os.system("vlc")
			else :
				print("Not supported !!!!!!!!!!")
		else:
			print("Not supported")