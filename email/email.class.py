#encoding=utf8
# author zeopean
# date 2015-12-2

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart		#发送附件

class emailHeadle:
	'定义系统登录常量'
	Host 	= 'smtp.163.com'
	User	= 'zeopean@163.com'
	Pwd		= 'xyfvxafmwvowgcwx'
	postfix	= 'email from zeopean@163.com'

	# 发送text文本格式的邮件
	def SendTextEmail(self,ToUserLists ,sub , content):
		header  = "<"+ emailHeadle.User +">"
		msg 	= MIMEText(content , _subtype='plain' , _charset='utf-8')
		msg['Subject']	= sub
		msg['From']		= header
		msg['To']		= ';'.join(ToUserLists)

		#发送邮件
		self.send(header , ToUserLists , msg)


	# 发送html格式的邮件
	def SendHtmlEmail(self , toUserLists , subject ,content):
		header  = "<"+ emailHeadle.User +">"
		msg 	= MIMEText(content ,_subtype='html' , _charset='utf-8')
		msg['Subject']  = subject
		msg['From']		= header
		msg['To']		= ';'.join(toUserLists)

		#发送邮件
		self.send(header , toUserLists , msg)



	def SendMultiparEmail(self,toUserLists , subject,filename ):
		#创建MUli对象
		multi = MIMEMultipart()
		header  = "<"+ emailHeadle.User +">"

		#构造附件
		attart = MIMEText(open('E:\\1.txt' , 'rb').read() ,'base64' ,'gb2312')
		attart["Content-Type"] = 'application/octet-stream'
		attart["Content-Disposition"] = 'attachment; filename="1.doc"'
		multi.attach(attart)

		#邮件头
		multi['To'] 	= ';'.join(toUserLists)
		multi['From']	= header
		multi['Subject']= subject

		#发送
		self.send(multi['From'] , multi['To'] , multi)

#发送公共方法
	def send(self , header , ToUsers , msg):
		try:
			server = smtplib.SMTP()
			server.connect(emailHeadle.Host)
			server.login(emailHeadle.User , emailHeadle.Pwd)
			server.sendmail( header , ToUsers , msg.as_string())
			server.quit()
			return True
		except Exception , e:
			print str(e)
			return False

email = emailHeadle()
#email.SendTextEmail(['1412512785@qq.com'] ,'pycode email demo' , 'hello world!我是我的')
#email.SendHtmlEmail(['1412512785@qq.com'] ,'pycode email demo' , '<h1><font color="red">hello</font> world!我是我的</h1>')

#email.SendMultiparEmail(['1412512785@qq.com'] ,'pycode email multipart demo' , '1.txt')





