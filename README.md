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
This spider can mainly scrape the articles  contents from the home page of bbc. The extracted data is in this form:
```
{
"title": "The robot assistant that can guess what you want",
"description": "Thomas Roszak was working as a maintenance technician at Ocado's giant warehouse in Hatfield when he received a very unusual assignment.",
"url": "https://www.bbc.com/news/business-52547331",
"Type": "Business",
"time": "12 May 2020",
"related_topics": "Robotics"
}
```
### 2. Cleanse the articles:
After scraping and extracting the data from [BBC](http://www.bbc.com) web site, we can find some superfluous content such as advertising and HTML in the news data. For this, we can use a framework such as [Readability](https://pypi.org/project/readability/) to cleanse the page  to get information related to the news stories only. We can use the command below to install the framework Readability :
```
pip install readability
```
> __PS:__ I didn't need the Readability framework in my project,  I just extract the necessary data.

## 3. Store the crawled data :
Each time an item is returned, we must validate the data and then add it to a Mongo collection. To do this, the initial step is to create the database that we plan to use to save all of our crawled data. Open settings.py and specify the pipeline and add the database settings:
```
MONGO_URI='localhost'
MONGODB_PORT = 27017
MONGO_DB='bbcNews'#db name
MONGODB_COLLECTION = "News"

ITEM_PIPELINES = {
    'bbc.pipelines.BbcPipeline': 300
}
```
I did use the __MongoDB Compass__ GUI tool, for visualizing our crawled data.

## 4. Create Flask API :
The fourth objectif of our challenge is to creat an API that provides access to the content in the mongo database, and the user should be able to search for articles by keyword. Therefore, I build an API using Flask framework by employing Flask-PyMongo to establish connection between the Flask server and the MongoDB.

```
pip install flask
```
We use Flask framework API to fetch news articles in a mongodb database. This API contains two endpoints:
 * The first one is to show all articles in the database.
 * The second one to search for articles that contains a keywordentered by a user in their titles or text.

```
# show all news articles
@app.route('/DB', methods=['GET'])
def all_news():
    if request.method == 'GET':
        jsons = request.args.get('json', 'off')
        DB_list = []
        article = name.find()
        for i in article:
            DB_list.append(i)
        
        if jsons == 'off':
            return render_template('database.html', entries=DB_list)
        else:
            return toJson(DB_list)
```
```
# Search for specific news using a keyword
# and returning all selected articles's data
        
@app.route('/search', methods=['GET'])
@app.route('/search/<item>', methods=['GET'])
def get_searched(item=None):
    if request.method == 'GET':
        page = request.args.get('page', 1, type=int)
        limit = request.args.get('limit', 60, type=int)
        p = (page - 1) * limit
        offset = request.args.get('offset', p, type=int)
        catid = request.args.get('catid', None, type=str)
        jsons = request.args.get('json', 'off')
        keyword = request.args.get('key', '')
        
        if not keyword:
            keyword = item

        if catid:
            cursor = name.find({'title.catid': catid})
        else:
            cursor = name.find({'description': {'$regex': keyword} })

        
        results = cursor.skip(offset).limit(limit)
        resultList = []
        for result in results:
            resultList.append(result)

        if jsons == 'off':
            return render_template('search.html', entries=resultList)
        else:
            return toJson(resultList)
```
After creating the needed endpoints that the user will claim it, this is the main page :
![Main page](bbc/img/main_page.png)

> To test your created API you can use __POSTMAN__  or any browser you prefer.
