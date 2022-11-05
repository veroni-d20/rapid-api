# from turtle import st
from flask import Flask, render_template, request, redirect, url_for, session
from markupsafe import escape
import requests
import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/list')
def list():
    url = "https://newscatcher.p.rapidapi.com/v1/search_enterprise"

    querystring = {"q": "Elon Musk", "lang": "en",
                   "sort_by": "relevancy", "page": "1", "media": "True"}

    headers = {
        "X-RapidAPI-Key": "05db4efea2msha6e24b9b04d0fa1p1d2e10jsn70ec1b71e643",
        "X-RapidAPI-Host": "newscatcher.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    json_object = json.loads(response.text)
    # Open function to open the file "MyFile1.txt"
    # (same directory) in read mode and
    file1 = open("data.json", "w")

    file1.writelines(response.text)

    print(type(json_object))
    # students = []
    # sql = "SELECT * FROM Students"
    # stmt = ibm_db.exec_immediate(conn, sql)
    # dictionary = ibm_db.fetch_both(stmt)
    # while dictionary != False:
    #     # print ("The Name is : ",  dictionary)
    #     students.append(dictionary)
    #     dictionary = ibm_db.fetch_both(stmt)

    # if students:
    #     return render_template("list.html", students=students)
    return render_template("index.html", students=json_object)


@app.route('/delete/<name>')
def delete(name):
    sql = f"SELECT * FROM Students WHERE name='{escape(name)}'"
    print(sql)
    stmt = ibm_db.exec_immediate(conn, sql)
    student = ibm_db.fetch_row(stmt)
    print("The Name is : ",  student)
    if student:
        sql = f"DELETE FROM Students WHERE name='{escape(name)}'"
        print(sql)
        stmt = ibm_db.exec_immediate(conn, sql)

        students = []
        sql = "SELECT * FROM Students"
        stmt = ibm_db.exec_immediate(conn, sql)
        dictionary = ibm_db.fetch_both(stmt)
        while dictionary != False:
            students.append(dictionary)
            dictionary = ibm_db.fetch_both(stmt)
        if students:
            return render_template("list.html", students=students, msg="Delete successfully")

    # # while student != False:
    # #   print ("The Name is : ",  student)

    # print(student)
    return "success..."

# @app.route('/posts/edit/<int:id>', methods=['GET', 'POST'])
# def edit(id):

#     post = BlogPost.query.get_or_404(id)

#     if request.method == 'POST':
#         post.title = request.form['title']
#         post.author = request.form['author']
#         post.content = request.form['content']
#         db.session.commit()
#         return redirect('/posts')
#     else:
#         return render_template('edit.html', post=post)


@app.route('/view/<news_id>', methods=['GET'])
def view(news_id):
    f = open("data.json", "r")
    news_data = f.read()
    f = open("data.json", "r")
    news_data = f.read()
    json_object = json.loads(news_data)
    return render_template('view.html', data=json_object['articles'][0]['summary'])
