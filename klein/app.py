"""
Applications are great.  Lets have more of them.
"""
import sys

from functools import wraps

from werkzeug.routing import Map, Rule

from twisted.python import log
from twisted.web.server import Site
from twisted.internet import reactor

from klein.resource import KleinResource

from flask import Flask

__all__ = ['app', 'resource']


app = Flask("Klein-Flask hybrid")



def resource():
    return KleinResource(app)

