from flask_wtf import Form
from wtforms import StringField, IntegerField, SubmitField, Label, BooleanField
from wtforms import validators


class UsersForm(Form):

    nickname = StringField("Nickname: ", [validators.data_required("Please, enter user nickname.")])
    login = StringField("Login: ", [validators.Optional()])
    password = StringField("Password: ", [validators.Optional()])

    submit = SubmitField("Enter")


class SitesForm(Form):

    site_adress = StringField("Site adress: ", [validators.URL("Please, enter site adress.")])
    site_name = StringField("Site name: ", [validators.Optional()])

    submit = SubmitField("Enter")


class StylesForm(Form):

    style_name = StringField("Site name: ", [validators.URL("Please, enter site adress.")])
    code = StringField("Code: ", [validators.Optional()])
    premium = BooleanField("Premium: ", [validators.Optional()])

    submit = SubmitField("Enter")