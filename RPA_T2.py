from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
servico = Service(ChromeDriverManager().install())

#Entrar no site
brow = webdriver.Chrome(service=servico)
brow.get(" https://www.rpachallenge.com/")

#Pegar os dados excel
chalege = ("C:/Users/filho/Downloads/challenge.xlsx")
chalege_df = pd.read_excel(chalege)

#--- Automação
for i in range(10):
    #----DADOS
    fn = str(chalege_df.loc[i,'First Name'])
    sn = str(chalege_df.loc[i,'Last Name '])
    cn = str(chalege_df.loc[i,'Company Name'])
    rc = str(chalege_df.loc[i,'Role in Company'])
    ad = str(chalege_df.loc[i,'Address'])
    em = str(chalege_df.loc[i,'Email'])
    pn = str(chalege_df.loc[i,'Phone Number'])


    #----CAMINHO
    brow.find_element(By.XPATH, "//*[@ng-reflect-name='labelFirstName']").send_keys(fn)
    #Sobrenome
    brow.find_element(By.XPATH, "//*[@ng-reflect-name='labelLastName']").send_keys(sn)
    #Company Name 
    brow.find_element(By.XPATH, "//*[@ng-reflect-name='labelCompanyName']").send_keys(cn)
    #Role in Company
    brow.find_element(By.XPATH," //*[@ng-reflect-name='labelRole']").send_keys(rc)
    #Address
    brow.find_element(By.XPATH, "//*[@ng-reflect-name='labelAddress']").send_keys(ad)
    #email
    brow.find_element(By.XPATH, "//*[@ng-reflect-name='labelEmail']").send_keys(em)
    #phone number
    brow.find_element(By.XPATH, "//*[@ng-reflect-name='labelPhone']").send_keys(pn)
    
    #enviar 
    brow.find_element(By.XPATH, "//*[@type='submit']").click()
    print(f"feito ",i) 
