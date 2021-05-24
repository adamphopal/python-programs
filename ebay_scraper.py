import requests
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def get_page(url):
    response = requests.get(url)

    if not response.ok:
        print('Server responded:', response.status_code)
    else:
        soup = BeautifulSoup(response.text, 'lxml')
    return soup


def get_detail_data(soup):
    try:
        title = soup.find('h1', id='itemTitle').text.strip()[16:]
    except:
        title = ''
    #print(title)

    try:
        try:
            p = soup.find('span', id='prcIsum').text.strip()
        except:
            p = soup.find('span', id='mm-saleDscPrc').text.strip()
        currency, price = p.split(' ')
    except:
        currency = ''
        price = ''

    try:
        sold = soup.find('span', class_='vi-qtyS-hot-red').find('a').text.strip().split(' ')[0]
    except:
        sold = ''
    #print(sold)

    data = {
        'title': title,
        'price': price,
        'currency': currency,
        'total sold': sold
    }

    return data


def get_index_data(soup):
    try:
        links = soup.find_all('a', class_='s-item__link')
    except:
        links = []

    urls = [item.get('href') for item in links]

    return urls


def write_csv(data, url):
    with open('ebay.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)

        row = [data['title'], data['price'], data['currency'], data['total sold'], url + "\t"]

        writer.writerow(row)


def main():
    driver =  webdriver.Chrome(ChromeDriverManager().install())
    csv_file = open('ebay.csv', 'w')
    writer = csv.writer(csv_file)
    writer.writerow(['title', 'price', 'currency', 'total sold', 'link'])
    csv_file.close()
    MAX_PAGE_NUM = 2
    MAX_PAGE_DIG = 1

    for i in range(1, MAX_PAGE_NUM + 1):
        page_num = (MAX_PAGE_DIG - len(str(i))) * "0" + str(i)
 #       url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=python+books&_sacat=0&LH_TitleDesc=0&_ipg=100&_pgn=' + page_num
        url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=mens+watches&rt=nc&rt=nc&rt=nc&_ipg=100&_pgn=' + page_num  

        driver.get(url)
 
 #   url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=mens+watches&_pgn=1' 
    products = get_index_data(get_page(url))

    for link in products:
        data = get_detail_data(get_page(link))
        write_csv(data, link)


if __name__ == '__main__':
    main()
