import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
books = {
        "chemicals":["Amazon","Microsoft","Google"],
        "symbols":["I","Am","cro","Na","le","abc"]
    }



@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype of REST API .</p>'''


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():



    results = {'"result"':""}

    for chemical in books["chemicals"]:
        for symbol in books["symbols"]:
            if(chemical.find(symbol)!=(-1)):
                x=chemical.index(symbol)
                y="["+symbol+"]"
                length=len(symbol)
                z=chemical[0:x]+y+chemical[x+length:len(chemical)]
                results['"result"']=results['"result"']+","+z

    
    results['"result"']=results['"result"'][1:len(results['"result"'])]
    #return results
    return jsonify(results)

    

app.run()
