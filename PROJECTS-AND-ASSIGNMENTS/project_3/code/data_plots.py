# Importable module containing various classes plotting figures that evaluate
# categorical predictions.


class Roc:

    def __init__(self, y_test=None, y_pred=None):
        self.classes = None

    def auc_score(self, y_test, y_pred):
        '''
        This is just the sklearn roc_auc_score in a wrapper that makes it work
        even if the target is multi-categorical or has not been label encoded.
        '''
        from sklearn.preprocessing import label_binarize
        from sklearn.metrics import roc_auc_score

        self.classes = list(set(y_test) | set(y_pred))
        is_multi_categorical = len(self.classes) > 2

        # Avoids label_binarize if unnecessary.
        if not is_multi_categorical:
            try:
                return roc_auc_score(y_test, y_pred)
            except TypeError:
                pass
        lb_test = label_binarize(y_test, classes=self.classes)
        lb_pred = label_binarize(y_pred, classes=self.classes)

        # Returns the mean roc auc score. The closer it is to 1, the better.
        return roc_auc_score(lb_test, lb_pred)

    def plot_auc(self, x, auc_scores, lw=2, title=None, xlabel=None, labels=None, **kwargs):
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(**kwargs)
        for i, scores in enumerate(auc_scores):
            if labels is None:
                labels = range(len(auc_scores))
            ax.plot(x, scores, label=labels[i])
        ax.set_xlabel(xlabel)
        ax.set_ylabel('AUC score')
        ax.set_title(title)
        ax.legend(loc='best')
        plt.show()
        plt.close()

    def plot(self, y_test, y_pred, average='macro', lw=2, title=None, labels=None, **kwargs):
        '''
        A convenience function for plotting Receiver Operating Characteristic
        (ROC) curves.

        labels accepts a dictionary of the column values mapped onto class
        names. If the column values are simply integers, it is possible to just
        pass a list.
        '''
        import numpy as np
        import matplotlib.pyplot as plt
        from sklearn.preprocessing import label_binarize
        from sklearn.metrics import roc_curve, auc
        from itertools import cycle
        from scipy import interp

        # Gets all unique categories.
        self.classes = list(set(y_test) | set(y_pred))
        is_multi_categorical = len(self.classes) > 2

        # Converts each categorical prediction into a list of 0 and 1 for each
        # category.
        lb_test = label_binarize(y_test, classes=self.classes)
        lb_pred = label_binarize(y_pred, classes=self.classes)

        # Initialize graph.
        fig, ax = plt.subplots(**kwargs)

        if is_multi_categorical:

            # Compute ROC curve and ROC area for each class.
            fpr = {}
            tpr = {}
            roc_auc = {}
            for i, k in enumerate(self.classes):
                fpr[k], tpr[k], _ = roc_curve(lb_test[:, i], lb_pred[:, i])
                roc_auc[k] = auc(fpr[k], tpr[k])

            if average == 'micro' or average == 'both':
                # Compute micro-average ROC curve and ROC area.
                fpr['micro'], tpr['micro'], _ = roc_curve(
                    lb_test.ravel(), lb_pred.ravel())
                roc_auc['micro'] = auc(fpr['micro'], tpr['micro'])

                ax.plot(fpr['micro'], tpr['micro'], ':r',
                        label=f'micro-average ROC curve (area = {roc_auc["micro"]:0.2f})', lw=lw)

            if average == 'macro' or average == 'both':
                # Compute macro-average ROC curve and ROC area.

                # First aggregate all false positive rates.
                all_fpr = np.unique(np.concatenate(
                    [fpr[k] for k in self.classes]))

                # Then interpolate all ROC curves at these points.
                mean_tpr = np.zeros_like(all_fpr)
                for k in self.classes:
                    mean_tpr += interp(all_fpr, fpr[k], tpr[k])

                # Finally average it and compute AUC
                mean_tpr /= len(self.classes)

                fpr['macro'] = all_fpr
                tpr['macro'] = mean_tpr
                roc_auc['macro'] = auc(fpr['macro'], tpr['macro'])

                ax.plot(fpr['macro'], tpr['macro'], ':b',
                        label=f'macro-average ROC curve (area = {roc_auc["macro"]:0.2f})', lw=lw)

            # Plot ROC curve for each category.
            colors = cycle(['teal', 'darkorange', 'cornflowerblue'])
            if labels is None:
                labels = self.classes
            for k, color in zip(self.classes, colors):
                ax.plot(fpr[k], tpr[k], color=color,
                        label=f'ROC curve of {labels[k]} (area = {roc_auc[k]:0.2f})', lw=lw)

        else:
            fpr, tpr, _ = roc_curve(lb_test, lb_pred)
            roc_auc = auc(fpr, tpr)

            if labels is None:
                labels = 'target'

            ax.plot(
                fpr, tpr, label=f'ROC curve of {labels} (area = {roc_auc:0.2f})', lw=lw)

        # Plot the curve of the baseline model (mean).
        ax.plot([0, 1], [0, 1], 'k--')
        ax.set_xlim([0.0, 1.0])
        ax.set_ylim([0.0, 1.05])
        ax.set_xlabel('False Positive Rate')
        ax.set_ylabel('True Positive Rate')
        ax.set_title(title)
        ax.legend(loc='best')
        plt.show()
        plt.close()
