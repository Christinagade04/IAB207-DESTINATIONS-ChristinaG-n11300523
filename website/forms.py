from flask_wtf import FlaskForm
from wtforms import DateField, DateTimeField, IntegerField, PasswordField, SelectField, TimeField
from wtforms.fields import TextAreaField,SubmitField, StringField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed

ALLOWED_FILE = {'PNG','JPG','png','jpg'}

class EventForm(FlaskForm):
  name = StringField('Event Name', validators=[InputRequired()])
  # adding two validators, one to ensure input is entered and other to check if the 
  # description meets the length requirements
  description = TextAreaField('Description', validators =[InputRequired(), 
        Length(min=100,max=500, message="Description must be between 100 and 500 characters.")])
  image = FileField('Event Image', validators=[
    FileRequired(message='Image cannot be empty'),
    FileAllowed(ALLOWED_FILE, message='Only PNG or JPG files allowed')])  
  date = DateField('Event Date', format='%Y-%m-%d', validators=[InputRequired()])
  start_time = TimeField('Start Time', format='%H:%M', validators=[InputRequired()])
  end_time = TimeField('End Time', format='%H:%M', validators=[InputRequired()])
  location = StringField('Location', validators=[InputRequired()])
  category = SelectField('Event Category', choices=[
        ('Sm Dogs', 'Small Dogs'),
        ('Md Dogs', 'Medium Dogs'),
        ('Lg Dogs', 'Large Dogs'),
        ('workshop', 'Workshop'),
        ('training', 'Training'),
        ('social', 'Social'),
        ('special needs', 'Special Needs')],
        validators=[InputRequired()])
  tickets = IntegerField('Tickets Available', validators=[InputRequired()]) 
  submit = SubmitField("Create")
    
# User comment
class CommentForm(FlaskForm):
  text = TextAreaField('Comment', [InputRequired()])
  submit = SubmitField('Create')

class OrderForm(FlaskForm):
  number_of_tickets = IntegerField('Number of Tickets', validators=[InputRequired()])
  submit = SubmitField('Book Now')


# User login
class LoginForm(FlaskForm):
    user_name = StringField("User Name", validators=[InputRequired('Enter user name')])
    password = PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

# User register
class RegisterForm(FlaskForm):
    user_name = StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    
    # linking two fields - password should be equal to data entered in confirm
    password = PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")
    # submit button
    submit = SubmitField("Register") 