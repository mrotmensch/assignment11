import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt


def plot_for_results(daily_ret, position):

	for p in position:
		plt.hist(daily_ret[p], 100, range=[-1,1])
		plt.savefig("histogram_" + "%04d"%(p) + "_pos.pdf", format="pdf")
		plt.close()
