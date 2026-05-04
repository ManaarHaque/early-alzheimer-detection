import nibabel as nib
import numpy as np
import cv2
import os

input_dir = "outputs/Preprocessed/Final_Data"
output_dir = "outputs/2D_Slices"

def process_and_save():
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if not file.endswith('.nii.gz'): continue

            img = nib.load(os.path.join(root, file)).get_fdata()
            total_slices = img.shape[2]
            start = int(total_slices * 0.2)
            end = int(total_slices * 0.8)

            for i in range(start, end):
                slice_data = img[:, :, i]

                # Rescale to 224x224 and normalize to 0-255
                slice_rescaled = cv2.resize(slice_data, (224, 224))
                slice_norm = cv2.normalize(slice_rescaled, None, 0, 255, cv2.NORM_MINMAX)
                diag = os.path.basename(root) # AD, MCI, or CN
                save_path = os.path.join(output_dir, diag)
                os.makedirs(save_path, exist_ok=True)
                cv2.imwrite(f"{save_path}/{file}_slice{i}.png", slice_norm)

process_and_save()