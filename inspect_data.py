import mne
from mne.datasets import eegbci
from mne.io import concatenate_raws, read_raw_edf

subject = 1
runs = [4, 8, 12]
raw_fnames = eegbci.load_data(subject, runs, path='./data')
raw = concatenate_raws([read_raw_edf(f, preload=True) for f in raw_fnames])

eegbci.standardize(raw)  # fix channel naming to standard 10-20
raw.set_montage('standard_1005')

print("Channels:", raw.ch_names)
print("Sample rate:", raw.info['sfreq'], "Hz")
print("Duration:", raw.n_times / raw.info['sfreq'], "seconds")

events, event_id = mne.events_from_annotations(raw)
print("Event types found:", event_id)
print("Number of events:", len(events))
