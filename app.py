from treats import app
import os
#from surf.database import db_session
from flask import Flask, session, g, render_template
from datetime import datetime

#from flask_security import Security, login_user, current_user
#from treats.database import User, Contact, Blog, db_session



from treats.views import main
app.register_blueprint(main.main)

from treats.views import contact
app.register_blueprint(contact.contact)

#@app.before_request
#def before_request():
    #g.user = current_user


