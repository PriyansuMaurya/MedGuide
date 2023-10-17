from flask import Flask, render_template


app=Flask(__name__)

## Route for a home page

@app.route('/')
def index():
    return render_template('tell_symptoms.html', title="Symptoms") 

@app.route("/possible-disease", methods=['GET', 'POST'])
def possibledisease_datappoint():
      
        return render_template('possible_disease.html', results="Good")

@app.route("/suggestions", methods=['GET', 'POST'])
def suggestions_datappoint():
      
        return render_template('suggestions.html', results="Good")

@app.route("/faqs", methods=['GET', 'POST'])
def faqs_datappoint(): 
       
        return render_template('faqs.html', results="Good")

if __name__=="__main__":
    app.run(debug=True)       

