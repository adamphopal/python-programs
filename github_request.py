from requests_html import HTML, HTMLSession
import csv

#In this Python project, we will be learning how to scrape websites, more specifically the latest python github projects using the Requests-HTML library.
#Requests-HTML is an excellent tool for parsing HTML code and grabbing exactly the information you need.

#Scrapes the Trending page for python project only, updated recently
#See what the GitHub community is most excited about today, by scraping the latest python project names,description, and link
#scrapes updated/newest trending python repos on github
#saves the newest github python project name, description, and code link into a csv file nicly organized
#prints the saved data into terminal
csv_file = open('python_github.csv', 'w')#writes the data into 'python_github.csv', you can name it whatever u want
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name', 'Description', 'Link'])#The heading that will be displayed

#first create the html session with the site
session = HTMLSession()
r = session.get('https://github.com/trending/python?since=daily')

articles = r.html.find('article')
#print(article.html)

for article in articles:#for loop, to loop over every article on the page, aka looping over all the repos
    headline = article.find('.text-normal', first=True).text #find the class .text-normal
    headline_u = headline.split("/")[0]#removes the / after the name of the repo, more organized
    print("Python Github repo name: ", headline_u)

    description = article.find('p', first=True).text#find paragraph tag
    print("Description: ", description)

    try: 
        link = article.find('a', first=True).attrs['href']#try the a tag, and get href attribute, which has a link
        #print(link)
        link_id = link.split('%2F')[1:3]#remove %2F from link, and keep only the second and last
        #print(link_id)
        final_link = "/" #starts off with just this
        final_link = final_link.join(link_id)#then we join the link_id, from the previous step, which has 2 words in a list, and joins it together between the "/"
        #print(final_link) 
        gh_link = f'https://github.com/{final_link}' #the href final_link, will now fianlly be added to the github base link, to create proper urls
    except Exception as e:
        gh_link = None

    print("Github repo link: ", gh_link)
    print()
    #adding the scraped data from the for loop into the csv file
    csv_writer.writerow([headline_u, description, gh_link])

csv_file.close()#close it

#to read the data from the csv file into terminal, use pandas, type the following into python shell
#the same directory as the csv file, and type python3 to start the terminal sesh
#>>> import pandas
#>>> df = pandas.read_csv('python_github.csv')
#>>> print(df)

#should scrape 25 rows of data from (headline_u, description, gh_link),
#into the 3 columns we specified(Name, Description, Link)

#prints all relative links on page
#for link in r.html.links:
#    print(link)

#prints all absoulte links(full url)
#for link in r.html.absolute_links:
#    print(link)
    



