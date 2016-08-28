# -*- coding:utf-8 -*-
from flask import current_app
import urllib
import urllib2
import cookielib
import datetime
import time
import os
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('GBK')
sys.path.append('..')
import config

def login(username,password,account,account_owner_no):
	current_app.logger.debug('征信账号：{0}_{1}'.format(username,password))
	nowtime = time.strftime('%Y%m%d',time.localtime(time.time()))
	fpath = os.path.join(config.INV_PATH,str(nowtime)+"/"+str(account_owner_no)+"/"+str(account.get('account_no')))
	try:
		#登录主页
		hosturl = "http://9.96.47.2/shcreditunion/"
		#登录页面
		lgurl = "http://9.96.47.2/shcreditunion/login.jsp"
		#POST提交url
		logonurl = "http://9.96.47.2/shcreditunion/logon.do"
		cj = cookielib.LWPCookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
		urllib2.install_opener(opener)

		current_app.logger.error('征信初始化成功')
		index_html = opener.open(hosturl).read()
		current_app.logger.error('进入主页成功')

		lg_headers={
		    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)',
		    'Host':'9.96.47.2',
		    'Accept-Encoding':'gzip, deflate',
		    'Accept-Language':'zh-cn',
		    'Connection':'Keep-Alive',
		    'Referer':'http://9.96.47.2/shcreditunion/',
		    'Accept':'image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, application/x-shockwave-flash, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*'
		    }

		lg_request = urllib2.Request(lgurl,'',lg_headers)
		lg_html = opener.open(lg_request).read()

		current_app.logger.error('进入登录页成功')
		lg_html = BeautifulSoup(lg_html)
		btn_value = lg_html.find('input',{'name':'B1'}).attrs['value']

		#POST提交数据，进行登录
		logon_headers = {
		    'Accept':'image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, application/x-shockwave-flash, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*',
		    'Accept-Encoding':'gzip, deflate',
		    'Accept-Language':'zh-cn',
		    'Cache-Control':'no-cache',
		    'Connection':'Keep-Alive',
		    'Content-Length':46,
		    'Content-Type':'application/x-www-form-urlencoded',
		    'Host':'9.96.47.2',
		    'Referer':'http://9.96.47.2/shcreditunion/logon.do',
		    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)'
		    }
		logon_postData={
		    'B1':btn_value,
		    'password':password,
		    'userid':username
		    }
		lpd = urllib.urlencode(logon_postData)
		logon_request = urllib2.Request(logonurl,lpd,logon_headers)
		logon_content = opener.open(logon_request).read()
                logon_content_soup = BeautifulSoup(logon_content)
		message_field = lg_html.find('span',{'class':'message-error'})
		if message_field:
			message = message_field.string.strip()
			if message :
				current_app.logger.error('登录系统失败,%s'%(message))
				return False,'征信查询失败:'+message
                else:
            		current_app.logger.error('登录系统成功')
			username = account.get('current_name')
			username = username.encode('GBK')

			certype= "0" #"输入证件类型: 0、身份证  1、户口簿  2、护照  3、军官证  4、士兵证  5、港澳居民来往内地通行证  6、台湾同胞来往内地通行证  7、临时身份证  8、外国人居留证  9、警官证  X、其它证件  A、香港身份证  B、澳门身份证  C、台湾身份证")
			cercode = account.get('current_id_number')
			queryreason = "02" #raw_input(u"查询原因：01、贷后管理  02、贷款审批  03、信用卡审批  08、担保资格审查  05、异议核查 16、公积金提取复核  19、特约商户实名审查" 22、法人代表、负责人、高管等资信审查 23、客户准入资格审查 25、资信审查)
			vertype= "30" #raw_input(u"信用报告版式：30、银行版 31、银行异议版")
			idauthflag = "0" #raw_input(u"查询类型：0、信用报告查询 1、身份信息核查")
			current_app.logger.error('%s === %s === %s === %s === %s ' % (username, certype, cercode, queryreason, vertype) )

			#person_zx_report_url="http://9.96.47.2/shcreditunion/queryAction.do?username="+username+"&certype="+certype+"&cercode="+cercode+"&queryreason="+queryreason+"&vertype="+vertype+"&policetype=0"          

			person_zx_report_url="http://9.96.47.2/shcreditunion/queryAction.do?%s"

			gt_param = {'username':username,'certype':certype, 'cercode':cercode, 'queryreason':queryreason, 'vertype':vertype, 'idauthflag':idauthflag, 'policetype':0}
			gt_param_code = urllib.urlencode(gt_param)

			current_app.logger.error(gt_param_code)
			current_app.logger.error(person_zx_report_url)

			report_content = opener.open(person_zx_report_url,gt_param_code).read()
			current_app.logger.error('============================')
			current_app.logger.error(report_content)
			current_app.logger.error('============================')
			current_app.logger.error('查询成功')

			savefile('person_success',report_content,fpath)
			#savefile('person_success2',report_content.decode('gbk').encode('utf8')),fpath)

			current_app.logger.error('文件保存成功')
			return True,'查询成功'
	except Exception,e:
		current_app.logger.error(e)
		savefile('error',e,fpath)
	return False,'查询异常'

def savefile(filename,message,fpath):
	f = open(fpath+'/'+filename+'.html','w')
	f.write(str(message))
	f.close()

def run(account,account_owner_no,operator):
	username=operator.get('inv_username')
	password=operator.get('inv_password')
	flag,message = login(username,password,account,account_owner_no)
	return flag,message

    
