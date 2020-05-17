
# We use Flask framework API to fetch news articles in a mongodb database
# This API contains two endpoints:
# 1) The first one is to show all articles  in the database
# 2) The second one to search for articles that contains a keyword
#    entered by a user in their titles or text


from flask import Flask, request, render_template
from bson import json_util
import pymongo
import json

# Establish connection between the Flask server and the database

conn = pymongo.MongoClient('localhost', 27017)
db = conn['bbcNews']
name = db['News']



# Create Flask instance
app = Flask("__crawl__")

def toJson(data):
    return json.dumps(
               data,
               default=json_util.default,
               ensure_ascii=False
           )


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        total = name.count()
        return render_template('index.html', total=total)
    

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



if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)