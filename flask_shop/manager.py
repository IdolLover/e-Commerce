from flask_shop import create_app,db
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager

app = create_app('develop')

manage=Manager(app)
Migrate(app,db)
manage.add_command('db',MigrateCommand)

if __name__ == '__main__':
    app.run()
    # manage.run()