from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from monarch.app import create_app
from monarch.corelibs.store import db
from monarch.models.admin_user import AdminUser

application = create_app('monarch')
application.config['DEBUG'] = True

manager = Manager(application)
migrate = Migrate(application, db)
manager.add_command('db', MigrateCommand)

@manager.command
def init_admin_user():
    AdminUser.create(
        account="admin",
        password="admin123",
        is_admin=True
    )

if __name__ == '__main__':
    manager.run()
