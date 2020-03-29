from data import db_session
from data.users import User
from data.jobs import Jobs
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    global session
    jobs = session.query(Jobs).all()
    dop = []
    for job in jobs:
        dop.append(dict())
        dop[-1]["name"] = job.job
        team_leader = session.query(User).filter(User.id == job.team_leader).first()
        dop[-1]["leader"] = team_leader.name + " " + team_leader.surname
        dop[-1]["size"] = job.work_size
        dop[-1]["collabs"] = job.collaborators
        dop[-1]["is_finished"] = job.is_finished
    return render_template("index.html", data=dop)


def main():
    global session
    db_session.global_init("db/mars_explorer.db")
    session = db_session.create_session()
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()