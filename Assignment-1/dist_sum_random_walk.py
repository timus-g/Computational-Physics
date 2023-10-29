import pandas as pd
import seaborn as sns
import numpy as np
from scipy.stats import norm
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


plt.rcParams["figure.figsize"] = [7.00, 5.00]
plt.rcParams["figure.autolayout"] = True

# First -------------------------------------------------------------------------------------------------------------------

sums = pd.read_csv("dist_sum_random_walk.csv", header=None)
sums=sums.iloc[:,0]
sums_min=min(sums)
sums_max=max(sums)
mean=np.mean(sums)
std=np.std(sums)

print (sums_min)
print (sums_max)
print (mean)
print (std)

x=np.linspace(sums_min,sums_max,100)
y=norm.pdf(x,mean,std)

fig = plt.figure()
plt.plot(x,y,'--r',label='Gaussian Fit')
sns.histplot(sums, stat = 'density', ec=None, binwidth = 1, label = 'Binwidth=1')
plt.xlabel('Sum')
plt.ylabel('Probability Density')
plt.title('Distribution of the Sum of 10^4 Random Walks of 10^4 steps each')
plt.legend()

fig = plt.figure()
plt.plot(x,y,'--r',label='Gaussian Fit')
sns.histplot(sums, stat = 'density', ec=None, binwidth = 2, label = 'Binwidth=2')
plt.xlabel('Sum')
plt.ylabel('Probability Density')
plt.title('Distribution of the Sum of 10^4 Random Walks of 10^4 steps each')
plt.legend()

fig = plt.figure()
sns.histplot(sums, stat = 'density', ec=None, binwidth = 5, label='Binwidth=5')
plt.plot(x,y,'--r',label='Gaussian Fit')
plt.xlabel('Sum')
plt.ylabel('Probability Density')
plt.title('Distribution of the Sum of 10^4 Random Walks of 10^4 steps each')
plt.legend()

fig = plt.figure()
sns.histplot(sums, stat = 'density', ec=None, binwidth = 10, label='Binwidth=10')
plt.plot(x,y,'--r',label='Gaussian Fit')
plt.xlabel('Sum')
plt.ylabel('Probability Density')
plt.title('Distribution of the Sum of 10^4 Random Walks of 10^4 steps each')
plt.legend()

fig = plt.figure()
plt.plot(x,y,'--r',label='Gaussian Fit')
sns.histplot(sums, stat = 'density', ec=None, binwidth = 2, binrange = (-407,409), label='Bins[...-1,1,..]')
plt.xlabel('Sum')
plt.ylabel('Probability Density')
plt.title('Distribution of the Sum of 10^4 Random Walks of 10^4 steps each')
plt.legend()

fig = plt.figure()
plt.plot(x,y,'--r',label='Gaussian Fit')
sns.histplot(sums, stat = 'density', ec=None, binwidth = 2, binrange = (-408,408), label='Bins[...-2,0,2,..]')
plt.xlabel('Sum')
plt.ylabel('Probability Density')
plt.title('Distribution of the Sum of 10^4 Random Walks of 10^4 steps each')
plt.legend()

# Second ------------------------------------------------------------------------------------------------------------------

sums = pd.read_csv("dist_sum_random_walk_2.csv")
sums=sums.iloc[:,0]

mean=np.mean(sums)
std=np.std(sums)
sums_min=min(sums)
sums_max=max(sums)

print (sums_min)
print (sums_max)
print (mean)
print (std)

x=np.linspace(sums_min,sums_max,100)
y=norm.pdf(x,mean,std)

fig = plt.figure()
plt.plot(x,y,'--r',label='Gaussian Fit')
sns.histplot(sums, stat = 'density', ec=None, color='orange', binwidth = 1, label='Binwidth=1')
plt.xlabel('Sum')
plt.ylabel('Probability Density')
plt.title('Distribution of the Sum of 10^5 Random Walks of 10^4 steps each')
plt.legend()

fig = plt.figure()
plt.plot(x,y,'--r',label='Gaussian Fit')
sns.histplot(sums, stat = 'density', ec=None, color='orange', binwidth = 2, label='Binwidth=2')
plt.xlabel('Sum')
plt.ylabel('Probability Density')
plt.title('Distribution of the Sum of 10^5 Random Walks of 10^4 steps each')
plt.legend()

fig = plt.figure()
plt.plot(x,y,'--r',label='Gaussian Fit')
sns.histplot(sums, stat = 'density', ec=None, color='orange', binwidth = 5, label='Binwidth=5')
plt.xlabel('Sum')
plt.ylabel('Probability Density')
plt.title('Distribution of the Sum of 10^5 Random Walks of 10^4 steps each')
plt.legend()

fig = plt.figure()
plt.plot(x,y,'--r',label='Gaussian Fit')
sns.histplot(sums, stat = 'density', ec=None, color='orange', binwidth = 10, label='Binwidth=10')
plt.xlabel('Sum')
plt.ylabel('Probability Density')
plt.title('Distribution of the Sum of 10^5 Random Walks of 10^4 steps each')
plt.legend()

fig = plt.figure()
plt.plot(x,y,'--r',label='Gaussian Fit')
sns.histplot(sums, stat = 'density', ec=None, color='orange', binwidth = 2, binrange = (-407,409), label='Bins[...-1,1,..]')
plt.xlabel('Sum')
plt.ylabel('Probability Density')
plt.title('Distribution of the Sum of 10^5 Random Walks of 10^4 steps each')
plt.legend()

fig= plt.figure()
plt.plot(x,y,'--r',label='Gaussian Fit')
sns.histplot(sums, stat = 'density', ec=None, color='orange', binwidth = 2, binrange = (-408,408), label='Bins[...-2,0,2,..]')
plt.xlabel('Sum')
plt.ylabel('Probability Density')
plt.title('Distribution of the Sum of 10^5 Random Walks of 10^4 steps each')
plt.legend()

# Third -------------------------------------------------------------------------------------------------------------------

sums = pd.read_csv("dist_sum_random_walk_3.csv")
sums=sums.iloc[:,0]

mean=np.mean(sums)
std=np.std(sums)
sums_min=min(sums)
sums_max=max(sums)

print (sums_min)
print (sums_max)
print (mean)
print (std)

x=np.linspace(sums_min,sums_max,100)
y=norm.pdf(x,mean,std)

fig = plt.figure()
plt.plot(x,y,'--r',label='Gaussian Fit')
sns.histplot(sums, stat = 'density', ec=None, color='green', binwidth = 1, label='Binwidth=1')
plt.xlabel('Sum')
plt.ylabel('Probability Density')
plt.title('Distribution of the Sum of 10^5 Random Walks of 10^5 steps each')
plt.legend()

fig = plt.figure()
plt.plot(x,y,'--r',label='Gaussian Fit')
sns.histplot(sums, stat = 'density', ec=None, color='green', binwidth = 2, label='Binwidth=2')
plt.xlabel('Sum')
plt.ylabel('Probability Density')
plt.title('Distribution of the Sum of 10^5 Random Walks of 10^5 steps each')
plt.legend()

fig = plt.figure()
plt.plot(x,y,'--r',label='Gaussian Fit')
sns.histplot(sums, stat = 'density', ec=None, color='green', binwidth = 5, label='Binwidth=5')
plt.xlabel('Sum')
plt.ylabel('Probability Density')
plt.title('Distribution of the Sum of 10^5 Random Walks of 10^5 steps each')
plt.legend()

fig = plt.figure()
plt.plot(x,y,'--r',label='Gaussian Fit')
sns.histplot(sums, stat = 'density', ec=None, color='green', binwidth = 10, label='Binwidth=10')
plt.xlabel('Sum')
plt.ylabel('Probability Density')
plt.title('Distribution of the Sum of 10^5 Random Walks of 10^5 steps each')
plt.legend()

fig = plt.figure()
plt.plot(x,y,'--r',label='Gaussian Fit')
sns.histplot(sums, stat = 'density', ec=None, color='green', binwidth = 2, binrange = (-1001,1003), label='Bins[...-1,1,..]')
plt.xlabel('Sum')
plt.ylabel('Probability Density')
plt.title('Distribution of the Sum of 10^5 Random Walks of 10^5 steps each')
plt.legend()

fig= plt.figure()
plt.plot(x,y,'--r',label='Gaussian Fit')
sns.histplot(sums, stat = 'density', ec=None, color='green', binwidth = 2, binrange = (-1002,1002), label='Bins[...-2,0,2,..]')
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
filename = "dist_sum_random_walk.pdf"
#call the function
save_image(filename)

