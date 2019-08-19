# -*- coding: utf-8 -*-
from flask import Blueprint, abort, flash, g, jsonify, redirect, \
	render_template, request, url_for


contact = Blueprint('contact', __name__, url_prefix='/contact')

@contact.route('/')
def index():

	#posts = Blog.query.order_by(desc(Blog.id)).limit(3)


	return render_template('/contact.html', title='Enquire Now')