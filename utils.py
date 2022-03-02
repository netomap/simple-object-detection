import pandas as pd
import random
from PIL import Image, ImageDraw
from tqdm import tqdm

def refatorar_anotacoes(df_: pd.DataFrame, img_size):
    bboxes = []
    for path, x0, y0, x1, y1 in tqdm(df_.values):
        w, h = Image.open(path).size
        x0, y0, x1, y1 = x0*(img_size/w), y0*(img_size/h), x1*(img_size/w), y1*(img_size/h)
        bboxes.append([path, x0, y0, x1, y1])
    
    new_df = pd.DataFrame(bboxes, columns=['path', 'x0', 'y0', 'x1', 'y1'])
    return new_df