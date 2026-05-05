# Deep Learning for Automated Detection of
Alzheimer's Disease from Brain MRI
Scans

This project aims to automate the classificationof MRI scans into 3 categories:

* **CN**: Cognitively Normal
* **MCI**: Mild Cognitive Impairememt
* **AD**: Alzheimer's Disease

We utilize the ADNI dataset and an approach involving a baselines model and transfer learning with EfficientNetB0

## 📊 Data Source
The data used in this project is obtained from the **Alzheimer's Disease Neuroimaging Initiative (ADNI)**.

* **Official Website:** [adni.loni.usc.edu](https://adni.loni.usc.edu/)
* **Data Access:** Access to ADNI data requires an official application and adherence to the [ADNI Data Use Agreement](https://adni.loni.usc.edu/data-samples/access-data/).

## Data Acquisition and Standardisation 

* **Format Conversion**: Raw DICOM files were converted to NifTI (.nii.gz) to allow 3D volumetric manipulation.

* **Numerical Decoding**: ADNI clinical metadata was mapped to patient IDs to assign ground truth labels (1=CN, 2=MCI, 3=AD).

##Preprocessing the Data

* **Orientation**: All scans were organized to a canonical orientation.

* **Slice Extraction**: To remove non informative parts (top and bottom of the skull), 2D axial slices were extracted from the central 60% of each 3D volume.

* **Normalization**: Slices were resized to 224x224 pixels and normalized to zero mean and unit variance to match ImageNet standards.

## Data Integrity and Leakage Prevention

* **Patient Level Splitting**: To prevent data leakage, all splits were performed at the Patient ID level.

* Created a master_manifest.csv linking every 2D slice to a unique Patient ID, ensuring a tight separation of data.

* **Stratified Split Result**:
  * Total Patients: 161
  * Hold Out Test Set: 25 patients
  * K-Fold Training/Val Set: 136 patients (used 5 folds cross validation.













