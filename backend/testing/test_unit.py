from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase( TestCase ):
    def create_app(self):
        return app

class TestApp( TestBase ):

    def test_get_animal(self):

        response = self.client.get( url_for('get_animal') )
        self.assertEqual( response.status_code, 200 )
        self.assertIn( b'animal', response.data )
    
    def test_post_noise(self):

        response = self.client.post( url_for('post_noise'), json={"animal":"Sheep"})
        self.assertEqual( response.status_code, 200 )
        self.assertIn( b'Baabaa', response.data )        
