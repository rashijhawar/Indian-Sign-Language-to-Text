import os
import cv2
from image_processing import image_processing

if not os.path.isdir('image_data_processed'):
    os.mkdir('image_data_processed')


for folder in os.listdir('image_data'):
    source_folder = os.path.join('image_data', folder)
    dest_folder = os.path.join('image_data_processed', folder)
    if not os.path.isdir(dest_folder):
        os.mkdir(dest_folder)

    for filename in os.listdir(source_folder):
        source_file_path = os.path.join(source_folder, filename)
        dest_file_path = os.path.join(dest_folder, filename)
        cv2.imwrite(dest_file_path, image_processing(cv2.imread(source_file_path)))
        

