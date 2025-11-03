### Put and Delete-HTTP Verbs
### Working with API's--Json


from flask import Flask, jsonify, request

app = Flask(__name__)

## Initial Data in my to-do-List
items = [
    {"id":1, "name":"Item 1", "description":"This is Item1"},
    {"id":2, "name":"Item 2", "description":"This is Item2"}
]

@app.route('/')
def home():
    return "welocome to the Sample To Do List App"

## Get: Retriving all the items

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

## Get: Retrive Item by Id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item=next((item for item in items if item["id"]==item_id), None)
    if item is None:
        return jsonify({"error": "item not found"})
    return jsonify(item)




if __name__=='__main__':
    app.run(debug=True)
