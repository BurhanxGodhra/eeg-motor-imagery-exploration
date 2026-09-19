import mne
from mne.datasets import eegbci

# Subject 1, runs 3&7&11 = left/right hand motor imagery task
subject = 1
runs = [4, 8, 12]  # motor imagery: left fist vs right fist

raw_fnames = eegbci.load_data(subject, runs, path='./data')
print("Downloaded files:")
for f in raw_fnames:
    print(f)
