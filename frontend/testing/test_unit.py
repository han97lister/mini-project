from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from frontend.app import app

class TestBase( TestCase ):
    def create_app(self):
        return app

class TestResponse( TestBase ):

    #test for get and post request
    def test_animal_shows(self):
        with patch( "requests.get" ) as g:
            with patch( "requests.post" ) as p:
                g.return_value.json.return_value = {"animal":"Cow"}
                p.return_value.json.return_value = {"noise":"Moooo"}

                response = self.client.get( url_for("index") )
                self.assertIn(b'Cow', response.data)
                self.assertIn(b'Moooo', response.data)

