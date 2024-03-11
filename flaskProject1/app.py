import re

from flask import Flask, request, render_template, session, redirect;
from utils import query
from utils.getHomeData import *
from utils.getSearchData import *
# from utils.getTime_tDate import *
app = Flask(__name__)
app.secret_key = 'this is session_key know ?'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        request.form = dict(request.form)

        def filter_fn(item):
            return request.form['email'] in item and request.form['password'] in item

        users = query.querys('select * from user', [], 'select')
        filter_user = list(filter(filter_fn, users))
        if len(filter_user):
            session['email'] = request.form['email']
            return redirect('/home')
        else:
            return render_template('login.html')


@app.route('/loginOut')
def loginOut():
    session.clear();
    return redirect('/login')


@app.route('/search/<int:movieId>', methods=['GET', 'POST'])
def search(movieId):
    email =session.get('email')
    if request.method == 'GET':
        resultData = getMovieDetailByid(movieId)
    else:
        request.form=dict(request.form)
        resultData =getMovieDetailBySearchWord(request.form['searchWord'])

    return render_template('search.html',resultData=resultData,email=email)

# @app.route('/time_t')
# def time_t():
#     row,columns=getYearDate()
#     email =session.get('email')
#     movieTimeDatta=getMovieTimeData()
#     return render_template('time_t.html',email=email,row=row,columns=columns,movieTimeDatta=movieTimeDatta)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        request.form = dict(request.form)
        if request.form['password'] != request.form['passwordChecked']:
            return render_template('error.html')

        def filter_fn(item):
            return request.form['email'] in item

        users = query.querys('select * from user', [], 'select')
        filter_list = list(filter(filter_fn, users))
        if len(filter_list):
            return render_template('error.html', message='该用户已被注册')
        else:
            query.querys('insert into user(email,password) values(%s,%s)',
                         [request.form['email'], request.form['password']])
            return redirect('/login')


@app.route('/home', methods=['GET', 'POST'])
def home():
    email = session.get('email')
    maxlang, maxCountry, maxRate, maxCasts, maxMovieLen, maxType = getHomeData()
    typeEchartData = getTypeEchartDate()
    row, columns = getRateEcharData()
    tableData = getTableData()
    return render_template('index.html', email=email, maxlang=maxlang,
                           maxCountry=maxCountry,
                           maxRate=maxRate,
                           maxCasts=maxCasts,
                           maxMovieLen=maxMovieLen,
                           maxType=maxType,
                           typeEchartData=typeEchartData,
                           row=row,
                           columns=columns,
                           tableData=tableData)


@app.before_request
def before_requre():
    pat = re.compile(r'^/static')
    if re.search(pat, request.path):
        return
    if request.path == '/login':
        return
    if request.path == '/register':
        return
    email = session.get('email')
    if email:
        return None
    return redirect('/login')


@app.route('/', methods=['GET', 'POST'])
def allRequest():
    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port='5000')
