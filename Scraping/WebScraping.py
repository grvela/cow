import time
import re
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

url = "https://web.whatsapp.com/"

option = Options()
option.headless = True
driver = webdriver.Firefox()

driver.get(url)
time.sleep(10)
mensagem=[]
mensagemdict={}
#Numero de Conversas em aberto
element = driver.find_element_by_xpath("/html/head/title").get_attribute('textContent')
Conversa = re.sub('[^0-9]', '', element)
print("numero de conversas em aberto: "+Conversa)

#Numero de mensagem de cada conversa
msgnum = driver.find_elements_by_class_name("_31gEB")
for i in range(int(Conversa)):
    mensagem += list(msgnum[i].get_attribute('textContent'))
    
#Pegando as mensagens de cada conversa
span = driver.find_elements_by_class_name('_325lp')
for i in range (int(Conversa)):
    span[i].click()
    spans = driver.find_elements_by_class_name('eRacY')
    pic_spans =[elem.get_attribute('outerHTML')for elem in spans]
    print(int(str(len(pic_spans))))


#Parseando o conteudo html
    for j in range (int(mensagem[i])):
        soup = BeautifulSoup(pic_spans[int(str(len(pic_spans)))-j-1],'html.parser')
        msg = soup.span.string
        print(msg)
        mensagemdict[str(i)+str(j)]=msg
        print(mensagemdict)

#Criando um Json
js=json.dumps(mensagemdict)
fp = open('resultado.json','w')
fp.write(js)
fp.close()
