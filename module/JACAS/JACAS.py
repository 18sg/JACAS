from django.contrib.auth.models import User
import PAM

thePass = None

def pam_conv(auth, query_list, userData):
	resp = []
	for i in range(len(query_list)):
		query, type = query_list[i]
	if(query == 'Password: '):
		resp.append((thePass, 0))
	else:
		resp.append(('',0))
	return resp

class JACAS:

	def authenticate(self, username=None, password=None):
		auth = PAM.pam()
		auth.start('passwd')
		auth.set_item(PAM.PAM_USER, username)
		auth.set_item(PAM.PAM_CONV, pam_conv)
		global thePass
		thePass = password
		try:
			auth.authenticate()
			auth.acct_mgmt()
		except Exception, e:
			return None
		else:
			try:
				user_db = User.objects.get(username=username)
			except User.DoesNotExist:
				user_db = User(username = username, password = 
					User.objects.make_random_password())
				user_db.save()
			return user_db
