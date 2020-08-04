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

#Numero de Conversas em aberto
element = driver.find_element_by_xpath("/html/head/title").get_attribute('textContent')
Conversa = re.sub('[^0-9]', '', element)
print("numero de conversas em aberto: "+Conversa)

#Numero de mensagem de cada conversa
msgnum = driver.find_elements_by_class_name("_31gEB")
for i in range(int(Conversa)):
    teste = msgnum[i].get_attribute('textContent')
    print("Numero de msg em cada conversa :"+teste)

#Pegando as mensagens de cada conversa
span = driver.find_elements_by_class_name('_210SC')
for i in range (int(Conversa)):
    span[i].click()
    spans = driver.find_elements_by_class_name('eRacY')
    pic_spans =[elem.get_attribute('outerHTML')for elem in spans]
#Parseando o conteudo html
    for i in range (int(msgnum[i].get_attribute('textContent'))):
        soup = BeautifulSoup(pic_spans[i],'html.parser')
        msg = soup.span.string
        print(msg)