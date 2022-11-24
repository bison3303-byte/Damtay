from flask import Flask, Response, request, render_template, redirect
from . import app
from .views import *


if __name__ == "__main__":
    Flask(debug=True)