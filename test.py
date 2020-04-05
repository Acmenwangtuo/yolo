import yolo
import os
from PIL import Image
import glob
from yolo import YOLO
def detect(yolo):
    path = '/home/bnc/tool/HistomicsML/yourproject/level3/*.tif'
    outpath = './result/'
    print("hahahahah")
    la = []
    la = glob.glob(path)
    print(la)
    for tif in glob.glob(path):
        print("shabi")
        img = Image.open(tif)
        img = yolo.detect_image(img)
        print("======>{} has been processed".format(img))
        img.save(os.path.join(outpath,os.path.basename(tif)))
    yolo.close_session()
def main():
    a = YOLO()
    detect(a)
if __name__ == "__main__":
    main()
