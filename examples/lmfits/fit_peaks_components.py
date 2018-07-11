#!/usr/bin/env python
# http://lmfit.github.io/lmfit-py/builtin_models.html#example-1-fit-peak-data-to-gaussian-lorentzian-and-voigt-profiles
# <examples/doc_builtinmodels_nistgauss.py>
import matplotlib.pyplot as plt
import numpy as np
import os

from lmfit.models import ExponentialModel, GaussianModel

datapath = os.path.dirname(os.path.abspath(__file__))
dat = np.loadtxt('%s/NIST_Gauss2.dat' % datapath)
x = dat[:, 1]
y = dat[:, 0]

exp_mod = ExponentialModel(prefix='exp_')
pars = exp_mod.guess(y, x=x)

gauss1 = GaussianModel(prefix='g1_')
pars.update(gauss1.make_params())

pars['g1_center'].set(105, min=75, max=125)
pars['g1_sigma'].set(15, min=3)
pars['g1_amplitude'].set(2000, min=10)

gauss2 = GaussianModel(prefix='g2_')

pars.update(gauss2.make_params())

pars['g2_center'].set(155, min=125, max=175)
pars['g2_sigma'].set(15, min=3)
pars['g2_amplitude'].set(2000, min=10)

mod = gauss1 + gauss2 + exp_mod

init = mod.eval(pars, x=x)

out = mod.fit(y, pars, x=x)
print(out.fit_report(min_correl=0.5))

plot_components = True

plt.plot(x, y, 'b')
plt.plot(x, init, 'k--')
plt.plot(x, out.best_fit, 'r-')

if plot_components:
    comps = out.eval_components(x=x)
    plt.plot(x, comps['g1_'], 'b--')
    plt.plot(x, comps['g2_'], 'b--')
    plt.plot(x, comps['exp_'], 'k--')

plt.show()