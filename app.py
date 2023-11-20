from datetime import datetime
from flask import Flask, render_template , request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/login'
db = SQLAlchemy(app)

class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    query= db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    number = db.Column(db.String(20), nullable=False)

    

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')    

@app.route("/course")
def course():
    return render_template('course.html')



@app.route("/connect")
def connect():
    return render_template('connect.html')


@app.route("/contact", methods= ('GET', 'POST'))
def contact():
    if(request.method=='POST'):
        '''add entry to database'''
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        query=request.form.get('query')

        entry =Contact(name=name, email=email,date=datetime.now(), query=query,  number=phone)
        db.session.add(entry)
        db.session.commit()
        
    return render_template('contact.html') 

@app.route("/dsa.html")
def dsa():
    return render_template('dsa.html')   

@app.route("/reg.html")
def reg():
    return render_template('reg.html')              

@app.route("/dsahome")
def innerpage():
    return render_template('dsahome.html')

@app.route("/e-books")
def book():
    return render_template('book.html')    

@app.route("/linear_search")
def linear_search():
    return render_template('linear_search.html')    





import pandas as pd
from flask import Flask, render_template, request, jsonify

# Load course data from pickled file
try:
    courses_list = pd.read_pickle('course.pkl')
except FileNotFoundError:
    print("Error: Could not find 'course.pkl' file.")
    courses_list = pd.DataFrame()  # Empty DataFrame as a fallback

# Assuming you have a similarity matrix (replace this with your actual similarity matrix)
# Example: similarity = your_function_to_compute_similarity(courses_list)
# Make sure to replace 'your_function_to_compute_similarity' with the actual function you use.
similarity = pd.read_pickle('similarity.pkl')

# Your recommendation function
def recommend(course):
    index = courses_list[courses_list['course_name'] == course].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_course_names = [courses_list.iloc[i[0]].course_name for i in distances[1:7]]
    return recommended_course_names

@app.route('/recommend')
def rec():
    # Check if courses_list is a DataFrame
    if not courses_list.empty:
        courses = courses_list['course_name'].tolist()
    else:
        courses = []  # Empty list as a fallback

    return render_template('index.html', courses=courses)

@app.route('/api/recommendations', methods=['POST'])
def get_recommendations():
    data = request.get_json()
    selected_course = data.get('selectedCourse', '')
    
    if not selected_course:
        return jsonify({'error': 'Invalid request'}), 400

    recommendations = recommend(selected_course)
    return jsonify({'recommendations': recommendations})





if __name__=="__main__":
    app.run(debug=True,port=5001)    