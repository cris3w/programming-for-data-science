import pandas as pd
import matplotlib.pyplot as plt
import matplotlib


# Look pretty...
matplotlib.style.use('ggplot')


# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..
seeds_dataset = pd.read_csv('Datasets/wheat.data')
print seeds_dataset.head(5), '\n'


# TODO: Create a 2d scatter plot that graphs the
# area and perimeter features
# 
# .. your code here ..
seeds_dataset.plot.scatter(x='area', y='perimeter', marker='^')


# TODO: Create a 2d scatter plot that graphs the
# groove and asymmetry features
# 
# .. your code here ..
seeds_dataset.plot.scatter(x='groove', y='asymmetry', marker='.')


# TODO: Create a 2d scatter plot that graphs the
# compactness and width features
# 
# .. your code here ..
seeds_dataset.plot.scatter(x='compactness', y='width', marker='o')


# BONUS TODO:
# After completing the above, go ahead and run your program
# Check out the results, and see what happens when you add
# in the optional display parameter marker with values of
# either '^', '.', or 'o'.


plt.show()
