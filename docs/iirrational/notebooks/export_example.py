# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Export Testcase Example
# Here an existing randomly generated testcase is exported

# %%
from wield.iirrational.utilities.mpl import *

# %%
dat = iirrational_data('simple2', instance_num = 2)
axB = plot_fitter_flag(dat.fitter)

# %%
wield.iirrational.v1.data2testcase(
    fname = 'simple2.mat', 
    data = dat.data,
    F_Hz = dat.F_Hz,
    SNR = dat.SNR,
    bestfit_ZPK_z = dat.bestfit_ZPK_z,
    F_nyquist_Hz = dat.F_nyquist_Hz,
    description = 'test',
)

# %%
import scipy.io
d = scipy.io.loadmat('simple2.mat')

# %%
d['bestfit_ZPK_z']

# %%
