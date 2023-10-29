import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import norm
from matplotlib.backends.backend_pdf import PdfPages

plt.rcParams["figure.figsize"] = [7.00, 5.00]
plt.rcParams["figure.autolayout"] = True

# First

sums=pd.read_csv("dist_sum_random.dat", header = None)
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
plt.plot(x,y,'--r')
sns.histplot(sums, binwidth=0.5, ec=None, stat = "density")
plt.xlabel('Sum')
plt.ylabel('Probability Density')
plt.title('Distribution of the 10K Sum(s) of 10^4 Random No. between [0,1] ')
plt.legend(['Gaussian Fit',"Binwidth=0.5"])

fig = plt.figure()
plt.plot(x,y,'--r', label='Gaussian Fit')
sns.histplot(sums, binwidth=1, ec=None, stat = "density", label="Binwidth=1")
plt.xlabel('Sum')
plt.ylabel('Probability Density')
plt.title('Distribution of the 10K Sum(s) of 10^4 Random No. between [0,1]')
plt.legend()

fig = plt.figure()
plt.plot(x,y,'--r', label='Gaussian Fit')
sns.histplot(sums, binwidth=2, ec=None, stat = "density", label="Binwidth=2")
plt.xlabel('Sum')
plt.ylabel('Probability Density')
plt.title('Distribution of the 10K Sum(s) of 10^4 Random No. between [0,1]')
plt.legend()

# Second

sums=pd.read_csv("dist_sum_random_2.dat", header = None)
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
sns.histplot(sums, binwidth=0.5, stat = "density", ec=None, color = 'orange', label="Binwidth=0.5")
plt.ylabel('Probability Density')
plt.title('Distribution of the 10K Sum(s) of 10^4 Random No. between [-1,1]')
plt.legend()

fig = plt.figure()
plt.plot(x,y,'--r',label='Gaussian Fit')
sns.histplot(sums, binwidth=1, stat = "density", ec=None, color = 'orange', label="Binwidth=1")
plt.xlabel('Sum')
plt.ylabel('Probability Density')
plt.title('Distribution of the 10K Sum(s) of 10^4 Random No. between [-1,1]')
plt.legend()

fig = plt.figure()
plt.plot(x,y,'--r',label='Gaussian Fit')
sns.histplot(sums, binwidth=2, stat = "density", ec=None, color = 'orange', label="Binwidth=2")
plt.xlabel('Sum')
plt.ylabel('Probability Density')
plt.title('Distribution of the 10K Sum(s) of 10^4 Random No. between [-1,1]')
plt.legend()

# Third

sums=pd.read_csv("dist_sum_random_3.dat", header = None)
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
sns.histplot(sums, binwidth=0.5, stat = "density", ec=None, color='green', label="Binwidth=0.5")
plt.ylabel('Probability Density')
plt.title('Distribution of the 100K Sum(s) of 10^4 Random No. between [-1,1]')
plt.legend()

fig = plt.figure()
plt.plot(x,y,'--r',label='Gaussian Fit')
sns.histplot(sums, binwidth=1, stat = "density", ec=None, color='green',label="Binwidth=1")
plt.xlabel('Sum')
plt.ylabel('Probability Density')
plt.title('Distribution of the 100K Sum(s) of 10^4 Random No. between [-1,1]')
plt.legend()

fig = plt.figure()
plt.plot(x,y,'--r',label='Gaussian Fit')
sns.histplot(sums, binwidth=2, stat = "density", ec=None, color='green', label="Binwidth=2")
plt.xlabel('Sum')
plt.ylabel('Probability Density')
plt.title('Distribution of the 100K Sum(s) of 10^4 Random No. between [-1,1]')
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
filename = "dist_sum_random.pdf"
#call the function
save_image(filename)
