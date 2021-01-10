from mongoengine import *

connect('image_tag_data', alias = 'default', host="mongodb+srv://GFNK:GFNK@gufanaka.orv7h.mongodb.net/image_tag_data?retryWrites=true&w=majority")

class Image(Document):
    name = StringField(unique=True, required=True)
    image = ImageField(required=True)
 
    meta = {
        'id' : name
    }

    # example = Image(name = 'example')
    # with open('C:\coupang_crawler\image\\2020_12_30_1.jpg', 'rb') as img:
    #     example.image.replace(img, filename = 'example.jpg')
    #     example.save()

    

        
