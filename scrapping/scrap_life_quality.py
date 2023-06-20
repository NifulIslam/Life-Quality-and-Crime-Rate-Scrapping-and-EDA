from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import pandas as pd

driver = webdriver.Chrome()


driver.get('https://www.worlddata.info/quality-of-life.php')
table = driver.find_element(By.ID,"lifequality")
headers=[i.text for i in table.find_elements(By.XPATH,'//*[@id="lifequality"]/tbody[1]/tr[1]')]
headers=headers[0]
# remove weight. eg: (15%) 
pattern = r"\([^)]*\)"
headers= re.sub(pattern, " ", headers)
headers= headers.split(" ")
headers=[i.replace('\n', '') for i in headers] # removing all unexpected line breaks
headers=headers[:-1] # an extra element came in

# table data collection
data=table.find_elements(By.TAG_NAME,'tr')
data=data[1:] # first elemet is the header (column name)
values=[]
for row in data:
    ro=row.text.split(" ")
    row_val=[ro[0]]
    name=""
    i=1
    while(not ro[i].isdigit()) : # sometimes countires can have long name like United Arab Emirates
        name += ro[i]
        name+= " "
        i+=1
    name=name[:-1] #removing extra space
    # some countires have * after their name [for specific reason]
    if(name[-1]=='*'):
        name=name[:-2]
    row_val.append(name)
    row_val.extend(ro[i:])
    values.append(row_val)



df= pd.DataFrame(values,columns=headers)
df.to_csv("life_quality_2023.csv",index=False)


driver.close()
