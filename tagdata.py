from mongoengine import *

connect('image_tag_data', 'default', host="mongodb+srv://GFNK:GFNK@gufanaka.orv7h.mongodb.net/image_tag_data?retryWrites=true&w=majority")

class Tagdata(Document):
    name = StringField(unique=True,required=True)
    title = StringField(required=True)  
    date = DateTimeField(required=True)
    google_tag = ListField(null=True)
    kakao_tag = ListField(null=True)
    title_tag = ListField()
    file_dir = StringField()

    meta = {
        'id' : name,
        'order' : date
    }

 
        

 
    