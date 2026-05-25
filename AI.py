#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      GP80
#
# Created:     26/10/2025
# Copyright:   (c) GP80 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pandas as pd
import numpy as np

df = pd.read_csv("ai_eu_geocoded_mean.csv")

import pandas as pd

# Assuming your DataFrame is named df

# Indicator columns (excluding 'Scale' and 'Intensity')
indicator_cols = [
    'Overall', 'Talent', 'Infrastructure', 'Operating Environment',
    'Research', 'Development', 'Government Strategy', 'Commercial'
]

# Compute mean of each indicator
eu_means = df[indicator_cols].mean()

# Convert to DataFrame for easy plotting/export
eu_means_df = eu_means.reset_index()
eu_means_df.columns = ['Indicator', 'Mean']

print(eu_means_df)

