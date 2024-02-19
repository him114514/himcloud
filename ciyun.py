from matplotlib import pyplot 
from wordcloud import WordCloud
import numpy as np
from PIL import Image
class cloud:
    def __init__(self,text,img):
        self.image = Image.open(img)
        self.mask = np.array(self.image)[:, :, 0] > 128
        self.wordcloud = WordCloud(font_path='msyhbd.ttc', background_color="white", width=800, height=400,mask=self.mask)
        self.w=text
     
    def show(self):
        self.wordcloud.generate(self.w)
        pyplot.imshow(self.wordcloud, interpolation='bilinear')
        pyplot.axis("off")
        pyplot.show()


cloud=cloud("ssslsjls","zhushen.ico")
cloud.show()

        

