from flask import Flask, render_template


app=Flask(__name__)

## Route for a home page

@app.route('/')
def index():
    return render_template('home.html', title="home") 

@app.route('/predict',methods=['GET','POST'])
def predict_datapoint():

        return render_template('predict.html',results="Good")
    

if __name__=="__main__":
    app.run(debug=True)       

