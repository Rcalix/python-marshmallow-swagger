"""
Flask environment manager.

Authors: Handerson Contreras
"""
from flask import Flask
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy


from app import APP, DB

MANAGER = Manager(APP)
MIGRATE = Migrate(APP, DB)

MANAGER.add_command("runserver", Server(host='localhost', port=8080))
MANAGER.add_command('migrate', MigrateCommand)
MANAGER.add_command('db', MigrateCommand)

MANAGER.add_option('-c', '--config', dest='config', required=True)

if __name__ == '__main__':
    MANAGER.run()
