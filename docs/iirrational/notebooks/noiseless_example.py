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
# Noiseless Data Fitting
# =============
#
# The default heuristics for noisy models must be modified for noiseless data. Those heuristics primarly check for relative changes to the average residuals. For noiseless data the residuals can be at numeric precision and so the checks should be done using exact thresholds rather than relative thresholds.
#
# Also for exact fits the nyquist frequency must be chosen well. Exact models from the s domain will have slightly modified phase response when run at a finite nyquist frequency. The fits will choose higher order to fit out this modified phase. If the nyquist is sufficiently high and some fit error is allowed, then the order will be reduced.
#
#  - *The order reduction for this is not working well (it worked better in the past). Needs some attention.*

# %% nbsphinx="hidden"
from wield.iirrational.utilities.mpl import *

# %%
#tdat =  iirrational_data('rand2_log100E', set_num = 1)
tdat =  iirrational_data('simple0E', set_num = 3)
out = v1.data2filter(
    tdat,
    SNR = 1,
    F_nyquist_Hz = 16384, 
)
ax = plot_fitter_flag_compare(out.fitter, tdat.fitter)

# %%
out = v1.data2filter(
    tdat,
    SNR = 1,
    F_nyquist_Hz = 16384, 
    hints = [
        v1.hintsets.exact_data,
    ],
)
ax = plot_fitter_flag_compare(out.fitter, tdat.fitter)

# %% [markdown]
#  - Inspect the hintsets to get an idea how to run for different applications. The "hints" argument to data2filter can take a list of sets which it will overlay.

# %%
v1.hintsets.exact_data

# %%
out = v1.data2filter(
    tdat,
    SNR = 1,
    F_nyquist_Hz = 16384, 
    hints = [
        {'resavg_EthreshOrdDn': 1,
         'resavg_RthreshOrdC': None,
         'resavg_RthreshOrdDn': None,
         'resavg_RthreshOrdUp': None},
        v1.hintsets.quiet,
    ]
)
ax = plot_fitter_flag_compare(out.fitter, tdat.fitter)

# %%
