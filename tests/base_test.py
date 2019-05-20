"""

BaseTest

This class should be the parent class of each non-unit test.
This instantiates database each time dynamically and makes sure
that each time, it's a new and blank database.

"""

from unittest import TestCase
from app import app
from db import db

class BaseTest(TestCase):

    @classmethod
    def setUpClass(cls):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        app.config['DEBUG'] = False
        with app.app_context():
            db.init_app(app)


    def setUp(self):
        # Making sure that the DB exists.
        with app.app_context():
            db.init_app(app)
            db.create_all()

        # Get a test client.
        self.app = app.test_client
        self.app_context = app.app_context


    def tearDown(self):
        # Clears the database
        with app.app_context():
            db.session.remove()
            db.drop_all()
