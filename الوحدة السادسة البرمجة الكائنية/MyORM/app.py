from Database import Database
from Model import Model
from Field import *
from http.server import SimpleHTTPRequestHandler, HTTPServer

Model.db = Database('database.sqlite')
Model.connection = Model.db.connect()

class Post(Model):
    title = 'TEXT'
    body = 'TEXT'
    created_at = 'TIMESTAMP'
    published = 'BOOLEAN'

class User(Model):
    first_name = CharField()
    last_name = CharField(max_length=255)
    age = IntegerField()


if __name__ == '__main__':
    post = Post()