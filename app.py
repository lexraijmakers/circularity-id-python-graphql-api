#!/usr/bin/env python

from database import init_db
from flask import Flask
from schema import schema
from flask_cors import CORS
from flask_graphql import GraphQLView

app = Flask(__name__)
CORS(app)
app.debug = True

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    init_db()

    app.run(threaded=True, debug=True)
