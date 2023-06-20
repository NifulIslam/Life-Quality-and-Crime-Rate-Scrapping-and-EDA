from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import pandas as pd
def isDigitfloat(x): # because isdigit only works for integers
    try:
        float(x)
        return True
    except ValueError:
        return False

driver = webdriver.Chrome()


driver.get('https://worldpopulationreview.com/country-rankings/crime-rate-by-country')
header= driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/section[2]/div[1]/div/div[1]/div[1]/div[2]/table/thead/tr')
header=[ i.text for i in header.find_elements(By.TAG_NAME,'th')]

body= driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/section[2]/div[1]/div/div[1]/div[1]/div[2]/table/tbody')
rows= [i.text.split(" ") for i in body.find_elements(By.TAG_NAME,'tr')]

data=[]
for ro in rows:
    row_val=[ro[0]]
    name=""
    i=1
    while(not isDigitfloat(ro[i])) : # sometimes countires can have long name like United Arab Emirates
        name += ro[i]
        name+= " "
        i+=1
    name=name[:-1] #removing extra space
    row_val.append(name)
    row_val.extend(ro[i:])
    data.append(row_val)
    data[-1][-1]=data[-1][-1].replace(',','') # digits containing comma may create problems in csv


df= pd.DataFrame(data,columns=header)
df.to_csv("crime_rate_2023.csv",index=False)
    


driver.close()