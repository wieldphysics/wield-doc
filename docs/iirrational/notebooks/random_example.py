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

# %%
from wield.iirrational.utilities.mpl import *

# %% [markdown]
# # Random Filter fit with comparison

# %% [markdown]
# ## Show stage-1 Rational Disc Fit
# Here is the preliminary fit on a reduced-nyquist disc
#
# The poles and zeros are shown on the full disc. Note that unstable poles are allowed _on the real line_ as these are removed by analytic surgery during the nyquist shift 

# %%
dat = iirrational_data('rand10_lin1k', set_num = 5)
out = v1.rational_disc_fit(
    dat,
)
ax = plot_fitter_flag(out)

# %% [markdown]
# ## With nyquist shift
#
# The data detunes from being a great fit

# %%
dat = iirrational_data('rand10_lin1k', set_num = 5)
out = v1.rational_disc_fit(
    dat,
    nyquist_final_Hz = 16384,
)
ax = plot_fitter_flag(out)

# %%
# %%time

out = v1.data2filter(
    dat,
    delay_s = None,
)

# %%
ax = plot_fitter_flag_compare(out.fitter, dat.fitter)

# %%
out.digest_write(
    folder = 'random',
    clear_plots = True,
    ipy_display = True,
    MP_workers = 1,
)

# %%
