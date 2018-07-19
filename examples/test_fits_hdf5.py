#!/usr/bin/env python
# -*- coding: utf-8 -*-
import h5py
import pandas as pd
import numpy as np
import os, sys
from astropy.io import fits
import sunpy.map

fname = sys.argv[1]
datapath = os.path.dirname(fname)
smap = sunpy.map.Map(fname)

if 'BSCALE' in smap.meta:
    arr = (smap.data / smap.meta['BSCALE']).astype('int%d' % smap.meta['BITPIX'])
else:
    arr = smap.data

print("array: %.1f M" % (arr.nbytes / 1024.**2))

np.save(f'{datapath}/fits_np', arr)
np.savez_compressed(f'{datapath}/fits_np', arr)

header = fits.Header()
hdu = fits.PrimaryHDU(arr, header)
hdu.writeto(f'{datapath}/fits_prim.fits', overwrite=True)
# i.e.
# import sunpy.io.fits
# sunpy.io.fits.write(f'{datapath}/fits_prim.fits', arr, header, overwrite=True)

hdu = fits.CompImageHDU(arr, header)
hdu.writeto(f'{datapath}/fits_compimg.fits', overwrite=True)

with h5py.File(f'{datapath}/fits_h5py_0.hdf5', 'w') as f:
    f.create_dataset('data', data=arr)
complevel = 9
for i in {'gzip', 'lzf'}:
    if i == 'lzf': complevel = None
    with h5py.File(f'{datapath}/fits_h5py_{i}.hdf5', 'w') as f:
        f.create_dataset('data', data=arr, compression=i, compression_opts=complevel)

arr = pd.DataFrame(arr)
with pd.HDFStore(f'{datapath}/fits_pd_0.hdf5', 'w') as f:
    f['data'] = arr
for i in {'zlib', 'lzo', 'bzip2', 'blosc'}:
    with pd.HDFStore(f'{datapath}/fits_pd_{i}.hdf5', 'w', complevel=9, complib=i) as f:
        f['data'] = arr

