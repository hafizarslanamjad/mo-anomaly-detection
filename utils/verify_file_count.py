import os
import pandas as pd


image_dir = '/home/hafiz/my_thesis/seg_recons/dataset/black_pak_screws/test/struct_images'
mask_dir = '/home/hafiz/my_thesis/seg_recons/dataset/black_pak_screws/test/struct_masks'
annotations_file = '/home/hafiz/my_thesis/seg_recons/dataset/black_pak_screws/test/test_annotations.csv'

#image_dir = '/dataset/black_pak_screws/train/struct_images'
#mask_dir = '/dataset/black_pak_screws/train/struct_masks'
#annotations_file = '/dataset/black_pak_screws/train/train_annotations.csv'

# Check if all images have corresponding masks
image_files = set(os.listdir(image_dir))
mask_files = set(os.listdir(mask_dir))
missing_masks = image_files - mask_files
if missing_masks:
    print(f"Missing masks for: {missing_masks}")

# Check if all images have entries in annotations.csv
annotations = pd.read_csv(annotations_file)
annotation_images = set(annotations['image_file'].apply(lambda x: f"{x}.png"))
missing_annotations = image_files - annotation_images
if missing_annotations:
    print(f"Missing annotations for: {missing_annotations}")

#/home/hafiz/my_thesis/seg_recons/dataset/black_pak_screws/train/struct_images