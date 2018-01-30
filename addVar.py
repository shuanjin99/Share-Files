from wtforms import Form, StringField, SubmitField, SelectField, TextAreaField, RadioField, IntegerField, validators

class Add(Form):
    header = StringField('Header: ')
    content = TextAreaField('Content: ')
    add = SubmitField('Add')