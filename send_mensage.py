import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib

# Lendo o arquivo com os dados
contatos_df = pd.read_excel('Contatos.xlsx')

# Abrindo o navegador
navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

# Lendo o QRCode
while len(navegador.find_elements(By.ID, "side")) < 1:
    time.sleep(1)

#Percorrendo contatos e enviando mensagens
for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i, "Pessoa"]
    numero = contatos_df.loc[i, "Número"]
    texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements(By.ID, "side")) < 1:
        time.sleep(10)
    navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div').send_keys(Keys.ENTER)
    time.sleep(10)