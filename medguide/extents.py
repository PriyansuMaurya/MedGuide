from flask import Blueprint,render_template, request

extents = Blueprint('extents',__name__)



@extents.route("/suggestions", methods=['GET', 'POST'])
def suggestions():
      
        return render_template('suggestions.html', title="Suggestions")

@extents.route("/faqs", methods=['GET', 'POST'])
def faqs(): 
       
        return render_template('faqs.html', title="Faqs")



