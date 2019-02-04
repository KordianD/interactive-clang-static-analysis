from mongoengine import Document, StringField, IntField, DateTimeField


class ClangWarning(Document):
    check_name = StringField(required=True)
    path_to_file = StringField(required=True)
    line_number = IntField(required=True)
    owner = StringField(required=True)
    date = DateTimeField(required=True)
