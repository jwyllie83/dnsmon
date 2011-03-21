import smtplib
import settings
from email.mime.text import MIMEText

class Mailer:

	def __init__( self, To, From, Subject, Message ):
		msg = MIMEText( Message )
		msg['Subject'] = Subject
		msg['From'] = From
		msg['To'] = ', '.join( To )

		import pdb
		pdb.set_trace()
		s = smtplib.SMTP(settings.mail_host, settings.mail_port)
		if settings.mail_use_TLS is True:
			s.starttls()
		if settings.mail_username is not None and settings.mail_password is not None:
			s.login(settings.mail_username, settings.mail_password)
		s.sendmail(From, To, msg.as_string())
		s.quit()
