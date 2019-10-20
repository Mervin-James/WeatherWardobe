import io
import os
from google.cloud import vision
from google.cloud.vision import types  

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="mapper.json"
client = vision.ImageAnnotatorClient()

file_name = os.path.join(os.path.dirname(__file__),'image3.jpg')

with io.open(file_name,'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)
objects = client.object_localization(image=image).localized_object_annotations
#print('Number of objects found: {}'.format(len(objects)))

for object_ in objects:
    print('\n{} '.format(object_.name))

'''
    print('Normalized bounding polygon vertices: ')
    for vertex in object_.bounding_poly.normalized_vertices:
        print(' - ({}, {})'.format(vertex.x, vertex.y))
'''
'''
image = types.Image(content=content)

response = client.label_detection(image=image)
#response2 = client.image_properties(image=image)
labels = response.label_annotations

for label in labels:
    print(label.description)
'''
