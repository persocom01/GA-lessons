import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from sklearn.svm import SVC
from sklearn.metrics import mean_squared_error

from ipywidgets import *



class XY(object):

    def __init__(self, class_n):
        self.class_n = class_n

        self.Y = np.array([0]*class_n + [1]*class_n)

        self.class1_x = np.random.randn(class_n, 2)
        self.class2_x = np.random.randn(class_n, 2)

        self.generate_X_matrices()


    def create_X(self, w_diff, h_diff, w_std, h_std):

        c1_hw = [150.-(w_diff/2.), 69.-(h_diff/2.)]
        c2_hw = [150.+(w_diff/2.), 69.+(h_diff/2.)]

        c1x = self.class1_x*[w_std, h_std] + c1_hw
        c2x = self.class2_x*[w_std, h_std] + c2_hw

        X = np.vstack([c1x, c2x])
        return X


    def generate_X_matrices(self):

        self.Xs = {}

        w_diff_range = range(0,101,1)
        h_diff_range = range(0,25,2)
        w_std_range = range(1,21,1)
        h_std_range = range(1,11,1)

        for wd in w_diff_range:
            self.Xs[wd] = {}

            for hd in h_diff_range:
                self.Xs[wd][hd] = {}

                for ws in w_std_range:
                    self.Xs[wd][hd][ws] = {}

                    for hs in h_std_range:
                        X = self.create_X(wd, hd, ws, hs)
                        self.Xs[wd][hd][ws][hs] = X



class SVMPlotter(object):

    def __init__(self, figsize=(9,7), point_size=95):

        self.figsize = figsize
        self.point_size = point_size

        self.colors = dict(blue='#1F77B4',
                           orange='#FF7F0E',
                           green='#2CA02C',
                           red='#D62728',
                           purple='#9467BD',
                           brown='#8C564B',
                           pink='#E377C2',
                           grey='#7F7F7F',
                           yellow='#BCBD22',
                           teal='#17BECF')

        self.model = SVC(kernel='linear', C=1.0)


    def initialize_data(self, class_n=20):
        self.class_n = class_n
        self.XY_container = XY(class_n)


    def matrix_ranges(self, X):
        x1_min, x2_min = np.amin(X, axis=0) - np.std(X, axis=0)/2
        x1_max, x2_max = np.amax(X, axis=0) + np.std(X, axis=0)/2

        x1_range = x1_max - x1_min
        x2_range = x2_max - x2_min

        return x1_min, x1_max, x1_range, x2_min, x2_max, x2_range


    def fit_svm(self, X, y, C=1.0):
        self.model.set_params(C=C)
        self.model.fit(X, y)
        # code taken from:
        # http://scikit-learn.org/stable/auto_examples/svm/plot_svm_margin.html
        margin = 1. / np.sqrt(np.sum(self.model.coef_ ** 2))

        return margin


    def calculate_hyperplane_margin(self, x1_min, x1_max, margin):

        weights = self.model.coef_[0]

        alpha = -weights[0] / weights[1]

        xx = np.linspace(x1_min, x1_max)

        # Intercept does not mean the same thing in SVM as in regression!
        yy = alpha * xx - (self.model.intercept_[0]) / weights[1]

        yy_down = yy + alpha * margin
        yy_up = yy - alpha * margin

        return xx, yy, yy_down, yy_up


    def svm_plot(self, X, y, C=1.0):

        x1_min, x1_max, x1_r, x2_min, x2_max, x2_r = self.matrix_ranges(X)

        margin = self.fit_svm(X, y, C=C)

        xx, yy, yy_down, yy_up = self.calculate_hyperplane_margin(x1_min, x1_max, margin)

        # Set the figure size to be big enough to see stuff
        plt.figure(figsize=self.figsize)

        # plot the line, the points, and the nearest vectors to the plane
        plt.plot(xx, yy, 'k-', lw=4)
        plt.plot(xx, yy_down, 'k--', lw=1.5, color=self.colors['yellow'])
        plt.plot(xx, yy_up, 'k--', lw=1.5, color=self.colors['yellow'])

        plt.scatter(self.model.support_vectors_[:, 0], self.model.support_vectors_[:, 1],
                    s=self.point_size*4, facecolors='none', edgecolors=self.colors['grey'],
                    lw=1.5)

        #plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired, s=self.point_size)
        plt.scatter(X[y==1, 0], X[y==1, 1], color=self.colors['blue'],
                    s=self.point_size, label='female')
        plt.scatter(X[y==0, 0], X[y==0, 1], color=self.colors['red'],
                    s=self.point_size, label='male')

        # set the axis limits:
        plt.xlim(x1_min, x1_max)
        plt.ylim(x2_min, x2_max)

        plt.xlabel('weight (lb)', fontsize=16)
        plt.ylabel('height (in)', fontsize=16)

        plt.title('male vs. female by height and weight\n')
        plt.legend(loc="lower right")

        plt.tick_params(labelsize=14)

        plt.show()


    def svm_plotter(self, log_C=0,
                    weight_diff=50,
                    height_diff=6,
                    weight_std=16,
                    height_std=4):

        X = self.XY_container.Xs[weight_diff][height_diff][weight_std][height_std]
        y = self.XY_container.Y
        self.svm_plot(X, y, C=10**log_C)


    def svm_interact(self):

        log_C = widgets.FloatSlider(min=-6.0, max=6.0, step=0.1,
                                    continuous_update=False, value=-1.5)
        log_C.width = '600px'
        log_C.description = 'log C:'

        weight_diff = widgets.IntSlider(min=0, max=100, step=5,
                                        continuous_update=False, value=50)
        weight_diff.width = '600px'
        weight_diff.description = 'weight diff:'

        height_diff=widgets.IntSlider(min=0, max=24, step=2,
                                      continuous_update=False, value=6)
        height_diff.width = '600px'
        height_diff.description = 'height diff:'

        weight_std=widgets.IntSlider(min=1, max=20, step=1,
                                     continuous_update=False, value=16)
        weight_std.width = '600px'
        weight_std.description = 'weight std:'

        height_std=widgets.IntSlider(min=1, max=10, step=1,
                                     continuous_update=False, value=4)
        height_std.width = '600px'
        height_std.description = 'height std:'


        widgets.interact(self.svm_plotter,
                         log_C=log_C,
                         weight_diff=weight_diff,
                         height_diff=height_diff,
                         weight_std=weight_std,
                         height_std=height_std)
