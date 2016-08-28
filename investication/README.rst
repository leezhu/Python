|个人信用报告：
     |查询基本信息：
          |报告编号
          |查询请求时间 
          |报告时间
          |被查询者姓名
          |被查询者证件类型
          |被查询者证件号码 
          |查询操作员 
          |查询原因 
     |个人基本信息
          |身份信息
          |配偶信息 
          |居住信息
          |职业信息
     |信息概要
          |信用提示
          |逾期及违约信息概要 
                |逾期（透支）信息汇总
          |授信及负债信息概要 
                |未结清贷款信息汇总
                |未销户贷记卡信息汇总
                |未销户准贷记卡信息汇总
                |对外担保信息汇总
     |信贷交易信息明细 
          |贷款
          |贷记卡
          |准贷记卡
          |担保信息
                |对外担保信息
     |公共信息明细
          |住房公积金参缴记录
     |查询记录
          |查询记录汇总
          |信贷审批查询记录明细



filepath="file:C:\person_success.html" 路径格式为："file:+本地路径"
inv = Investication()
allinfo = inv.readinformation(filepath)

queryinfo=allinfo.get('查询基本信息')

      reportnumber=queryinfo.get('报告编号')
      querytime=queryinfo.get('查询请求时间') 
      reporttime=queryinfo.get('报告时间')
      name=queryinfo.get('被查询者姓名')
      credentialtype=queryinfo.get('被查询者证件类型')
      credentialnumber=queryinfo.get('被查询者证件号码'）
      queryoperator=queryinfo.get('查询操作员')
      queryrenson=queryinfo.get('查询原因') 

baseinfo=allinfo.get('个人基本信息 ')
      userinfo=baseinfo.get('身份信息')
                set=userinfo.get('性别')
                birthdate=userinfo.get('出生日期')
                isMarry=userinfo.get('婚姻状况')
                phone=userinfo.get('手机号码')
                unitnumber=userinfo.get('单位电话')
                homenumber=userinfo.get('住宅电话')
                degree=userinfo.get('学历')
                academicdegree=userinfo.get('学位')
                comaddress=userinfo.get('通讯地址')
                address=userinfo.get('户籍地址')
      spouseinfo=baseinfo.get('配偶信息')
                name=spouseinfo.get('姓名')
                docutype=spouseinfo.get('证件类型')
                docunumber=spouseinfo.get('证件号码')
                workunit=spouseinfo.get('工作单位')
                phone=spouseinfo.get('联系电话')
      adressinfo=baseinfo.get('居住信息')
                adressinfo:一个列表，里面存放了居住信息字典
                for item in adressinfo:
                     id=item.get('编号')
                     adress=item.get('居住地址')
                     staytype=item.get('居住状况')
                     updateinformation=item.get('信息更新日期')
      careerinfo=baseinfo.get('职业信息')
                careerinfo:一个列表，里面存放了职业信息字典
                for item in careerinfo:
                     id=item.get('编号')
                     company=item.get('工作单位')
                     adress=item.get('单位地址')
                     titlecareer=item.get('职业')
                     industry=item.get('行业')
                     title=item.get('职务')
                     titlename=item.get('职称')
                     indate=item.get('进入本单位年份')
                     updateinformation=item.get('信息更新日期')

summaryinfo=allinfo.get('信息概要 ')
if summaryinfo:
          creditinfo=summaryinfo.get('信用提示')
          if creditinfo:
                    houseloannumber=creditinfo.get('住房贷款笔数')
                    otherloannumber=creditinfo.get('其他贷款笔数')
                    firstloanmonth=creditinfo.get('首笔贷款发放笔数')
                    creditcardaccount=creditinfo.get('贷记卡账户数')
                    firstcreditcardmonth=creditinfo.get('首张贷记卡发卡月份')
                    semicreditcardaccount=creditinfo.get('准贷记卡账户数')
                    firstsemicreditcardmonth=creditinfo.get('首张准贷记卡账户数发卡月份')
                    declarenumber=creditinfo.get('本人声明数目')
                    Objectionlabenum=creditinfo.get('异议标注数目')
          overtimeinfo=summaryinfo.get('逾期及违约信息概要 ')
          if overtimeinfo:
                    overdueinfo=overtimeinfo.get('逾期（透支)信息汇总')
                    if overdueinfo:
                          overdueinfo:里面存放了逾期（透支)信息汇总字典
                          overdueinfo[0]:贷款逾期
                             count=overdueinfo[0].get('笔数')
                             monthdate=overdueinfo[0].get('月份数')
                             onemonth=overdueinfo[0].get('单月最高逾期总额')
                             maxmonth=overdueinfo[0].get('最长逾期月数')
                          overdueinfo[1]:贷记卡逾期
                             count=overdueinfo[1].get('笔数')
                             monthdate=overdueinfo[1].get('月份数')
                             onemonth=overdueinfo[1].get('单月最高逾期总额')
                             maxmonth=overdueinfo[1].get('最长逾期月数')
                          overdueinfo[2]:准贷记卡60天以上透支
                             count=overdueinfo[1].get('笔数')
                             monthdate=overdueinfo[1].get('月份数')
                             onemonth=overdueinfo[1].get('单月最高透支余额')
                             maxmonth=overdueinfo[1].get('最长逾期透支月数')
        creditbalanceinfo=summaryinfo.get('授信及负债信息概要')
        if  creditbalanceinfo:
                   outstandLoaninfo=creditbalanceinfo.get('未结清贷款信息汇总')
                   if outstandLoaninfo:
                          institutionalnum=outstandLoaninfo.get('贷款法人机构数')
                          lendernum=outstandLoaninfo.get('贷款机构数')
                          number=outstandLoaninfo.get('笔数')
                          totalmoney=outstandLoaninfo.get('合同总额')
                          balance=outstandLoaninfo.get('余额')
                          reimbursement=outstandLoaninfo.get('最近6个月平均应还款')
                  creditcardinfo=creditbalanceinfo.get('未销户贷记卡信息汇总')
                  if creditcardinfo:
                          creditcardissuers=creditcardinfo.get('发卡法人机构数')
                          cardissuers=creditcardinfo.get('发卡机构数')
                          accountnumber=creditcardinfo.get('账户数')
                          totalcredi=creditcardinfo.get('授信总额')
                          maxonebankcredi=creditcardinfo.get('单家行最高授信额')
                          minonebankcredi=creditcardinfo.get('单家行最低授信额')
                          usedquota=creditcardinfo.get('已用额度')
                          averageamount=creditcardinfo.get('最近6个月平均使用额度')

                  semicreditCardinfo=creditbalanceinfo.get('未销户准贷记卡信息汇总')
                  if semicreditCardinfo:
                          creditcardissuers=semicreditCardinfo.get('发卡法人机构数')
                          cardissuers=semicreditCardinfo.get('发卡机构数')
                          accountnumber=semicreditCardinfo.get('账户数')
                          totalcredi=semicreditCardinfo.get('授信总额')
                          maxonebankcredi=semicreditCardinfo.get('单家行最高授信额')
                          minonebankcredi=semicreditCardinfo.get('单家行最低授信额')
                          overdraftbalance=semicreditCardinfo.get('透支余额')
                          averageamount=semicreditCardinfo.get('最近6个月平均使用额度')
    
                  externalguaranteinfo=creditbalanceinfo.get('对外担保信息汇总')
                  if externalguaranteinfo:
                          guaranteenum=externalguaranteinfo.get('担保笔数')
                          guaranteeamount=externalguaranteinfo.get('担保金额')
                          guaranteeprincipal=externalguaranteinfo.get('担保本金余额')
                         
creditinfo=allinfo.get('信贷交易信息明细')
if creditinfo:
          loaninfo=creditinfo.get('贷款')
          if loaninfo:
                  loaninfo:一个列表，存放贷款信息
                  for item in loaninfo:
                      date=item.get('日期')
                      institution=item.get('机构')
                      money=item.get('金额')
                      loantype=item.get('贷款类型')
                      businessnumber=item.get('业务号')
                      guaranteetype=item.get('抵押担保')
                      periods=item.get('期数')
                      repaymenttype=item.get('归还方式')
                      expiredate=item.get('到期时间')
                      overdate=item.get('截止时间')
                      tableinfo=item.get('表格1')
                           type=tableinfo.get（'特殊交易类型'）
                           date=tableinfo.get（'发生日期'）
                           changemonth=tableinfo.get（'变更月数'）
                           money=tableinfo.get（'发生金额'）
                           record=tableinfo.get（'明细记录'）
                      nonscheduletable=loaninfo.get('表格2')
                           classify=nonscheduletable.get('五级分类')
                           principalbalance=nonscheduletable.get('本金余额')
                           paymentperiods=nonscheduletable.get('剩余还款期数')
                           monrepayment=nonscheduletable.get('本月应还款')
                           repaymentdate=nonscheduletable.get('应还款日')
                           truthrepayment=nonscheduletable.get('本月实还款')
                           lastrepayment=nonscheduletable.get('最近一次还款日期')
                           nowdelinquency=nonscheduletable.get('当前逾期期数')
                           delinquencymoney=nonscheduletable.get('当前逾期金额')
                           sixtyday=nonscheduletable.get('逾期31-60天未还本金')
                           ninetyday=nonscheduletable.get('逾期61－90天未还本金')
                           onehundredeighty=nonscheduletable.get('逾期91－180天未还本金')
                           overonehundred=nonscheduletable.get('逾期180天以上未还本金')
                           paymentrecord=nonscheduletable.get('还款记录')

          allcreditinfo=creditinfo.get('贷记卡')
          if allcreditinfo:
                  allcreditinfo:一个列表，存放贷款信息
                  for item in allcreditinfo:
                      date=item.get('时间')
                      institution=item.get('机构')
                      accounttype=item.get('账户类型')
                      businessnumber=item.get('业务号')
                      lineofcredit=item.get('授信额度')
                      guaranteetype=item.get('担保方式')
                      lasttime=item.get('截止时间')
                      tableinfo=item.get('表格')
                           totaldquota=tableinfo.get('共享额度')
                           usedquota=tableinfo.get('已用额度')
                           averageused=tableinfo.get('最近6个月平均使用额度')
                           maxquota=tableinfo.get('最大使用额度')
                           repayment=tableinfo.get('本月应还款')
                           billday=tableinfo.get('账单日')
                           truthrepayment=tableinfo.get('本月实还款')
                           recentrepayment=tableinfo.get('最近一次还款日期')
                           lateperiodnumber=tableinfo.get('当前逾期期数')
                           lateperiodmoney=tableinfo.get('当前逾期金额')
                           repaymentrecord=tableinfo.get('还款记录')
                           periodrecord=tableinfo.get('逾期记录')
                           periodrecord:一个列表，里面存放逾期记录信息
                                  month=periodrecord.get('逾期月份')
                                  months=periodrecord.get('逾期持续月数')
                                  money=periodrecord.get('逾期金额')
          allSemicreditinfo=creditinfo.get('准贷记卡')
          if allSemicreditinfo:
                 allSemicreditinfo:一个列表，存放贷款信息
                 for item in allSemicreditinfo
                 date=item.get('时间')
                 institution=item.get('机构')
                 accounttype=item.get('账户类型')
                 businessnumber=item.get('业务号')
                 lineofcredit=item.get('授信额度')
                 guaranteetype=item.get('担保方式')
                 lasttime=item.get('截止时间') 
                 tableinfo=item.get('表格')
                      totaldquota=tableinfo.get('共享金额')
                      overdrawnquota=tableinfo.get('透支余额‘)
                      averageused=tableinfo.get('最近6个月平均透支余额')
                      maxquota=tableinfo.get('最大透支余额')
                      billday=tableinfo.get('账单日')
                      truthrepayment=tableinfo.get('本月实还款')
                      recentrepayment=tableinfo.get('最近一次还款日期')
                      longtimenorepay=tableinfo.get('透支180天以上未付余额')
                      repaymentrecord=tableinfo.get('还款记录')

          guaranteeinfo=creditinfo.get('担保信息')
          if guaranteeinfo:
                         outguarantee=uaranteeinfo.get('对外担保信息')
                                 if outguarantee:
                                         outguarantee:一个列表，里面存放担保信息
                                         for item in outguarantee:
                                                  id=item('编号')
                                                  lender=item('担保贷款发放机构')
                                                  amount=item('担保贷款合同金额')
                                                  grantdate=item('担保贷款发放日期')
                                                  datedue=item('担保贷款到期日期')
                                                  grantmoney=item('担保金额')
                                                  capitalbalance=item('担保贷款本金余额')
                                                  category=item('担保贷款五级分类')
                                                  balancedate=item('结算日期')

publicinfo=allinfo.get('公共信息明细')
if publicinfo：
          ousefundinfo=publicinfo.get('住房公积金参缴记录')
          if ousefundinfo:
                  location=ousefundinfo.get('参缴地')
                  date=ousefundinfo.get('参缴日期')
                  startmonth=ousefundinfo.get('初缴月份')
                  lastmonth=ousefundinfo.get('缴至月份')
                  state=ousefundinfo.get('缴费状态')
                  monthpayment=ousefundinfo.get('月缴存额')
                  individualscale=ousefundinfo.get('个人缴存比例')
                  companyscale=ousefundinfo.get('单位缴存比例')
                  paycostunit=ousefundinfo.get('缴费单位')
                  updateinfo=ousefundinfo.get('信息更新日期')

                           
selectinfo=allinfo.get('查询记录')
if selectinfo：
         allselectinfo=selectinfo('查询记录汇总')
         if allselectinfo:
              allselectinfo:一个列表，里面存放了查询记录汇总的字典   
              allselectinfo[0]:最近一个月的查询机构数
                    loanapproval=allselectinfo[0].get('贷款审批')
                    creditcardapproval=allselectinfo[0].get('信用卡审批')
              allselectinfo[1]:最近一个月的查询次数
                    loanapproval=allselectinfo[1].get('贷款审批')
                    creditcardapproval=allselectinfo[1].get('信用卡审批')
              allselectinfo[2]:最近两年内的查询次数
                    postloanmanagement=allselectinfo[2].get('贷后管理')
                    guarantee=allselectinfo[2].get('担保资格审查')
                    realnamereview=allselectinfo[2].get('特约商户实名审查')

         selectrecordinfo=selectinfo('信贷审批查询记录明细')
         if selectrecordinfo:
              selectrecordinfo:一个列表，里面存放了信贷审批查询记录明细的字典   
              for item in selectrecordinfo:
                    id=item.get('编号')
                    date=item.get('查询日期')
                    queryoperator=item.get('查询操作员')
                    reason=item.get('查询原因')

  
