### Building Url Dynamically
### Variable Rule
### Jinja 2 Template Engine


### Jinja 2 Template Engine
'''
{{  }} expressions to print Output in HTML
{%..%} conditions, for loops 
{#...#} this is for comments
'''


from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


@app.route("/")
def welcome():
    return "<html><h1>Welcome to the Flask course </h1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')


# Varaible Rule
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    
    return render_template('result.html', results=res)


# Varaible Rule
@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"

    exp={'Score ':score, 'res ':res}
    
    return render_template('result1.html', results=exp)



# Varaible Rule
@app.route('/successif/<int:score>')
def successif(score):
   
    
    return render_template('result.html', results=score)


@app.route('/fail/<int:score>')
def fail(score):
    
    
    return render_template('result.html', results=score)
    

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['Maths'])
        c = float(request.form['c'])
        data_science = float(request.form['Datascience'])

        total_score = (science + maths + c + data_science) / 4
        return redirect(url_for('successres', score=total_score))
    
    return render_template('getresult.html')




if __name__ == "__main__":
    app.run(debug=True)
