from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/season", methods=['get'])
def season_input():
  return render_template('start.html')

@app.route("/season", methods=['post'])
def season_print():
  month = request.form.get('month', type=int)
  season = '겨울'
  style = 'gray'
  if 3<=month<=5:
    season = '봄'
    style = 'green'
  elif 6<=month<=8:
    season = '여름'
    style = 'blue'
  elif 9<=month<=11:
    season = '가을'
    style = 'purple'
  return render_template("/end.html", month=month, season=season, style=style)

app.run()