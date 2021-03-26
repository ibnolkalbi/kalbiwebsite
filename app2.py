from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from dateutil import relativedelta 
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return render_template("mywebpage.html")


# @app.route('/resume')
# def resume():
#     return render_template("resume.html")

@app.route('/cspa')
def login():
    return render_template("aboutcspa.html")


@app.route('/', methods=['POST', 'GET'])
def age():
    years = ''
    months = ''
    days = ''
    if request.method == 'POST':
            # ...approved...date...
            y = int(request.form.get('y'))
            m = int(request.form.get('m'))
            d = int(request.form.get('d'))
            
            # ....priority...date...
            year = int(request.form.get('year'))
            month = int(request.form.get('month'))
            day = int(request.form.get('day'))

            cpy = int(request.form.get('cpy'))
            cpm = int(request.form.get('cpm'))
            cpd = int(request.form.get('cpd'))

            dy = int(request.form.get('dy'))
            dm = int(request.form.get('dm'))
            dd = int(request.form.get('dd'))

            # ....approved-priority.....
            a = datetime(y,m,d)
            b = datetime(year,month,day)
            delta = relativedelta.relativedelta (a,b)
            years = delta.years
            months = delta.months
            days =  delta.days

            # ....current-priority----DOB.....
            a1 = datetime(cpy,cpm,cpd)
            b1 = datetime(dy,dm,dd)
            delta1 = relativedelta.relativedelta (a1,b1)
            years1 = delta1.years
            months1 = delta1.months
            days1 =  delta1.days

            # ....Age_upto_cp---(approved-priority).....
            a2 = datetime(years1,months1,days1)
            b2 = datetime(years,months,days)
            delta2 = relativedelta.relativedelta (a2,b2)
            years = delta2.years
            months = delta2.months
            days =  delta2.days

            
    return render_template("cspa.html", years=years, months=months, days=days )


    #....for demo......
    # su = ''
    # if request.method == 'POST':
    #     n = request.form.get('n')
    #     m = request.form.get('m')
    #     su= int(n) + int(m)
    # return render_template("cspa.html", su = su)
    #....end demo.....




if __name__==("__main__"):
    app.run(debug=True)