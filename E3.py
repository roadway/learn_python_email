# -*- coding: utf-8 -*-
 
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
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
 
msg = MIMEText('<html><body><h1>Hello</h1>' +
  '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
  '</body></html>', 'html', 'utf-8')
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员luoshi <%s>' % to_addr)
msg['Subject'] = Header(u'来自luoshi的SMTP的问候……', 'utf-8').encode()
 
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()