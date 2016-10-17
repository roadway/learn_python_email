# -*- coding: utf-8 -*-
 
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
import smtplib
 
def _format_addr(s):
  name, addr = parseaddr(s)
  return formataddr(( \
    Header(name, 'utf-8').encode(), \
    addr.encode('utf-8') if isinstance(addr, unicode) else addr))
 
from_addr = 'luoshi@log001.com'
password = 'y67fcni..'
to_addr = 'luoshi@188.com'
smtp_server = 'mail.log001.com'

# 邮件对象: 
msg = MIMEMultipart()
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员luoshi <%s>' % to_addr)
msg['Subject'] = Header(u'来自luoshi的SMTP的问候……', 'utf-8').encode()
 
# 邮件正文是MIMEText:
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
 
# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('test.png', 'rb') as f:
  # 设置附件的MIME和文件名，这里是png类型:
  mime = MIMEBase('image', 'png', filename='test.png')
  # 加上必要的头信息:
  mime.add_header('Content-Disposition', 'attachment', filename='test.png')
  mime.add_header('Content-ID', '<0>')
  mime.add_header('X-Attachment-Id', '0')
  # 把附件的内容读进来:
  mime.set_payload(f.read())
  # 用Base64编码:
  encoders.encode_base64(mime)
  # 添加到MIMEMultipart:
  msg.attach(mime) 
 
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(0)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()