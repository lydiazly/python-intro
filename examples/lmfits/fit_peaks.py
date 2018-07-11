#!/usr/bin/env python
# http://lmfit.github.io/lmfit-py/builtin_models.html#example-1-fit-peak-data-to-gaussian-lorentzian-and-voigt-profiles
# <examples/doc_nistgauss2.py>
import matplotlib.pyplot as plt
import numpy as np
import os

from lmfit.models import ExponentialModel, GaussianModel

datapath = os.path.dirname(os.path.abspath(__file__))
dat = np.loadtxt('%s/NIST_Gauss2.dat' % datapath)
x = dat[:, 1]
y = dat[:, 0]

exp_mod = ExponentialModel(prefix='exp_')
gauss1 = GaussianModel(prefix='g1_')
gauss2 = GaussianModel(prefix='g2_')


def index_of(arrval, value):
    """return index of array *at or below* value """
    if value < min(arrval):
        return 0
    return max(np.where(arrval <= value)[0])

ix1 = index_of(x, 75)
ix2 = index_of(x, 135)
ix3 = index_of(x, 175)

pars1 = exp_mod.guess(y[:ix1], x=x[:ix1])
pars2 = gauss1.guess(y[ix1:ix2], x=x[ix1:ix2])
pars3 = gauss2.guess(y[ix2:ix3], x=x[ix2:ix3])

pars = pars1 + pars2 + pars3
mod = gauss1 + gauss2 + exp_mod

out = mod.fit(y, pars, x=x)

print(out.fit_report(min_correl=0.5))

plt.plot(x, y, 'b')
plt.plot(x, out.init_fit, 'k--')
plt.plot(x, out.best_fit, 'r-')

# plt.savefig('models_nistgauss2.png')
plt.show()