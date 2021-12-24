# 1st step install and import modules
 #-- pip/pip3 install lxml
 #-- pip/pip3 install requests
 #-- pip/pip3 install beautifulsoup
 
# https://wuzzuf.net/search/jobs/?q=python&a=hpb

import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

## our empty lists
job_title = []
company_name = []
location_name = []
job_skill = []

# 2nd step use request to fetch the url
result = requests.get('https://wuzzuf.net/search/jobs/?q=python&a=hpb') 

# 3rd step save page content/markup
src = result.content
#print(src)              # dirty data

# 4th step create soup object to parse content
soup = BeautifulSoup(src, 'lxml')       # need to parameters (page , 'lxml') , now we able to make operation on pages
#print(soup)

# 5th step find the elements containing info we need
#-- job titles, job skills, company names, location names
#-- result of find_all == list

#job_titles = soup.find('a',class_="css-o171kl").text
# or
#job_titles = soup.find_all('a',{'class':"css-o171kl"})  # bad filter
job_titles = soup.find_all('h2',{'class':"css-m604qf"})
#print(job_titles)
company_names = soup.find_all('a', class_="css-17s97q8")
#print(company_names)
location_names = soup.find_all('span', {'class':"css-5wys0k"})
#print(location_names)
job_skills = soup.find_all('div', class_="css-y4udm8")  # here we get them from upper div 
#print(job_skills)

# if you need to search for more than one attrubutes inside one tag ('a',{'class':"css-o171kl", 'class':"css-o171kl" , 'class':"css-o171kl" })

# 6th step loop over returned lists to extract needed info into other lists
#-- we need make empty lists to take our elemnts from for loop and put them on it
#-- len of any one pf them = other len

for i in range(len(job_titles)):                # BUG: differ between lists name and variable name!!!
    job_title.append(job_titles[i].text)
    company_name.append(company_names[i].text)
    location_name.append(location_names[i].text)
    job_skill.append(job_skills[i].text)

# print(job_title)
# print(company_name)
# print(location_name)
# print(job_skill)

# 7th step create csv file and fill it with values