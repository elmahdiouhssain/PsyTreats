# -*- coding: utf-8 -*-
from flask import Blueprint, abort, flash, g, jsonify, redirect, \
	render_template, request, url_for


main = Blueprint('main', __name__, url_prefix='/')

@main.route('/')
def index():

	#posts = Blog.query.order_by(desc(Blog.id)).limit(3)


	return render_template('/index.html', title='Home')


@main.route('/invitation')
def invitation():

	#posts = Blog.query.order_by(desc(Blog.id)).limit(3)


	return render_template('/invitation.html', title='Our Invitation')


@main.route('/food')
def food():

	#posts = Blog.query.order_by(desc(Blog.id)).limit(3)


	return render_template('/food.html', title='Food Page')

@main.route('/about_us')
def about():

	#posts = Blog.query.order_by(desc(Blog.id)).limit(3)


	return render_template('/about.html', title='Alex Wedlock')

@main.route('/yoga')
def yoga():

	#posts = Blog.query.order_by(desc(Blog.id)).limit(3)


	return render_template('/yoga.html', title='Food Page')

@main.route('/location')
def location():

	#posts = Blog.query.order_by(desc(Blog.id)).limit(3)


	return render_template('/location.html', title='Our Location')

@main.route('/what_you_can_expect')
def exp():

	#posts = Blog.query.order_by(desc(Blog.id)).limit(3)


	return render_template('/expect.html', title='What You Can Expect')

@main.route('/programme')
def programme():

	#posts = Blog.query.order_by(desc(Blog.id)).limit(3)


	return render_template('/programme.html', title='Our Programme')