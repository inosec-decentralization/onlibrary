
from flask import Flask, render_template, redirect, url_for, request, jsonify
from foundation import search, get_db
import logging


try:
    file_log = open('cloud_chain/api_/web.log', 'r').close()
except:
    file_log = open('cloud_chain/api_/web.log', 'w').close()

logging.basicConfig(filename="cloud_chain/api_/web.log",
                    format='%(asctime)s %(message)s',
                    filemode='a+') #change the mode to a+ if file is present

logger = logging.getLogger()
logger.info("Started the web API")



app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
   return render_template("index.html")

@app.route('/search', methods=['GET', 'POST'])
def search():

   if request.method == "POST":
      keyword = request.form['content']
      return redirect(url_for('result', keyword=keyword, indx=0))
      
   else:
      # callecting the previous seach up to 100
      list_indexed = []
      indexed = get_db().out_db()

      if indexed is not None:
         for ind in range(0, 100):
            try:
               list_indexed.append(indexed[ind])
            except: break
      
      return render_template("search.html", index=list_indexed)

@app.route('/result/keyword=<keyword>,indx=<num>')
def result(keyword, num):
   keyword = str(keyword)

   if num == '0': #if searh is alreaady in database, indx==1, (0 for already searched & 1 for not searched)
      print(0)
      res = ['hello', 'bye']
      lin = ['/', '/']
      if res is not None:
            return render_template('result.html', link =lin, data=res)
            
      else: return jsonify({'response': 505})

   else: # if a new search
      print(1)
      load_data = get_db().in_db(keyword)

      if load_data is False: return jsonify({'response': 505})

      else:
         #lin = 
         #res = search(keyword).get_result() #return data in dictionary form
         if res is not None:
            return render_template('result.html', link =lin, data=res)
            
         else: return jsonify({'response': 505})



if __name__ == '__main__':
   app.run(host= '127.0.0.1', port=9248, debug=True)
'''
<!--
<ul>
    {% for item in data %}
        <li>{{item.name}}</li>
        <li>{{item.place}}</li>
        <li>{{item.mob}}</li>
    {% endfor %}
</ul>
-->
'''
