import requests
from bs4 import BeautifulSoup
def beautify(links, titles):
    if len(links)==0:
        print("No recipes found!")
        return None
    print('='*130)
    header= f'{" "*30}{"Title":5s}{" "*30}{" "*30}{"Link":5s}{" "*30}'
    print(header)
    print('='*130)
    
    for i in range(0,len(links),1):
        content= f'{titles[i].text.strip():65s}{links[i]:65s}'
        print(content)
        print('-'*130)
def getRecipes(ingredients):
    url1= f'https://tasty.co/search?q={"+".join(ingredients)}&sort=popular'
    url2= f'https://www.delish.com/search/?q={"+".join(ingredients)}&type=Recipes'
    #print(url1)
    print("Calculating...")
    response = requests.get(url1).content
    soup= BeautifulSoup(response, 'lxml')
    link= soup.find_all('a')
    list_href=[]
    recipes=[]
    for l in link:
        href= l.get('href')
        if href.startswith('/recipe'):
            list_href.append("https://tasty.co"+href)
    recipes.extend(soup.find_all('div', class_='feed-item__title'))
    #print(recipes)
    #print(list_href)
    response = requests.get(url2).content
    #print(response)
    soup= BeautifulSoup(response, 'lxml')
    link= soup.find_all('a')
    #print(link)
    #list_href=[]
    #print(len('/cooking/recipe-ideas'))
    for l in link:
        href= l.get('href')
        if href.startswith('/cooking/recipe-ideas') and len(href)>22:
            list_href.append("https://www.delish.com"+href)
    recipes.extend(soup.find_all('span', class_='css-76imi8 e10ip9lg5'))
    #print(recipes)
    #print(list_href)
    beautify(list_href, recipes)

print("="*50)
print(" "*20,"WELCOME!")
print("="*50)
while True:
    ingredients= input("Enter ingredients seperated by space: ").split()
    getRecipes(ingredients)
    #print(ingredients[0])
    print("="*130)
    print()
    inp=input("Do you want to continue?(Y/N) ")
    if inp in "Nn":
        print("Thank You!")
        break