#encoding=utf-8
from investication import Investication
import uuid

"""
root_path =["file:/home/pfchen/investication/template/person_success.html",
            "file:/home/pfchen/investication/template/person_success1.html",
            "file:/home/pfchen/investication/template/person_success2.html",
            "file:/home/pfchen/investication/template/person_success3.html",
            "file:/home/pfchen/investication/template/person_success4.html",
            "file:/home/pfchen/investication/template/person_success5.html"]
"""

class Result():
   def __init__(self):
        self.root_path ="file:/home/leezhu/Documents/xccrm/server/app/investication/template/person_success150.html"  #路径
#        self.root_path ="file:/home/leezhu/Documents/xccrm/server/app/investication/person_all.html"
        self.inv=Investication()    #对象实例化
        self.information = self.inv.readinformation(self.root_path)
        self.uuid=str(uuid.uuid1())  #由时间,mac地址生成uuid

   #个人基本信息
   def personInfo(self):
              item= self.information.get('个人基本信息').get('身份信息')   #需要查看get出来的是字典还是列表，才能用不能方式得出结果
              item= self.information.get('个人基本信息').get('身份信息')        
              result=item
              item= self.information.get('个人基本信息').get('居住信息')   
              if item:
                  result=dict(result,**item[0])     #为空进行处理
              else:
                 pass
              item= self.information.get('个人基本信息').get('配偶信息')   
              result=dict(result,**item)
              item = self.information.get('查询基本信息')
              result=dict(result,**item)
              item = self.information.get('个人基本信息').get('职业信息')
              if item:
                  result=dict(result,**item[0])     #为空进行处理
              else:
                  pass
              data={}
              data['uuid']=self.uuid    #添加内码
              for k,y in result.items():      #筛选出指定字段并按数据库字段改变键
                  if '被查询者证件号码'==k:
                      data=dict(data,**{'p_5109':y})
                  if '被查询者姓名' ==k:
                      data=dict(data,**{'p_5101':y})
                  if '被查询者证件类型' ==k:
                      data=dict(data,**{'p_5107':y})
                  if '性别' ==k:
                      data=dict(data,**{'p_5105':y})
                  if '出生日期' ==k:
                      data=dict(data,**{'p_2408':y})
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
              return data

   #贷款信息
   def loanInfo(self):
       ite = self.information.get('信贷交易信息明细').get('贷款')   
       data=[]              #存整个贷款信息
       overdue=[]
       for item in ite:
           loan_uuid=str(uuid.uuid1())       #每条贷款记录都有自己的uuid
           temp={}      #临时存储一条贷款字典
           overdue=[]   #存逾期信息
           temp['o_3']=''   #一次性归还时，期数为空
           temp['loan_uuid']=loan_uuid      #贷款记录内码
           temp['uuid']=self.uuid           #贷款人全局内码
           for k,y in item.items():
               if '业务号'==k:
                   temp=dict(temp,**{'o_7101':y})      
               if '机构'==k:
                   temp=dict(temp,**{'o_6101':y})   
               if '贷款类型'==k:
                   temp=dict(temp,**{'o_7111':y})      
               if '金额'==k:
                   temp=dict(temp,**{'o_1101':y})      
               if '日期'==k:
                   y=y[:4]+y[5:7]+y[8:10]    #将由传过来的字符串'2005年11月01日'这样的形式转换成20051101，注意一个汉字在分片中占三个
                   temp=dict(temp,**{'o_2101':y})      
               if '截止时间'==k:            #还款结清日期
                   temp=dict(temp,**{'o_2':y})      
               if '期数'==k:
                   y=y[0:3]                     #由36期转成36，
                   temp=dict(temp,**{'o_3':y})      
               if '抵押担保'==k:
                   temp=dict(temp,**{'o_7115':y})      #担保方式
               if '到期时间'==k:
                   y=y[:4]+y[5:7]+y[8:10]
                   temp=dict(temp,**{'o_2103':y})      
               if '归还方式'==k:
                   temp=dict(temp,**{'o_1':y})
               if '表格'==k :                       #贷款还款信息表,特殊交易类型，
                   for k,y in y.items():
                       if '逾期31-60天未还本金'==k:
                          temp=dict(temp,**{'o_1113':y})
                       if '当前逾期金额'==k:
                          temp=dict(temp,**{'o_1111':y})
                       if '剩余还款期数'==k:
                          temp=dict(temp,**{'o_4105':y})
                       if '还款记录'==k:
                          temp=dict(temp,**{'o_7107':y})
                       if '逾期180天以上未还本金'==k:
                          temp=dict(temp,**{'o_1119':y})
                       if '逾期61-90天未还本金'==k:
                          temp=dict(temp,**{'o_1115':y})
                       if '当前逾期期数'==k:
                          temp=dict(temp,**{'o_4109':y})
                       if '最近一次还款日期'==k:
                          temp=dict(temp,**{'o_2107':y})
                       if '本月实还款'==k:
                          temp=dict(temp,**{'o_1107':y})
                       if '本金余额'==k:
                          temp=dict(temp,**{'o_1109':y})
                       if '五级分类'==k:
                          temp=dict(temp,**{'o_7105':y})
                       if '逾期91-180天未还本金'==k:
                          temp=dict(temp,**{'o_1117':y})
                       if '应还款日'==k:
                          temp=dict(temp,**{'o_2301':y})
                       if '本月应还款'==k:
                          temp=dict(temp,**{'o_1105':y})
                       if '特殊交易类型'==k:
                           temp=dict(temp,**{'o_7113':y})
                       if '变更月数'==k:
                           temp=dict(temp,**{'o_4418':y})
                       if '发生金额'==k:
                           temp=dict(temp,**{'o_1416':y})
                       if '发生日期'==k:
                           temp=dict(temp,**{'o_2410':y})
                       if '明细记录'==k:
                           temp=dict(temp,**{'o_8101':y})
                       if '逾期记录'==k:
                           for x in range(0,len(y),3):          #按间隔3进行取值
                               over={}
                               over=dict(over,**{'over_month':y[x]})
                               over=dict(over,**{'over_monthnum':y[x+1]})
                               over=dict(over,**{'over_money':y[x+2]})
                               over['overdue_uuid']=loan_uuid        #每条逾期记录关联贷记卡uuid
                               overdue.append(over)
           a={}
           a['贷款信息']=temp
           a['逾期信息']=overdue    #不为空就添加
           data.append(a)       #用列表存每条贷款信息  
       return data
   
   #贷记卡信息
   def creditCardInfo(self):
       ite = self.information.get('信贷交易信息明细').get('贷记卡')
       data1=[]      #封装每条贷记卡信息
       data2=[]      #封装每条逾期信息 
       for it in ite:
           credit_uuid=str(uuid.uuid1())
           creditdata={}
           overdue=[]
           creditdata['credit_uuid']=credit_uuid
           creditdata['uuid']=self.uuid
           overdue=[]
           for k,y in it.items():
               if '时间'==k:
                   y=y[:4]+y[5:7]+y[8:10]
                   creditdata=dict(creditdata,**{'c_2101':y})
               if '授信额度'==k:
                   creditdata=dict(creditdata,**{'c_1101':y})
               if '共享授信额度'==k:
                   creditdata=dict(creditdata,**{'c_2':y})
               if '账户类型'==k:
                   creditdata=dict(creditdata,**{'c_accouttype':y})
               if '账户状态'==k:
                   creditdata=dict(creditdata,**{'c_3':y})
               if '担保方式'==k:
                   creditdata=dict(creditdata,**{'c_7115':y})
               if '机构'==k:
                   creditdata=dict(creditdata,**{'c_6101':y})
               if '业务号'==k:
                   creditdata=dict(creditdata,**{'c_7101':y})
               if '截止时间'==k:
                   y=y[2:6]+y[7:9]+y[10:12]
                   creditdata=dict(creditdata,**{'c_1':y})
               if '表格'==k:
                   for k,y in y.items():
                       if '当前逾期金额'==k:
                           creditdata=dict(creditdata,**{'c_1111':y})
                       if '最近六个月平均使用额度'==k:
                           creditdata=dict(creditdata,**{'c_sixmean1109':y})
                       if '还款记录'==k:
                           creditdata=dict(creditdata,**{'c_7107':y})
                       if '账户状态'==k:
                           creditdata=dict(creditdata,**{'c_3':y})
                       if '最大使用额度'==k:
                           creditdata=dict(creditdata,**{'c_h1109':y})
                       if '当前逾期期数'==k:
                           creditdata=dict(creditdata,**{'c_4109':y})
                       if '最近一次还款日期'==k:
                           creditdata=dict(creditdata,**{'c_2107':y})
                       if '共享额度'==k:
                           creditdata=dict(creditdata,**{'c_1102':y})
                       if '本月实还款'==k:
                           creditdata=dict(creditdata,**{'c_1107':y})
                       if '账单日'==k:
                           creditdata=dict(creditdata,**{'c_2101':y})
                       if '已用额度'==k:
                           creditdata=dict(creditdata,**{'c_1109':y})
                       if '本月应还款'==k:
                           creditdata=dict(creditdata,**{'c_1105':y})
                       if '逾期记录'==k:
                           for x in range(0,len(y),3):          #按间隔3进行取值
                               over={}
                               over=dict(over,**{'over_month':y[x]})
                               over=dict(over,**{'over_monthnum':y[x+1]})
                               over=dict(over,**{'over_money':y[x+2]})
                               over['overdue_uuid']=credit_uuid        #每条逾期记录关联贷记卡uuid
                               overdue.append(over)
           data1.append(creditdata)
           data2.append(overdue)    #不为空
       info={}
       if data1:
           info['贷记卡信息']=data1
           info['贷记卡逾期信息']=data2
       else:
           pass
       return info
   
   #准贷记卡信息
   def semicreditInfo(self):
       ite = self.information.get('信贷交易信息明细').get('准贷记卡')   
       info=[]
       for it in ite:
           semidata={}
           semi_uuid=str(uuid.uuid1())
           semidata['semi_uuid']=semi_uuid      #每条准贷记卡的uuid
           semidata['uuid']=self.uuid           #整个页面信息的uuid进行绑定，以便可以查询
           for k,y in it.items():
               if '时间'==k:
                   y=y[:4]+y[5:7]+y[8:10]       #时间格式切片
                   semidata=dict(semidata,**{'s_2101':y})
               if '授信额度'==k:
                   semidata=dict(semidata,**{'s_1101':y})
               if '账户类型'==k:
                   semidata=dict(semidata,**{'s_accouttype':y})
               if '担保方式'==k:
                   semidata=dict(semidata,**{'s_7115':y})
               if '机构'==k:
                   semidata=dict(semidata,**{'s_6101':y})
               if '业务号'==k:
                   semidata=dict(semidata,**{'s_7101':y})
               if '截止时间'==k:
                   y=y[2:6]+y[7:9]+y[10:12]
                   semidata=dict(semidata,**{'s_1':y})
               if '表格'==k:
                   for k,y in y.items():
                       if '本月实还款'==k:
                           semidata=dict(semidata,**{'s_1107':y})
                       if '最近六个月平均透支余额'==k:
                           semidata=dict(semidata,**{'s_3':y})
                       if '最大透支余额'==k:
                           semidata=dict(semidata,**{'s_h1109':y})
                       if '透支180天以上未付余额'==k:
                           semidata=dict(semidata,**{'s_1':y})
                       if '账户状态'==k:
                           semidata=dict(semidata,**{'s_4':y})
                       if '共享金额'==k:
                           semidata=dict(semidata,**{'s_1102':y})
                       if '账单日'==k:
                           semidata=dict(semidata,**{'s_2101':y})
                       if '最近一次还款日期'==k:
                           semidata=dict(semidata,**{'s_2107':y})
                       if '还款记录'==k:
                           semidata=dict(semidata,**{'s_7107':y})
                       if '透支余额'==k:
                           semidata=dict(semidata,**{'s_2':y})
           info.append(semidata)    
       return info

   #对外担保信息
   def assureInfo(self):
       ite = self.information.get('信贷交易信息明细').get('担保信息')   
       info=[]
       for it in ite:
           data={}
           data['uuid']=self.uuid
           for k,y in it.items():
               if '担保金额'==k:
                   data=dict(data,**{'a_moy':y})
               if '担保贷款本金余额'==k:
                   data=dict(data,**{'a_remmoy':y})
               if '担保贷款五级分类'==k:
                   data=dict(data,**{'a_sort':y})
               if '担保贷款到期日期'==k:
                   data=dict(data,**{'a_end_dat':y})
               if '结算日期'==k:
                   data=dict(data,**{'a_exp_dat':y})
               if '担保贷款发放日期'==k:
                   data=dict(data,**{'a_sta_dat':y})
               if '担保贷款合同金额'==k:
                   data=dict(data,**{'a_pamoy':y})
               if '担保贷款发放机构'==k:
                   data=dict(data,**{'a_org':y})
           
           info.append(data)     
       return info

   #住房公积金信息
   def hoFndInfo(self):
       ite = self.information.get('公共信息明细').get('住房公积金参缴记录')   
       info=[]
       data={}
       data['uuid']=self.uuid
       for k,y in ite.items():
           if '信息更新日期'==k:
               data=dict(data,**{'h_up_dat':y})
           if '参缴日期'==k:
               data=dict(data,**{'h_dat':y})
           if '缴费单位'==k:
               data=dict(data,**{'h_comp':y})
           if '参缴地'==k:
               data=dict(data,**{'h_addr':y})
           if '个人缴存比例'==k:
               data=dict(data,**{'h_per_rat':y})
           if '单位缴存比例'==k:
               data=dict(data,**{'h_comp_rat':y})
           if '缴至月份'==k:
               data=dict(data,**{'h_mon':y})
           if '月缴存额'==k:
               data=dict(data,**{'h_depos':y})
           if '初缴月份'==k:
               data=dict(data,**{'h_fir_mon':y})
           if '缴费状态'==k:
               data=dict(data,**{'h_stus':y})
       
       info.append(data)
       return info

   #信用信息
   def creditInfo(self):
       ite6 = self.information.get('信息概要').get('授信及负债信息概要').get('对外担保信息汇总')   
       data={}     
       data['uuid']=self.uuid
       for k,y in ite6.items():
           if '担保笔数'==k:
               data=dict(data,**{'cf_23':y})
           if '担保金额'==k:
               data=dict(data,**{'cf_24':y})
           if '担保本金余额'==k:
               data=dict(data,**{'cf_25':y})
      

       ite5 = self.information.get('信息概要').get('授信及负债信息概要').get('未销户准贷记卡信息汇总')   
       for k,y in ite5.items():
           if '账户数'==k:
               data=dict(data,**{'cf_15':y})
           if '授信总额'==k:
               data=dict(data,**{'cf_16':y})
           if '单家行最低授信额'==k:
               data=dict(data,**{'cf_17':y})
           if '最近6个月平均使用额度'==k:
               data=dict(data,**{'cf_18':y})
           if '单家行最高授信额'==k:
               data=dict(data,**{'cf_19':y})
           if '发卡法人机构数'==k:
               data=dict(data,**{'cf_20':y})
           if '透支余额'==k:
               data=dict(data,**{'cf_21':y})
           if '发卡机构数'==k:
               data=dict(data,**{'cf_22':y})

       
       ite4 = self.information.get('信息概要').get('授信及负债信息概要').get('未销户贷记卡信息汇总')   
       for k,y in ite4.items():
           if '账户数'==k:
               data=dict(data,**{'cf_7':y})
           if '授信总额'==k:
               data=dict(data,**{'cf_8':y})
           if '单家行最低授信额'==k:
               data=dict(data,**{'cf_9':y})
           if '最近6个月平均使用额度'==k:
               data=dict(data,**{'cf_10':y})
           if '单家行最高授信额'==k:
               data=dict(data,**{'cf_11':y})
           if '发卡法人机构数'==k:
               data=dict(data,**{'cf_12':y})
           if '已用额度'==k:
               data=dict(data,**{'cf_13':y})
           if '发卡机构数'==k:
               data=dict(data,**{'cf_14':y})
 

       ite3 = self.information.get('信息概要').get('授信及负债信息概要').get('未结清贷款信息汇总')   
       for k,y in ite3.items():
           if '贷款法人机构数'==k:
               data=dict(data,**{'cf_1':y})
           if '合同总额'==k:
               data=dict(data,**{'cf_4':y})
           if '余额'==k:
               data=dict(data,**{'cf_5':y})
           if '贷款机构数'==k:
               data=dict(data,**{'cf_2':y})
           if '最近6个月平均应还款'==k:
               data=dict(data,**{'cf_6':y})
           if '笔数'==k:
               data=dict(data,**{'cf_3':y})


       ite2 = self.information.get('信息概要').get('逾期及违约信息概要').get('逾期(透支)信息汇总')   
       if ite2:
          for k,y in ite2[0].items():      #分开处理贷款逾期、贷记卡逾期、准贷记卡逾期，因为解析传送过来的信息k是一样的，但是顺序是不变的，从左到右
              if '笔数'==k:
                  data=dict(data,**{'cf_loan_num':y})
              if '单月最高逾期总额'==k:
                  data=dict(data,**{'cf_loan_sum':y})
              if '最长逾期月数'==k:
                  data=dict(data,**{'cf_loan_lomon':y})
              if '月份数'==k:
                  data=dict(data,**{'cf_loan_mon':y})
          for k,y in ite2[1].items():
              if '笔数'==k:
                  data=dict(data,**{'cf_credit_num':y})
              if '单月最高逾期总额'==k:
                  data=dict(data,**{'cf_credit_sum':y})
              if '最长逾期月数'==k:
                  data=dict(data,**{'cf_credit_lomon':y})
              if '月份数'==k:
                  data=dict(data,**{'cf_credit_mon':y})
          for k,y in ite2[2].items():
              if '笔数'==k:
                  data=dict(data,**{'cf_scredit_num':y})
              if '单月最高透支余额'==k:
                  data=dict(data,**{'cf_scredit_sum':y})
              if '最长逾期透支月数'==k:
                  data=dict(data,**{'cf_scredit_lomon':y})
              if '月份数'==k:
                  data=dict(data,**{'cf_scredit_mon':y})


       ite = self.information.get('信息概要').get('信用提示')   
       for k,y in ite.items():
           if '首笔贷款发放月份'==k:
               data=dict(data,**{'cf_fir_mon':y})
           if '异议标注数目'==k:
               data=dict(data,**{'cf_dis_num':y})
           if '其他贷款笔数'==k:
               data=dict(data,**{'cf_oth_num':y})
           if '首张贷记卡发卡月份'==k:
               data=dict(data,**{'cf_cre_mon':y})
           if '首张准贷记卡账户数发卡月份'==k:
               data=dict(data,**{'cf_scre_mon':y})
           if '住房贷款笔数'==k:
               data=dict(data,**{'cf_hloan_num':y})
           if '准贷记卡账户数'==k:
               data=dict(data,**{'cf_sacc_num':y})
           if '本人声明数目'==k:
               data=dict(data,**{'cf_decl_num':y})
           if '贷记卡账户数'==k:
               data=dict(data,**{'cf_acc_num':y})
       return data

'''
if __name__ == "__main__":
    result=Result()
#    h=result.hoFndInfo()
#    c=result.creditInfo()  
#    a=result.assureInfo()
#    p=result.personInfo()
    se=result.semicreditInfo()
#    result.creditCardInfo()
#    l=result.loanInfo()
#    for k,y in p.items():
#        print k,y
'''        
