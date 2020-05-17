# BBC News scraping using Scrapy and MongoDB
## Description : 
The goal of this coding challenge is to create a solution that crawls for articles from a news website (e.g. http://www.bbc.com), cleanses the response, stores it in a mongo database, then makes it available to search via an API. The main goals of this challenge are:
* Crawl articles on a news website such as using a crawler framework such as [Scrapy](http://scrapy.org) in Python.
* Cleanse the articles to obtain only information relevant to the news story, e.g. article text, headline, article url, etc.
* Store the data in a hosted Mongo database, e.g. [MongoDB Atlas](https://www.mongodb.com/cloud/atlas), for subsequent search and retrieval.
* Finally, writing an API that provides access to the content in the mongo database to search for articles by keyword.

## Specifications : 
### 1. Crawl the news articles :
A crawler is needed to start crawl the news articles from the news website, therefore we used is Scrapy framework that help us extracting the data from websites. To install it we use the following command : 
```
pip install scrapy
```

Then, to create a scrapy project and change the current working directory, we use:
```
scrapy startproject 'proj_name'
cd 'proj_name'
```

Finally, when we finish building the web spider in the directory of the project "proj_name/spiders", we can use the following instruction to start crawling the news articles :
```
scrapy crawl 'spider_name'
```
If you want to crawl bbc and save the data in a json file (e.g. called bbc.json), 
```
scrapy crawl 'spider_name' -o bbc.json
```
### 2. Cleanse the articles:
After scraping and extracting the data from [BBC](http://www.bbc.com) web site, we can find some superfluous content such as advertising and HTML in the news data. For this, we can use a framework such as [Readability](https://pypi.org/project/readability/) to cleanse the page  to get information related to the news stories only. We can use the command below to install the framework Readability :
```
pip install readability
```
~~The world is flat.~~



