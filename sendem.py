import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

messag = input('Write whatever you want:\n')

def send_email():
	#We create a list to enter emails separated by commas to send them a message
	friends = ['']
	sender = '' #enter your email
	password = '' #enter your email's password
	#sendto = ''   for one-way address only

	#Host and port
	sr = smtplib.SMTP('smtp.gmail.com',587)
	sr.starttls()

	try:
		with open('') as ht:
			temps = ht.read()
	except IOError:
		mistake = 'Can not open this file,try again'
		return mistake

	try:
		sr.login(sender,password)       #trying to log in
 		rus = MIMEMultipart()
		#rus = MIMEText(vlozh,'html')
		rus['Subject'] ='Introduction'       #Tag of ur email
		rus.attach(MIMEText(messag))
		rus.attach(MIMEText(temps,'html'))
		for i in friends:          #sending messages for every email that we added
		    sr.sendmail(sender,i,rus.as_string())
		#server.sendmail(sender,sender,f"Subject: hey \n{message}")

		return 'The message was sent!'

	except Exception as _ex:
		return f"{_ex}\n Please check your password or login"
def main():
    print(send_email())

if __name__ == "__main__":
	main()

