from settings import app, db
from models import Project


with app.app_context():
    db.init_app(app)
    db.create_all()

@app.route("/api/projects", methods=["POST"])
def add_project():
    project = Project(id="1", name="teste")
    db.session.add(project)
    db.session.commit()
    return {'foo': 'bar'}

@app.route("/api/projects/<string:project_name>", methods=["GET"])
def show_project_detail(project_name):
    result = Project.query.filter_by(name='teste').first()
    print(result)
    return {'foo': 'bar'}

@app.route("/api/projects/<string:project_name>", methods=["DELETE"])
def delete_project(project_name):
    result = Project.query.filter_by(name='teste').first()
    db.session.delete(result)
    db.session.commit()
    return {'foo': 'bar'}
