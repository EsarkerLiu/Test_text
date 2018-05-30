# encoding : utf-8

import re

text1 = "一、对被申请人童昌茂、刘惠英所有的位于义乌市xxx路xx号xxxx室的房地产【房屋所有权证号：义乌房权证xx字第c00151xxx号至c00151xxx号，土地使用证号：义乌国用（2008）第1-34xx号】准予采取拍卖、变卖等方式依法变价，申请人义乌市伊美小额贷款股份有限公司对变价后所得款项在借款本金100万元及利息85050元（已算至2015年4月28日，之后按合同约定计付至实际履行完毕之日止）范围内以117万元为限优先受偿"
text2 = "限制对登记在被申请人戴安兵名下坐落于瑞安市塘下镇鲍田上戴村房产（产权证号：××号），办理过户、设定抵押等手续(限制期限为采取保全措施之日起二年，若未办理续限手续，期限届满自动解除)"

res = []
pattern = re.compile(r'(被申请人)(.*)(所有的)')
m1 = re.search(pattern,text1)
if(m1 != None):
	res.append(m1.group(2))

m1_1 = re.search(pattern,text2)
if(m1_1 == None):
	print("Not Found! %s " % pattern)

pattern2 = re.compile(r'(被申请人)(.*)(所有的|名下)')
m2 = re.search(pattern2,text2)
if(m2 != None):
	res.append(m2.group(2))

print(res)
