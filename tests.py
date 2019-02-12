import unittest
from flask_testing import TestCase
import os
from flask import abort, url_for

from app import create_app,db
from app.models import User,Book


class TestBase(TestCase):

    def create_app(self):

        setting_name = 'testing'
        app =create_app(setting_name)
        app.config.update(
            SQLALCHEMY_DATABASE_URI='postgresql://postgresdemo:12345@localhost/demodb_test'
        )
        return app
    
    def setUp(self):
        
        db.create_all()
        tester = User(username="tester",password="12345")

        db.session.add(tester)
        db.session.commit()

    
    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class TestModels(TestBase):
    
    def test_users_model(self):
        """
        Test number of records in User table
        """
        self.assertEqual(User.query.count(),1)


    def test_book_model(self):
        """
        Test number of records in book table
        
        """
        book = Book(name="book1",rating=1.0,user_id=1)
        db.session.add(book)
        db.session.commit()
        self.assertEqual(Book.query.count(),1)

class TestViews(TestBase):
        
    def test_homepage_view(self):

        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('home.homepage'))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        """
        Test that login page is accessible without login
        """
        response = self.client.get(url_for('auth.login'))
        self.assertEqual(response.status_code, 200)

class TestErrorPages(TestBase):
        
    def test_404_not_found(self):
        response = self.client.get('/papapa')
        self.assertEqual(response.status_code, 404)
        self.assertTrue("404 Error" in response.data)

    def test_500_internal_server_error(self):
            
        @self.app.route('/500')
        def internal_server_error():
            abort(500)

        response = self.client.get('/500')
        self.assertEqual(response.status_code, 500)
        self.assertTrue("500 Error" in response.data)

if __name__ == '__main__':
    unittest.main()