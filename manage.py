from app import create_app, db
from flask_script import Manager, Server
from app.models import User, Role, Review
from flask_migrate import Migrate, MigrateCommand

app = create_app("production")
manager = Manager(app)
server = Server(host="0.0.0.0", port=5000)
manager.add_command("runserver", server)

migrate = Migrate(app,db)
manager.add_command("db",MigrateCommand)

@manager.command
def test():
    """
    Run the unittests
    """
    import unittest
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app,
                db = db,
                User = User, 
                Role = Role,
                Review = Review)

if __name__ == '__main__':
    manager.run()