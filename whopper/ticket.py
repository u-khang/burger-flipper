from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from whopper.db import get_db

bp = Blueprint('auth', __name__)
