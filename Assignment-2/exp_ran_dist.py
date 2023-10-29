import pandas as pd
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

plt.rcParams["figure.figsize"] = [11.69,8.27]
plt.rcParams["figure.autolayout"] = True

df = pd.read_csv("exp_ran_dist.dat", header = None)

df1 = df.iloc[:,0]
df_x = df.iloc[0:10000,0]
df_y = df.iloc[10000:20000,0]
std = np.std(df1)
mean = np.mean(df1)

fig = plt.figure()
sns.histplot(df, stat = 'probability', ec = None, bins = 1000, label = 'Bins=1000'+'\n'+'$\mu=$'+'%.4f'%mean+'\n'+'$\sigma=$'+'%.4f'%std)
plt.xlabel('Random numbers',fontsize = 16)
plt.ylabel('Probability',fontsize = 16)
plt.xticks(fontsize = 10)
plt.yticks(fontsize = 10)
plt.title('Exponentially distributed ($e^{-2x}$) $10^6$ random numbers', fontsize = 20)
plt.legend(fontsize = 18)
plt.savefig('Q4b_exp_dist.pdf')

fig = plt.figure()
plt.plot(df_x,df_y,'.g')
plt.xlabel("1st set of random numbers", fontsize = 16)
plt.ylabel("2nd set of random numbers", fontsize = 16)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.title("Scatter plot of two sets $10^4$ exponentially($e^{-2x}$) distributed random numbers", fontsize = 20)
plt.savefig('Q4b_exp_scatter.pdf')
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
filename = "exp_ran_dist.pdf"
#call the function
save_image(filename)
