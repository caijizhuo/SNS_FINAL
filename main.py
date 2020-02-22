from utils import *
import time

countries = get_country_codes('countrycode.txt')
# print(countries)

# url1 = 'https://www.google.com/search?q=filetype:pdf+site:%s&start='
# url = url1 %countries[0] + str(0)
# get_html(url,0)

#get html part------------------------
filenum = 1361
url1 = 'https://www.google.com/search?q=filetype:pdf+site:%s&start='
start = filenum//10
for i in range(start,len(countries)):
    for page_num in range(10):
        url = url1 %countries[i] + str(page_num*10)
        get_html(url,filenum)
        filenum += 1


#get pdf url part------------------------------
# htmlname = 'pages/page%d.html'

# start_num = 1
# for i in range(start_num,1000):
#     html_path = htmlname%i
#     try:
#         res = fetch_pdfurl(html_path)
#         generate_txt(res,'pdfurlfinal.txt')
#     except:
#         pass

# caculate throughput------------------------------
# with open('pdfurl.txt','r') as f:
#     pdfurl = f.readlines()
# pdfurl_total_len = len(pdfurl)
# for i in range(pdfurl_total_len):
#     pdfurl[i] = pdfurl[i].strip()
# index = 0
# #start to end#####################
# for i in range(index,100):
#     try:
#         t = download_pdf(pdfurl[i],i)
#         t = round(t,2)
#         if t:
#             print('tp:',t)
#             with open('tp.txt','a+') as f:
#                 f.write(pdfurl[i]+','+str(t)+'\n')
#     except:
#         pass


