from flask import Flask
from kbd import create_app
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from kbd import db

#RUN DB ALEMBIC COMMANDS FROM THE CL

manager=Manager(create_app)
manager.add_command('db',MigrateCommand)

if __name__=='__main__':
    manager.run()
