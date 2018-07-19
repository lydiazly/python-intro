#!/usr/bin/env python
# -*- coding: utf-8 -*-
import h5py
import pandas as pd
import numpy as np
import os

datapath = os.path.dirname(os.path.abspath(__file__)) + '/../data'

arr = np.random.rand(1000, 1000)
arr2 = np.random.randint(9, size=(500, 2000))

print("array: %.1f M" % ((arr.nbytes + arr2.nbytes) / 1024.**2))

np.save(f'{datapath}/test_np', arr)
np.savez_compressed(f'{datapath}/test_np', arr)

with h5py.File(f'{datapath}/test_h5py_0.hdf5', 'w') as f:
    f.create_dataset('data', data=arr)
    f.create_dataset('data2', data=arr2)
complevel = 9
for i in {'gzip', 'lzf'}:
    if i == 'lzf': complevel = None
    with h5py.File(f'{datapath}/test_h5py_{i}.hdf5', 'w') as f:
        f.create_dataset('data', data=arr, compression=i, compression_opts=complevel)
        f.create_dataset('data2', data=arr2, compression=i, compression_opts=complevel)

arr = pd.DataFrame(arr)
arr2 = pd.DataFrame(arr2)
with pd.HDFStore(f'{datapath}/test_pd_0.hdf5', 'w') as f:
    f['data'] = arr
    f['data2'] = arr2
for i in {'zlib', 'lzo', 'bzip2', 'blosc'}:
    with pd.HDFStore(f'{datapath}/test_pd_{i}.hdf5', 'w', complevel=9, complib=i) as f:
        f['data'] = arr
        f['data2'] = arr2

