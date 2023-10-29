import pandas as pd
import seaborn as sns
import numpy as np
from scipy.stats import norm
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from scipy.ndimage import gaussian_filter1d
from scipy.signal import savgol_filter

plt.rcParams["figure.figsize"] = [7.00, 5.00]
plt.rcParams["figure.autolayout"] = True

sums = pd.read_csv("dist_sum_random_walk.csv", header=None)
sums=sums.iloc[:,0]
sums_min=min(sums)
sums_max=max(sums)
mean=np.mean(sums)
std=np.std(sums)

x=np.linspace(sums_min,sums_max,100)
y=norm.pdf(x,mean,std)

window_size = 2  # Specify the window size
polynomial_degree = 1  # Specify the degree of the polynomial
smooth_data = savgol_filter(sums, window_size, polynomial_degree)

fig = plt.figure()

plt.plot(x,y,'--r',label='Gaussian Fit')
sns.histplot(smooth_data, stat = 'density', ec=None, binwidth = 1, label = 'Binwidth=1')
plt.xlabel('Sum')
plt.ylabel('Probability Density')
plt.title('Distribution of the Sum of 10^4 Random Walks of 10^4 steps each')
plt.legend()

sums = pd.read_csv("dist_sum_random_walk_2.csv", header=None)
sums=sums.iloc[:,0]
sums_min=min(sums)
sums_max=max(sums)
mean=np.mean(sums)
std=np.std(sums)

x=np.linspace(sums_min,sums_max,100)
y=norm.pdf(x,mean,std)

window_size = 2  # Specify the window size
polynomial_degree = 1  # Specify the degree of the polynomial
smooth_data = savgol_filter(sums, window_size, polynomial_degree)

fig = plt.figure()

plt.plot(x,y,'--r',label='Gaussian Fit')
sns.histplot(smooth_data, stat = 'density', ec=None, binwidth = 1, label = 'Binwidth=1')
plt.xlabel('Sum')
plt.ylabel('Probability Density')
plt.title('Distribution of the Sum of 10^5 Random Walks of 10^4 steps each')
plt.legend()

sums = pd.read_csv("dist_sum_random_walk_3.csv", header=None)
sums=sums.iloc[:,0]
sums_min=min(sums)
sums_max=max(sums)
mean=np.mean(sums)
std=np.std(sums)

x=np.linspace(sums_min,sums_max,100)
y=norm.pdf(x,mean,std)

window_size = 2  # Specify the window size
polynomial_degree = 1  # Specify the degree of the polynomial
smooth_data = savgol_filter(sums, window_size, polynomial_degree)

fig = plt.figure()

plt.plot(x,y,'--r',label='Gaussian Fit')
sns.histplot(smooth_data, stat = 'density', ec=None, binwidth = 1, label = 'Binwidth=1')
plt.xlabel('Sum')
plt.ylabel('Probability Density')
plt.title('Distribution of the Sum of 10^5 Random Walks of 10^5 steps each')
plt.legend()

def save_image(filename):
	
	# PdfPages is a wrapper around pdf
	# file so there is no clash and
	# create files with no error.
	p = PdfPages(filename)
	
	# get_fignums Return list of existing
	# figure numbers
	fig_nums = plt.get_fignums()
	figs = [plt.figure(n) for n in fig_nums]
	
	# iterating over the numbers in list
	for fig in figs:
		
		# and saving the files
		fig.savefig(p, format='pdf')
		
	# close the object
	p.close()
	
#name your pdf file
filename = "dist_sum_random_walk_fixed.pdf"
#call the function
save_image(filename)
