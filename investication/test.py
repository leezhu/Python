#encoding=utf-8
from investication import Investication

"""
root_path =["file:/home/pfchen/investication/template/person_success.html",
            "file:/home/pfchen/investication/template/person_success1.html",
            "file:/home/pfchen/investication/template/person_success2.html",
            "file:/home/pfchen/investication/template/person_success3.html",
            "file:/home/pfchen/investication/template/person_success4.html",
            "file:/home/pfchen/investication/template/person_success5.html"]
"""
root_path =["file:/home/leezhu/Documents/xccrm/server/app/investication/template/person_success2.html"]

for index in root_path:
	inv = Investication()
        
        information = inv.readinformation(index)
     #   print "information",information
#需要查看get出来的是字典还是列表，才能用不能方式得出结果
        info = {}

        #取出个人身份信息表信息
        item= information.get('个人基本信息').get('身份信息')        
        result=item
        item= information.get('个人基本信息').get('居住信息')   
        result=dict(result,**item[0])
        item= information.get('个人基本信息').get('配偶信息')   
        result=dict(result,**item)
        item = information.get('查询基本信息')
        result=dict(result,**item)
        item = information.get('个人基本信息').get('职业信息')
        a= item[0] 
        result=dict(result,**a)
        data={}
        for k,y in result.items():      #筛选出指定字段并按数据库字段改变键
            if '被查询者证件号码'==k:
                data=dict(data,**{'p_5109':y})
            if '被查询者姓名' ==k:
                data=dict(data,**{'p_5101':y})
            if '被查询者证件类型' ==k:
                data=dict(data,**{'p_5107':y})
            if '性别' ==k:
                data=dict(data,**{'p_5105':y})
            if '学历' ==k:
                data=dict(data,**{'p_5113':y})
            if '学位' ==k:
                data=dict(data,**{'p_5115':y})
            if '住宅电话' ==k:
                data=dict(data,**{'p_3115':y})
            if '手机号码' ==k:
                data=dict(data,**{'p_3117':y})
            if '单位电话' ==k:
                data=dict(data,**{'p_3119':y})
            if '通讯地址' ==k:
                data=dict(data,**{'p_3113':y})
            if '户籍地址' ==k:
                data=dict(data,**{'p_3101':y})
            if '工作单位' ==k:
                data=dict(data,**{'p_5117':y})
            if '单位地址' ==k:
                data=dict(data,**{'p_3133':y})
            if '行业' ==k:
                data=dict(data,**{'p_6103':y})
            if '职业' ==k:
                data=dict(data,**{'p_5119':y})
            if '职务' ==k:
                data=dict(data,**{'p_5121':y})
            if '职称' ==k:
                data=dict(data,**{'p_5123':y})
            if '进入本单位年份' ==k:
                data=dict(data,**{'p_2109':y})
            if '居住地址' ==k:
                data=dict(data,**{'p_3103':y})
            if '居住状况' ==k:
                data=dict(data,**{'p_5127':y})
            if '婚姻状况' ==k:
                data=dict(data,**{'p_5111':y})
            if '配偶姓名' ==k:
                data=dict(data,**{'p_5204':y})
            if '配偶证件类型' ==k:
                data=dict(data,**{'p_5208':y})
            if '配偶证件号码' ==k:
                data=dict(data,**{'p_5210':y})
            if '配偶工作单位' ==k:
                data=dict(data,**{'p_5206':y})
            if '配偶联系电话' ==k:
                data=dict(data,**{'p_3111':y})
        for k,y in data.items():    #将空字段由'--'转换成''
            if y=='--':
                data[k]=''
        info['个人身份信息表']=data     #用字典传个人身份信息返回值
        return info
    	for item in information.get('信贷交易信息明细').get('贷款'):
            for k,y in item.items():
	           print k,y
	    for item in information.get('信贷交易信息明细').get('贷记卡'):
	        for k,y in item.items():
	           print k,y
	    for item in information.get('信贷交易信息明细').get('准贷记卡'):
	        for k,y in item.items():
	           print k,y
	
'''     
        for k,y in information.get('信息概要').get('信用提示').items():
             print k,y
        for item in information.get('信息概要').get('逾期及违约信息概要').get('逾期（透支)信息汇总'):
             for k,y in item.items():
                   print k,y

        for k,y in information.get('信息概要').get('授信及负债信息概要').get('未结清贷款信息汇总').items():
             print k,y
	for k,y in information.get('信息概要').get('授信及负债信息概要').get('未销户贷记卡信息汇总').items():
             print k,y
	for k,y in information.get('信息概要').get('授信及负债信息概要').get('未销户准贷记卡信息汇总').items():
             print k,y
	for k,y in information.get('信息概要').get('授信及负债信息概要').get('对外担保信息汇总').items():
	     print k,y

	for item in information.get('信贷交易信息明细').get('贷款'):
             for k,y in item.items():
	           print k,y
	for item in information.get('信贷交易信息明细').get('贷记卡'):
	     for k,y in item.items():
	           print k,y
	for item in information.get('信贷交易信息明细').get('准贷记卡'):
	     for k,y in item.items():
	           print k,y
	for item in information.get('信贷交易信息明细').get('担保信息').get('对外担保信息'):
	     for k,y in item.items():
	           print k,y 
	for k,y in information.get('公共信息明细').get('住房公积金参缴记录').items():
		   print k,y
	for item in information.get('查询记录').get('查询记录汇总'):
	     for k,y in item.items():
	           print k,y 
	for item in information.get('查询记录').get('信贷审批查询记录明细'):
	     for k,y in item.items():
	           print k,y   
'''
