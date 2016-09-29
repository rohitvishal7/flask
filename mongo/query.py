from mongoengine import *
connect('test')


class add_blog(Document):
    name_of_blog = StringField(required=True)
    content = StringField(max_length=500)
    author = StringField(max_length=50)
    image =  StringField(max_length=100)


ross = add_blog(name_of_blog="a",
                    content="a",
                    author="a",
                    image="a"
                    ).save()

for user in add_blog.objects:
    print user.content