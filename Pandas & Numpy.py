# Python code demonstrate creating
# DataFrame from dict narray / lists
# By default addresses.

import pandas as pd
import numpy as np 

# initialize data of lists.
data = {'Name': ['Tom', 'nick', 'krish', 'jack'],
        'Age': [20, 21, 19, 18]}
# Create DataFrame
df = pd.DataFrame(data)
# Print the output.
print(df)
df.shape
df.shape[0]-1
np.isnan('Age')

