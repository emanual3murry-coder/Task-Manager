from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'

db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description or '',
            'completed': self.completed,
            'created_at': self.created_at.strftime('%b %d, %Y')
        }


with app.app_context():
    db.create_all()


@app.route('/')
def index():
    filter_by = request.args.get('filter', 'all')
    if filter_by == 'active':
        tasks = Task.query.filter_by(completed=False).order_by(Task.created_at.desc()).all()
    elif filter_by == 'completed':
        tasks = Task.query.filter_by(completed=True).order_by(Task.created_at.desc()).all()
    else:
        tasks = Task.query.order_by(Task.created_at.desc()).all()

    total = Task.query.count()
    active = Task.query.filter_by(completed=False).count()
    done = Task.query.filter_by(completed=True).count()

    return render_template('index.html',
                           tasks=tasks,
                           filter_by=filter_by,
                           total=total,
                           active=active,
                           done=done)


@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title', '').strip()
    description = request.form.get('description', '').strip()

    if not title:
        return redirect(url_for('index'))

    task = Task(title=title, description=description if description else None)
    db.session.add(task)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/toggle/<int:task_id>', methods=['POST'])
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = not task.completed
    db.session.commit()
    return jsonify({'success': True, 'completed': task.completed})


@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'success': True})


@app.route('/clear-completed', methods=['POST'])
def clear_completed():
    Task.query.filter_by(completed=True).delete()
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
