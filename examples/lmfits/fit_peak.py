#!/usr/bin/env python
# http://lmfit.github.io/lmfit-py/builtin_models.html#example-1-fit-peak-data-to-gaussian-lorentzian-and-voigt-profiles
import matplotlib.pyplot as plt
import numpy as np
import os

from lmfit.models import GaussianModel, LorentzianModel, VoigtModel

datapath = os.path.dirname(os.path.abspath(__file__))
data = np.loadtxt('%s/test_peak.dat' % datapath)
x = data[:, 0]
y = data[:, 1]

# Choose one
#----------------------------------------------------------------------|
# mod = GaussianModel()
# pars = mod.guess(y, x=x)
#----------------------------------------------------------------------|
# mod = LorentzianModel()
# pars = mod.guess(y, x=x)
#----------------------------------------------------------------------|
mod = VoigtModel()
pars = mod.guess(y, x=x)
pars['gamma'].set(value=0.7, vary=True, expr='')
#----------------------------------------------------------------------|

out = mod.fit(y, pars, x=x)
print(out.fit_report(min_correl=0.25))

plt.plot(x, y, 'b')
# plt.plot(x, out.init_fit, 'k--')
plt.plot(x, out.best_fit, 'r-')
plt.show()
