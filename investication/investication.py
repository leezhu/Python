#encoding=utf-8
from sgmllib import SGMLParser 
import urllib2
import sys
class Investication(SGMLParser):
       
    def reset(self):
        self.userlist = []  #用户基本信息表
        self.spouselist = [] #配偶信息
        self.adresslist = []    #居住信息
        self.careerlist = []    #职业信息
        self.creditlist = []    #信用提示
        self.overduelist = []   #逾期信息
        self.outstandlist = []  #负债信息
        self.creditcardlist = []    #
        self.semicreditlist = []
        self.externallist = []
        self.housefundlist = [] #住房公积金信息
        self.allselectlist = [] #查询记录汇总
        self.selectrecordlist = []  #查询记录明细
        self.listcountflag = [] #标志位数
        self.guaranteeflag=False    #担保标志
        self.guaranteelist=[]       #担保信息
        self.listcount=0  
        self.listcount1=0
        self.listcount2=0
        self.tableflag = [] #表标志
        self.tablelist = [] #dai kuang 表信息
        self.loaninfo = [] 
        self.listcountflag1=[]
        self.listcountflag2=[]
        self.info = []
        self.info1 = []
        self.info2=[]
        self.tableflag1=[]
        self.tablelist1=[]
        self.tableflag2=[]
        self.tablelist2=[]
        self.queryoperationlist=[]
        self.useflag = False
        self.spouseflag = False
        self.adressflag = False
        self.careerflag = False
        self.creditflag = False
        self.overdueflag = False
        self.outstandflag = False
        self.creditcardflag = False
        self.semicreditflag = False
        self.externalflag = False
        self.housefundflag = False
        self.allselectflag = False
        self.allsemiflag=False
        self.loanflag = False
        self.cardflag=False
        self.flag = False  
        self.getdata = False
        self.flag1 = False
        self.flag2 = False
        self.queryoperationflag=False
        self.tablegetdata=False
        self.item=0
        self.item1=0
        root_dic = {}
        self.count = 1
        self.countloan = 0
        self.countcredit=0
        self.countsemi=0
        self.countguarantee=1
        SGMLParser.reset(self)  
    def start_tr(self, attrs): #匹配标签,进入tr 
        self.flag = True  
        for k, v in attrs:
            if (k == 'valign' and v == 'bottom') : #找到valign 和botton属性的标签，并将各个信息读取设置为否，不读
                self.useflag = False
                self.spouseflag = False
                self.adressflag = False
                self.careerflag = False
                self.creditflag = False
                self.overdueflag = False
                self.outstandflag = False
                self.creditcardflag = False
                self.semicreditflag = False
                self.housefundflag = False
                self.allselectflag = False
                self.loanflag = False
                self.cardflag=False
                self.allsemiflag=False 
            if k == 'height' and v == '40':
                self.housefundflag = False
                self.externalflag = False
                self.guaranteeflag=False
                self.queryoperationflag=False
    def end_tr(self): 
        self.flag = False 
    def start_td(self, attrs):    
        self.flag = True
        
    def end_td(self): 
        self.flag = False  
                 
    def start_span(self, attrs):  
        if self.flag == False:  
            return  
        self.getdata = True 
                
    def end_span(self):  
        if self.getdata:  
            self.getdata = False 
           
    def start_font(self, attrs):  
        if self.flag == False:  
            return  
        self.getdata = True 
                
    def end_font(self):  
        if self.getdata:  
            self.getdata = False
            
    def start_tbody(self, attrs):  
        if self.flag == False:  
            return  
        #self.tablegetdata = True 
        self.flag2 = True   
            
    def end_tbody(self):  
        #if self.tablegetdata:  
         # self.tablegetdata = False
        self.flag2 = False
        self.listcountflag.append(self.listcount)   #count hole count
        self.listcountflag1.append(self.listcount1)
        self.listcountflag2.append(self.listcount2)
        self.listcount1=0
        self.listcount2=0
        self.listcount = 0                  
    def handle_data(self, text): 
        if '报告编号' in text.strip():
            self.queryoperationflag=True
        if self.queryoperationflag and self.getdata:
            self.queryoperationlist.append(text)
        if '身份信息' == (text.strip()):
            self.useflag = True
        if self.getdata and self.useflag:
            self.userlist.append(text.strip())
            
        if '配偶信息' == (text.strip()):          
            self.spouseflag = True
        if self.getdata and self.spouseflag:
            self.spouselist.append(text)
          
        if '居住信息' == (text.strip()):         
            self.adressflag = True
        if  self.getdata and self.adressflag:
            self.adresslist.append(text)
        
        if '职业信息' == (text.strip()):      
            self.careerflag = True
        if  self.getdata and self.careerflag:
            self.careerlist.append(text)
            if text == str(self.count):
             self.count += 1 
             
        if '信用提示' in text.strip():
            self.creditflag = True
        if self.getdata and self.creditflag:
            self.creditlist.append(text)
        
        if '逾期（透支）信息汇总' in text.strip():
            self.overdueflag = True
        if self.getdata and self.overdueflag:
            self.overduelist.append(text) 
            
        if '未结清贷款信息汇总' in text.strip():
            self.outstandflag = True
        if self.getdata and self.outstandflag:
            self.outstandlist.append(text)   
                    
        if '未销户贷记卡信息汇总' == text.strip():
            self.creditcardflag = True
        if  self.getdata and self.creditcardflag:
            self.creditcardlist.append(text)
        
        if '未销户准贷记卡信息汇总'in text.strip():
            self.semicreditflag = True
        if self.getdata and self.semicreditflag:
            self.semicreditlist.append(text)
            
        if '对外担保信息汇总'in text.strip():
            self.externalflag = True
        if self.getdata and self.externalflag:
            self.externallist.append(text)  
            
        if '住房公积金参缴记录' == text.strip():
            self.housefundflag = True
        if self.getdata and self.housefundflag:
            self.housefundlist.append(text) 
        
        if '查询记录汇总' in text.strip():
            self.allselectflag = True
        if self.allselectflag and self.getdata:
            self.allselectlist.append(text) 
           
           
        if '信贷审批查询记录明细' in text.strip():
            self.flag1 = True
        if '报告说明' in text.strip():  
            self.flag1 = False
        if self.flag1 and self.getdata:
            self.selectrecordlist.append(text) 
            
        if '（一）贷款' in text.strip()or  '（二）贷款' in text.strip() and len(text.strip()) == 15:
            self.loanflag = True
        if self.loanflag and self.getdata: 
                if len(text.strip())>160:
                  self.countloan +=1
                  self.info.append(text.strip())   
                if self.flag2:
                   if text.strip()!='':
                      self.tableflag.append(self.countloan)
                      self.tablelist.append(text.strip())
                      self.listcount+=1
        if  '（二）贷记卡' in text.strip() or  '（三）贷记卡'in text.strip() or '（一）贷记卡'in text.strip() and len(text.strip())==18:
              self.cardflag=True
        if self.cardflag and self.getdata: 
              if len(text.strip())>140:
                  self.countcredit+=1
                  self.info1.append(text.strip())   
              if self.flag2:
                  if text.strip()!='':
                      self.tableflag1.append(self.countcredit)
                      self.tablelist1.append(text.strip())
                      self.listcount1+=1
                      
        if '（二）准贷记卡' in text.strip() or '（三）准贷记卡' in text.strip() or '（一）准贷记卡' in text.strip()  and len(text.strip())==21:
            self.allsemiflag=True
        if self.allsemiflag and self.getdata: 
           if len(text.strip())>140:
              self.countsemi+=1
              self.info2.append(text.strip())   
           if self.flag2:
              if text.strip()!='':
                  self.tableflag2.append(self.countsemi)
                  self.tablelist2.append(text.strip())
                  self.listcount2+=1
                  
        if '对外担保信息'==(text.strip()):
          self.guaranteeflag=True
        if self.guaranteeflag and self.getdata:
          self.guaranteelist.append(text)
          if text==str(self.countguarantee):
             self.countguarantee+=1   

     
    def readinformation(self, filepath):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        req = urllib2.Request(filepath)
        res = urllib2.urlopen(req)
        html = res.read()
        res.close()
        html = unicode(html, "gb2312").encode("utf8")          
        self.feed(html)
        information={}
        baseinfo={}
        summaryinfo={}
        creditinfo={}
        publicinfo={}
        selectinfo={}
        creditinfo_oneguarantee={}
        root_dic={}
        root_dic['身份信息']=self.getIDCardInfo();
        root_dic['配偶信息']=self.getSpouseCardInfo()
        root_dic['居住信息']=self.getAdressCardInfo()
        root_dic['职业信息']=self.getCareerInfo()
        root_dic['信用提示']=self.getCreditInfo()
        root_dic['逾期(透支)信息汇总']=self.getOverdueInfo()
        root_dic['未结清贷款信息汇总']=self.getOutstandInfo()
        root_dic['未销户贷记卡信息汇总']=self.getCreditCardInfo()
        root_dic['未销户准贷记卡信息汇总']=self.getSemiCreditCardInfo()
        root_dic['对外担保信息汇总']=self.getExternalInfo()
        root_dic['住房公积金参缴记录']=self.getHouseFundInfo()
        root_dic['查询记录汇总']=self.getAllSelectInfo()
        root_dic['信贷审批查询记录明细']=self.getSelectRecordInfo()
        root_dic['贷款'] = self.getLoanInfo()   # hava problem
        root_dic['贷记卡'] = self.getAllCreditInfo()
        root_dic['准贷记卡'] = self.getAllSemiCard()
        root_dic['对外担保信息'] = self.getGuaranteeInfo()
        root_dic['查询基本信息']=self.getQueryOperation()
        baseinfo['身份信息']=root_dic['身份信息']
        baseinfo['配偶信息']=root_dic['配偶信息']
        baseinfo['居住信息']=root_dic['居住信息']
        baseinfo['职业信息']=root_dic['职业信息']
        summaryinfo_onedue={}
        summaryinfo_onecredit={}
        summaryinfo_onedue['逾期(透支)信息汇总']=root_dic['逾期(透支)信息汇总']
        summaryinfo_onecredit['未结清贷款信息汇总']=root_dic['未结清贷款信息汇总']
        summaryinfo_onecredit['未销户贷记卡信息汇总']=root_dic['未销户贷记卡信息汇总']
        summaryinfo_onecredit['未销户准贷记卡信息汇总']=root_dic['未销户准贷记卡信息汇总']
        summaryinfo_onecredit['对外担保信息汇总']=root_dic['对外担保信息汇总']
#        creditinfo_oneguarantee['对外担保信息']=root_dic['对外担保信息']
        summaryinfo['信用提示']=root_dic['信用提示']
        summaryinfo['逾期及违约信息概要']=summaryinfo_onedue
        summaryinfo['授信及负债信息概要']=summaryinfo_onecredit
        creditinfo['贷款']=root_dic['贷款']
        creditinfo['贷记卡']=root_dic['贷记卡']
        creditinfo['准贷记卡']=root_dic['准贷记卡']
        creditinfo['担保信息']=root_dic['对外担保信息']
        publicinfo['住房公积金参缴记录']=root_dic['住房公积金参缴记录']
        selectinfo['查询记录汇总']=root_dic['查询记录汇总']
        selectinfo['信贷审批查询记录明细']=root_dic['信贷审批查询记录明细']
        information['个人基本信息']=baseinfo
        information['信息概要']=summaryinfo
        information['信贷交易信息明细']=creditinfo
        information['公共信息明细']=publicinfo
        information['查询记录']=selectinfo
        information['查询基本信息']=root_dic['查询基本信息']
        return information
    def getQueryOperation(self):    #获取查询操作信息
        idCardInfo = {};
        if not self.queryoperationlist:
            return idCardInfo       #by zhulei
        str1=''.join(self.queryoperationlist[0])
        str2=''.join(self.queryoperationlist[1])
        str3=''.join(self.queryoperationlist[2])
        idCardInfo['报告编号']=str1.split(':')[1]
        idCardInfo['查询请求时间']=str2.split(':')[1]
        idCardInfo['报告时间']=str3.split(':')[1]
        idCardInfo['被查询者姓名']=self.queryoperationlist[8]
        idCardInfo['被查询者证件类型']=self.queryoperationlist[9]
        idCardInfo['被查询者证件号码']=self.queryoperationlist[10]
        idCardInfo['查询操作员']=self.queryoperationlist[11]
        idCardInfo['查询原因']=self.queryoperationlist[12] 
        self.queryoperationlist=[]
        return idCardInfo  
    def getIDCardInfo(self):
        idCardInfo = {}
        if not self.userlist:
            return idCardInfo       #by zhulei
        idCardInfo['性别'] = self.userlist[9]
        idCardInfo['出生日期'] = self.userlist[10]
        idCardInfo['婚姻状况'] = self.userlist[11]
        idCardInfo['手机号码'] = self.userlist[12]
        idCardInfo['单位电话'] = self.userlist[13]
        idCardInfo['住宅电话'] = self.userlist[14]
        idCardInfo['学历'] = self.userlist[15]
        idCardInfo['学位'] = self.userlist[16]
        idCardInfo['通讯地址'] = self.userlist[19]
        idCardInfo['户籍地址'] = ''.join(self.userlist[20]).strip()
        self.userlist = []
        return idCardInfo
    
    def getSpouseCardInfo(self):
        idCardInfo = {};
        if not self.spouselist:
            return idCardInfo       #by zhulei
        idCardInfo['配偶姓名'] = self.spouselist[6]
        idCardInfo['配偶证件类型'] = self.spouselist[7]
        idCardInfo['配偶证件号码'] = self.spouselist[8]
        idCardInfo['配偶工作单位'] = self.spouselist[9]
        idCardInfo['配偶联系电话'] = self.spouselist[10]
        self.spouselist = []
        return idCardInfo
    
    def getAdressCardInfo(self):

         stayinfo = []
         if not self.adresslist:
            return stayinfo       #by zhulei
         count = (len(self.adresslist) - 1) / 4 - 1
         for index in range(count):        
            stayinfo.append({'编号':self.adresslist[(index + 1) * 4 + 1], '居住地址':self.adresslist[(index + 1) * 4 + 2], \
                            '居住状况':self.adresslist[(index + 1) * 4 + 3], '信息更新日期':self.adresslist[(index + 1) * 4 + 4]})
         self.adresslist = []  
         return stayinfo
     
    def getCareerInfo(self):
         stayinfo = [] 
         if not self.careerlist:
            return stayinfo       #by zhulei
         for index in range(self.count - 1): 
            stayinfo.append({'编号':self.careerlist[4 + index * 3], '工作单位':self.careerlist[5 + index * 3],
                             '单位地址':self.careerlist[6 + index * 3], \
                             '职业':self.careerlist[6 + (self.count - 2) * 3 + 9 + index * 7], \
                             '行业':self.careerlist[6 + (self.count - 2) * 3 + 10 + index * 7],
                             '职务':self.careerlist[6 + (self.count - 2) * 3 + 11 + index * 7], \
                             '职称':self.careerlist[6 + (self.count - 2) * 3 + 12 + index * 7], \
                             '进入本单位年份':self.careerlist[6 + (self.count - 2) * 3 + 13 + index * 7], \
                             '信息更新日期':self.careerlist[6 + (self.count - 2) * 3 + 14 + index * 7]}) 
         self.careerlist = []
         return stayinfo
     
    def getCreditInfo(self):
        idCardInfo = {};
        if not self.creditlist:
            return idCardInfo       #by zhulei
#by zhulei 
#这个地方出现的问题就是，在信用提示页面html中，字段在表格中会分行，而且现有的页面版本中，有时是22个字段(可以用len(self.creditlist)进行查看)
#将这两种情况分情形取值，如果还有其他情况可以直接在下面添加
        
        if 29 == len(self.creditlist):              #长度为29版本
            idCardInfo['住房贷款笔数'] = self.creditlist[20]   #
            idCardInfo['其他贷款笔数'] = self.creditlist[21]
            idCardInfo['首笔贷款发放月份'] = self.creditlist[22]
            idCardInfo['贷记卡账户数'] = self.creditlist[23]
            idCardInfo['首张贷记卡发卡月份'] = self.creditlist[24]
            idCardInfo['准贷记卡账户数'] = self.creditlist[25]
            idCardInfo['首张准贷记卡账户数发卡月份'] = self.creditlist[26]
            idCardInfo['本人声明数目'] = self.creditlist[27]
            idCardInfo['异议标注数目'] = self.creditlist[28]
            self.creditlist = []
        else:                                       #长度为22，没有考虑'个人商用房信息'
            idCardInfo['住房贷款笔数'] = self.creditlist[12]   #
            idCardInfo['其他贷款笔数'] = self.creditlist[14]
            idCardInfo['首笔贷款发放月份'] = self.creditlist[15]
            idCardInfo['贷记卡账户数'] = self.creditlist[16]
            idCardInfo['首张贷记卡发卡月份'] = self.creditlist[17]
            idCardInfo['准贷记卡账户数'] = self.creditlist[18]
            idCardInfo['首张准贷记卡账户数发卡月份'] = self.creditlist[19]
            idCardInfo['本人声明数目'] = self.creditlist[20]
            idCardInfo['异议标注数目'] = self.creditlist[21]
            self.creditlist = []
        return idCardInfo
    
    def getOverdueInfo(self):
        stayinfo = [] 
        if not self.overduelist:
            return stayinfo         #by zhulei
        if len(self.overduelist)>0:
            over1 = {'笔数':self.overduelist[28], '月份数':self.overduelist[29], '单月最高逾期总额':self.overduelist[30], '最长逾期月数':self.overduelist[31]}
            over2 = {'笔数':self.overduelist[32], '月份数':self.overduelist[33], '单月最高逾期总额':self.overduelist[34], '最长逾期月数':self.overduelist[35]}
            over3 = {'笔数':self.overduelist[36], '月份数':self.overduelist[37], '单月最高透支余额':self.overduelist[38], '最长逾期透支月数':self.overduelist[39]}
            stayinfo.append(over1)
            stayinfo.append(over2)
            stayinfo.append(over3)
            self.overduelist = []
        return stayinfo
    
    def getOutstandInfo(self):
        idCardInfo = {};
        if not self.outstandlist:
            return idCardInfo       #by zhulei
        if len(self.outstandlist)>0:
            idCardInfo['贷款法人机构数'] = self.outstandlist[7]
            idCardInfo['贷款机构数'] = self.outstandlist[8]
            idCardInfo['笔数'] = self.outstandlist[9]
            idCardInfo['合同总额'] = self.outstandlist[10]
            idCardInfo['余额'] = self.outstandlist[11]
            idCardInfo['最近6个月平均应还款'] = self.outstandlist[12]
            self.outstandlist = []
        return idCardInfo
    
    def getCreditCardInfo(self):
        
        idCardInfo = {};
        
        if not self.creditcardlist:
            return idCardInfo       #by zhulei

        if len(self.creditcardlist)>0:
            idCardInfo['发卡法人机构数'] = self.creditcardlist[15]
            idCardInfo['发卡机构数'] = self.creditcardlist[16]
            idCardInfo['账户数'] = self.creditcardlist[17]
            idCardInfo['授信总额'] = self.creditcardlist[18]
            idCardInfo['单家行最高授信额'] = self.creditcardlist[19]
            idCardInfo['单家行最低授信额'] = self.creditcardlist[21]
            idCardInfo['已用额度'] = self.creditcardlist[22]
            idCardInfo['最近6个月平均使用额度'] = self.creditcardlist[24]
            self.creditcardlist=[]
        return idCardInfo 
    
    def getSemiCreditCardInfo(self):
      
        idCardInfo = {}
        
        if not self.semicreditlist:
            return idCardInfo       #by zhulei

        if len(self.semicreditlist)>0:
            idCardInfo['发卡法人机构数'] = self.semicreditlist[15]
            idCardInfo['发卡机构数'] = self.semicreditlist[16]
            idCardInfo['账户数'] = self.semicreditlist[17]
            idCardInfo['授信总额'] = self.semicreditlist[18]
            idCardInfo['单家行最高授信额'] = self.semicreditlist[19]
            idCardInfo['单家行最低授信额'] = self.semicreditlist[21]
            idCardInfo['透支余额'] = self.semicreditlist[22]
            idCardInfo['最近6个月平均使用额度'] = self.semicreditlist[24]
            self.semicreditlist = []
        return idCardInfo
    
    def getExternalInfo(self):
        idCardInfo = {}
        if not self.externallist:
            return idCardInfo       #by zhulei
        if len(self.externallist)>0:
            idCardInfo['担保笔数'] = self.externallist[4]
            idCardInfo['担保金额'] = self.externallist[5]
            idCardInfo['担保本金余额'] = self.externallist[6]
            self.externallist = []
        return idCardInfo
    def getHouseFundInfo(self):
        idCardInfo = {}
        if not self.housefundlist:
            return idCardInfo       #by zhulei
        if len(self.housefundlist)>0:
            idCardInfo['参缴地'] = self.housefundlist[9]
            idCardInfo['参缴日期'] = self.housefundlist[10]
            idCardInfo['初缴月份'] = self.housefundlist[11]
            idCardInfo['缴至月份'] = self.housefundlist[12]
            idCardInfo['缴费状态'] = self.housefundlist[13]
            idCardInfo['月缴存额'] = self.housefundlist[14]
            idCardInfo['个人缴存比例'] = self.housefundlist[15]
            idCardInfo['单位缴存比例'] = self.housefundlist[16]
            idCardInfo['缴费单位'] = self.housefundlist[19]
            idCardInfo['信息更新日期'] = self.housefundlist[20]
            self.housefundlist = []
        return idCardInfo
    def getAllSelectInfo(self):
        stayinfo = []
        if not self.allselectlist:
            return stayinfo         #by zhulei
        if len(self.allselectlist)>0:
            stayinfo.append({'贷款审批':self.allselectlist[11], '信用卡审批':self.allselectlist[12]})
            stayinfo.append({'贷款审批':self.allselectlist[13], '信用卡审批':self.allselectlist[14]})
            stayinfo.append({'贷后管理':self.allselectlist[15], '担保资格审查':self.allselectlist[16], '特约商户实名审查':self.allselectlist[17]})
            self.allselectlist = []
        return stayinfo
    def getSelectRecordInfo(self):
        stayinfo = [] 
        if not self.selectrecordlist:
            return stayinfo             #by zhulei
        if len(self.selectrecordlist)>0:     
            for index in range((len(self.selectrecordlist) - 5) / 4):
                stayinfo.append({'编号':self.selectrecordlist[(index + 1) * 4 + 1], \
                                 '查询日期':self.selectrecordlist[(index + 1) * 4 + 2], \
                                 '查询操作员':self.selectrecordlist[(index + 1) * 4 + 3], \
                                 '查询原因':self.selectrecordlist[(index + 1) * 4 + 4]})
            self.selectrecordlist = []
        return stayinfo
    
    def getLoanInfo(self):

# by zhulei  2016/8/25     
        data=[]
        tablelistflag=[]
        tableinfo=[]      #用来存经过处理后生成的表格字典信息
        if not self.info:
            return data
        while(0 in self.listcountflag):
          self.listcountflag.remove(0)
        countflag = 0
        for i, j in enumerate(self.listcountflag):      #取出分割的多个表格内容
               end = j+countflag
               start = end - j 
               tablelistflag.append(self.tablelist[start:end])
               countflag = end 
        #对分割的表格进行匹配格式，分三种情况进行考虑，!!!!!!!!其他情况还没遇到，遇到可以在下面添加,并生成字典
        for index in range(len(tablelistflag)):
            if '五级分类' in tablelistflag[index]:
                ran = range(len(tablelistflag[index]))   #表的长度范围
                for seq in ran:                          #向后匹配
                    if '剩余还'== tablelistflag[index][seq] or '最近一次'==tablelistflag[index][seq] or '逾期31-60天'==tablelistflag[index][seq] or '逾期61－90天'==tablelistflag[index][seq]  or '逾期91－180天'== tablelistflag[index][seq] or '逾期180天以'== tablelistflag[index][seq]:         #重要！！:要复制html内容匹配，因为有些字符分全角半角等
                       temp = tablelistflag[index][seq+1]
                       tablelistflag[index][seq]=tablelistflag[index][seq]+temp
                       tablelistflag[index].remove(temp)    #将匹配到的一个词后面删除，比如是'剩余还'+'款期数','款期数'是要删除的
                       ran.pop()                         #删除一个元素，长度也该减少1
                length = len(tablelistflag)
                repay = tablelistflag[index][length-26:]            #还款记录是在最后，直接切片
                repay = ''.join(repay)                              #转字符串
                addlen = 0
                if '账户状态' in tablelistflag[index]:      #如果存在账户状态信息，长度加1
                    addlen = 1
                key1 = tablelistflag[index][:7+addlen] 
                key2 = tablelistflag[index][14+2*addlen:20+2*addlen]              #分别取出名称和相应的值，因为长度固定
                value1 = tablelistflag[index][7+addlen:14+addlen] 
                value2 = tablelistflag[index][20+2*addlen:27+addlen]
                temp1 = dict(zip(key1,value1))
                temp = dict(zip(key2,value2))
                temp = dict(temp,**temp1)
                temp['还款记录'] = repay                                           #将还款记录添加到表格内容
                tableinfo.append(temp)                                          #内容合并到一起
            elif  '特殊交易类型' in tablelistflag[index]:
                if '逾期月份' in tablelistflag[index]:
                    key = tablelistflag[index][1:4]
                    end = tablelistflag[index].index('特殊交易类型')    #数据是在‘交易类型’前
                    value = tablelistflag[index][7:end]
                    a={'逾期记录':value}
                    start = end
                    key1= tablelistflag[index][end:end+5]
                    value1 = tablelistflag[index][end+5:]
                    temp = dict(zip(key1,value1))
                    temp = dict(temp,**a)                               #将逾期记录合并到一起
                    tableinfo.append(temp)                                 #将结果封装
                else:
                    for it in tablelistflag[index]:
                        key = tablelistflag[index][:5]                  #只有特殊交易信息，占5个
                        value = tablelistflag[index][5:]
                        temp = dict(zip(key,value))
                    tableinfo.append(temp)
        
        tableflag=list(set(self.tableflag))                                  #去除重复数据,
        for its in range(len(self.info)):                                    #tablelist记录的是表格出现在贷款记录的位置
            temp = self.cutString(self.info[its])
            if its+1 in tableflag:                                             #当出现tablelist记录的表格位置时，就将表格附进去,因为计算从0开始，所以要+1
               pos = tableflag.index(its+1)
               if pos<len(tableinfo):
                  temp['表格'] = tableinfo[pos]
            data.append(temp)
        return data
   
    def getAllCreditInfo(self):
# by zhulei 2016/8/26        
        data=[]
        tablelistflag=[]        #截取每个表格信息
        tableinfo=[]
        if not self.info1:
            return data         #by zhulei
        while(0 in self.listcountflag1):            #移除里面为0元素
          self.listcountflag1.remove(0)
        tablePos=list(set(self.tableflag1))         #这是表格位置，是哪条记录的表格
        lent = len(tablePos)                        #有几个记录表格就在表格内容取几个
        flag = self.listcountflag1[:lent]           #因为有些表内容多了，只能取相应长度的
        countflag  = 0
        for i, j in enumerate(flag):      #取出分割的多个表格内容
               end = j+countflag
               start = end - j 
               tablelistflag.append(self.tablelist1[start:end])
               countflag = end 

        #对分割的表格进行匹配格式，分三种情况进行考虑，!!!!!!!!其他情况还没遇到，遇到可以在下面添加,并生成字典
        for index in range(len(tablelistflag)):
            if '已用额度' in tablelistflag[index]:
                ran = range(len(tablelistflag[index]))   #表的长度范围
                length = len(tablelistflag)
                key1 = tablelistflag[index][:5] 
                value1 = tablelistflag[index][5:10] 
                key2 = tablelistflag[index][10:15]              #分别取出名称和相应的值，因为长度固定
                value2 = tablelistflag[index][15:20]
                repay = tablelistflag[index][21:45]            #还款记录是在最后，直接切片
                repay = ''.join(repay)                              #转字符串
                temp1 = dict(zip(key1,value1))
                temp = dict(zip(key2,value2))
                temp = dict(temp,**temp1)
                temp['还款记录'] = repay                                           #将还款记录添加到表格内容
                if '逾期月份' in tablelistflag[index]:
                    pos = tablelistflag[index].index('逾期月份')
                    value = tablelistflag[index][pos+6:]
                    a = {'逾期记录':value}
                    temp = dict(temp,**a)
                tableinfo.append(temp)                                          #内容合并到一起
                
            elif  '逾期月份' in tablelistflag[index]:
                value = tablelistflag[index][7:]                         #只有逾期记录，数据在第七个位置后面
                a = {'逾期记录':value}
                tableinfo.append(a)
        for its in range(len(self.info1)):                                    #tablelist记录的是表格出现在贷款记录的位置
            temp = self.CutCreditCard(self.info1[its])
            if its+1 in tablePos:                                             #当出现tablelist记录的表格位置时，就将表格附进去,因为计算从0开始，所以要+1
               pos = tablePos.index(its+1)
               if pos<len(tableinfo):
                   temp['表格'] = tableinfo[pos]
            data.append(temp)
        return data

    def getAllSemiCard(self):
#by zhulei 2016/8/27        
        data=[]
        tablelistflag=[]        #截取每个表格信息
        tableinfo=[]
        if not self.info1:
            return data         #by zhulei
        while(0 in self.listcountflag2):            #移除里面为0元素
          self.listcountflag2.remove(0)
        tablePos=list(set(self.tableflag2))         #这是表格位置，是哪条记录的表格
        lent = len(tablePos)                        #有几个记录表格就在表格内容取几个
        flag = self.listcountflag2[:lent]           #因为有些表内容多了，只能取相应长度的
        countflag  = 0
        for i, j in enumerate(flag):      #取出分割的多个表格内容
               end = j+countflag
               start = end - j 
               tablelistflag.append(self.tablelist2[start:end])
               countflag = end 
        for index in range(len(tablelistflag)):
                if '共享额度' in tablelistflag[index]:
                     key1 = ['共享额度','透支余额','最近六个月平均透支余额','最大透支余额','账单日','本月实还款','最近一次还款日期','透支180天以上未付余额','还款日期']
                else:
                     key1 = ['账户状态','透支余额','最近六个月平均透支余额','最大透支余额','账单日','本月实还款','最近一次还款日期','透支180天以上未付余额','还款日期']
                length=len(tablelistflag[index])
                value1 = tablelistflag[index][length-33:length-25]          #从后面开始计算
                repay = tablelistflag[index][length-23:]            #还款记录是在最后，直接切片
                repay = ''.join(repay)                              #转字符串
                temp = dict(zip(key1,value1))
                temp['还款记录'] = repay                                           #将还款记录添加到表格内容
                tableinfo.append(temp)                                          #内容合并到一起
                
        for its in range(len(self.info2)):                                    #tablelist记录的是表格出现在贷款记录的位置
            temp = self.CutCreditCard(self.info2[its])
            if its+1 in tablePos:                                             #当出现tablelist记录的表格位置时，就将表格附进去,因为计算从0开始，所以要+1
               pos = tablePos.index(its+1)
               if pos<len(tableinfo):
                   temp['表格'] = tableinfo[pos]
            data.append(temp)
        return data

    def getGuaranteeInfo(self):
        stayinfo=[]
        if not self.guaranteelist:
            return stayinfo             #by zhulei
        for index in range(self.countguarantee-1):
            stayinfo.append({ '编号':self.guaranteelist[17+index*9],\
                                   '担保贷款发放机构':self.guaranteelist[18+index*9],\
                                   '担保贷款合同金额':self.guaranteelist[19+index*9],\
                                   '担保贷款发放日期':self.guaranteelist[20+index*9],\
                                   '担保贷款到期日期':self.guaranteelist[21+index*9],\
                                   '担保金额':self.guaranteelist[22+index*9],\
                                   '担保贷款本金余额':self.guaranteelist[23+index*9],\
                                   '担保贷款五级分类':self.guaranteelist[24+index*9],\
                                   '结算日期':self.guaranteelist[25+index*9]})
        return stayinfo   
        
     
    def CutCreditCard(self,string):
# by zhulei 2016/8/25
        str_temp = string.decode('utf-8')
        data={}

        start = str_temp.find('日')+1
        start2 = str_temp.find('.') +1              #因为当贷记卡数超过9条时，就不是从2开始了
        data['日期'] = str_temp[start2:start]      #日期的位置
        end = str_temp.find('发放的')
        search = str_temp[start:end]      #切片，查找到机构
        data['机构'] = search[search.find('“')+1:search.find('”')] #对查找的机构内容处理，去引号里面内容
        
        #在实际中'()'括号有可能是中文，有可能是英文，难以区分。由于账户类型差不多为人民币账户、欧元账户、美元账户、若有新类型可以添加
        if '人民币账户' in str_temp:
            data['账户类型'] = '人民币账户'
        if '欧元账户' in str_temp:
            data['账户类型'] = '欧元账户'
        if '美元账户' in str_temp:
            data['账户类型'] = '美元账户'
        
        start = str_temp.find('业务号') + 3
        end = str_temp.find('，',start)         #在业务号后面开始找到第一个逗号，截取
        data['业务号'] = str_temp[start:end]

        start = str_temp.find('授信额度') + 4
        end = str_temp.find('，',start)
        money = str_temp[start:end]
        if '币' in money:                          #里面存在诸如'折合人民币','人民币'都需要剔除
            start = money.find('币')
            money = money[start+1:]
        data['授信额度'] = money
        
        if '共享授信额度' in str_temp:
            start = str_temp.find('共享授信额度') + 6
            end = str_temp.find('，',start)
            money = str_temp[start:end]
            if '币' in money:                          #里面存在诸如'折合人民币','人民币'都需要剔除
                start = money.find('币')
                money = money[start+1:]
            data['共享授信额度'] = money
        else:
            data['共享授信额度'] = ''          #不存在时，为空

        start = end + 1       #从授信额度后面的逗号开始找
        end = str_temp.find('担保') + 2
        data['担保方式'] = str_temp[start:end]

        start = end + 1         #从担保方式逗号后面找
        new_str = str_temp[start:]      #对后面的部分单独处理，情况复杂
        mid = new_str.find('月')         #以'月'分开，从两边开始找截止日期和账户状态
        year_mon = new_str[mid-7:mid+1]         #找到年月
        if '日' in new_str:
            data['截止日期'] = year_mon + new_str[mid+1:mid+4]      #后面存在日
        else:
            data['截止日期'] = year_mon
        
        data['账户状态'] = ''                 #初始化账户状态为空
        if '销户' in new_str:
            data['账户状态'] = '销户'         #只考虑到了这两种账户状态，要是还有其他类型，可直接if添加 
        if '尚未激活' in new_str:
            data['账户状态'] = '尚未激活'

        return data

    def cutString(self, spiltstring):
#       by zhulei 2016/8/24

        str_temp=spiltstring.decode('utf-8')
        data={}
        start = str_temp.find('日')+1
        start2 = str_temp.find('.') +1              #因为当贷记卡数超过9条时，就不是从2开始了
        data['日期'] = str_temp[start2:start]      #日期的位置
        end = str_temp.find('发放的')
        search = str_temp[start:end]      #切片，查找到机构
        data['机构'] = search[search.find('“')+1:search.find('”')] #对查找的机构内容处理，去引号里面内容
       
        start = end+3                           #因为find函数找出的位置是第一个匹配，所以需要右移三个位置
        end = str_temp.find('（')
        data['金额'] = str_temp[start:end]
       
        start = str_temp.find('）')+1
        end = str_temp.find('，业务号')
        data['贷款类型'] = str_temp[start:end]
        
        start = end +4
        end = str_temp.find('，',end+3)           #从业务号后面开始查找第一个逗号停止
        data['业务号'] = str_temp[start:end]
        
        start = end + 1
        end = str_temp.find('，',start)
        data['抵押担保']=str_temp[start:end]
       
       #逗号之间的归还方式可能包含期数，所以要特殊处理
        start = end + 1
        end = str_temp.find('归还',start)
        search = str_temp[start:end+2]
        data['期数']=''             #初始期数为空
        if '期，' in search:        #说明里面有期数
            data['期数'] = search[:search.find('，')]
            data['归还方式']=search[search.find('，')+1:]
        else:
            data['归还方式']=search
        
        data['到期时间']=''
        if '到期' in str_temp:      #是否有到期时间
            end = str_temp.find('到期')
            start = end-11      #日期格式为2001年12月12日占了11个字符，往后数
            data['到期时间']=str_temp[start:end]

        data['截止时间']=''
        if '截至' in str_temp:
            start = str_temp.find('截至')+2     #不包含截至
            end = start+11          
            data['截止时间']=str_temp[start:end]
        else:
            if '结清' in str_temp:   #算截至时间时，结清和截至时间是不同时存在的
                end = str_temp.find('结清')
                start = end - 8
                data['截止时间']=str_temp[start:end]
        return data

