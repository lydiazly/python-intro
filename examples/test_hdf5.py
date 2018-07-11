#!/usr/bin/env python
# -*- coding: utf-8 -*-
import h5py
import pandas as pd
import numpy as np

arr = np.arange(1000000.).reshape(1000, -1)
arr2 = np.arange(1000000).reshape(1000, -1)

with h5py.File('data/test_h5py_0.hdf5', 'w') as f:
    f.create_dataset('data', data=arr)
    f.create_dataset('data2', data=arr2)
comp = 9
for i in {'gzip', 'lzf'}:
    if i == 'lzf': comp = None
    with h5py.File(f'data/test_h5py_{i}.hdf5', 'w') as f:
        f.create_dataset('data', data=arr, compression=i, compression_opts=comp)
        f.create_dataset('data2', data=arr2, compression=i, compression_opts=comp)

arr = pd.DataFrame(arr)
arr2 = pd.DataFrame(arr2)
with pd.HDFStore('data/test_pd_0.hdf5', 'w') as f:
    f['data'] = arr
    f['data2'] = arr2
for i in {'zlib', 'lzo', 'bzip2', 'blosc'}:
    with pd.HDFStore(f'data/test_pd_{i}.hdf5', 'w', complevel=9, complib=i) as f:
        f['data'] = arr
        f['data2'] = arr2

