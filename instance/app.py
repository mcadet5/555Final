


from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///payments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)

def create_tables():
    with app.app_context():
        db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_record = Record(
            company=request.form['company'],
            amount=request.form['amount'],
            payment_date=datetime.strptime(request.form['payment_date'], '%Y-%m-%d'),
            status=request.form['status'],
            due_date=datetime.strptime(request.form['due_date'], '%Y-%m-%d')
        )
        db.session.add(new_record)
        db.session.commit()
        return redirect(url_for('index'))

    records = Record.query.all()
    return render_template('index.html', records=records)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    record = Record.query.get_or_404(id)
    db.session.delete(record)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
