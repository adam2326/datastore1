# python modeules
from flask import Flask, request, flash
import jinja2
import os

# google modules
from google.appengine.ext import ndb



app = Flask(__name__)


###############################################################################################################
#
# DATASTORE - Kind classes
#
###############################################################################################################

# define an employee class
class Employee(ndb.Model):
	# Cloud Datastore assign a numeric ID automatically, omit the key_name argument:
	fname = ndb.StringProperty()
	lname = ndb.StringProperty()
	employee_creation_date = ndb.DateTimeProperty(auto_now_add=True)

# define an opportunity class
class Opportunity(ndb.Model):
	entity_creation_date = ndb.DateTimeProperty(auto_now_add=True)
	opp_start_date = ndb.DateTimeProperty()
	unit_name = ndb.StringProperty()
	num_units = ndb.IntegerProperty()
	existing_customer = ndb.BooleanProperty()
	notes = ndb.TextProperty()


###############################################################################################################
#
# DATASTORE - Entity creation
#
###############################################################################################################


def create_employee_key(starter_name='default_employee'):
    return ndb.Key('EmployeeBook', starter_name)

# create an employee
def create_employee(fname, lname):
	employee = Employee(parent=create_employee_key())
	# Cloud Datastore assign a numeric ID automatically since the keyword is omitted, omit the key_name argument:
	employee.fname = fname
	employee.lame = lname
	employee.put()


# create an opportunity
def create_opportunity(entity_creation_date, opp_start_date, unit_name, num_units, existing_customer, notes):
	opportunity = Opportunity()
	# Cloud Datastore assign a numeric ID automatically since the keyword is omitted, omit the key_name argument:
	opportunity.entity_creation_date = entity_creation_date
	opportunity.opp_start_date = opp_start_date
	opportunity.unit_name = unit_name
	opportunity.num_units = num_units
	opportunity.existing_customer = existing_customer
	opportunity.notes = notes
	opportunity.put()










###############################################################################################################
#
# FRONTENT CODE
#
###############################################################################################################

@app.route('/')
def render_data(fname=None, lname=None):
	# get argument 'name' or use default name set above
	fname = request.args.get('fname',fname)
	lname = request.args.get('lname',lname)
	if fname != None and lname != None:
		create_employee(fname=fname, lname=lname)
		outcome='success'
	else:
		#flash('Error in your names')
		outcome = 'error'
	return "<html><body>submission status: {}</body></html>".format(outcome)