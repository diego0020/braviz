from PyQt4 import QtGui
import numpy as np
import pandas as pd
from braviz.visualization import matplotlib_qt_widget


class TestFrame(QtGui.QFrame):
    def __init__(self):
        QtGui.QFrame.__init__(self)
        layout = QtGui.QVBoxLayout()
        self.setLayout(layout)
        msg = "Testing MatplotWidget\n\nUse the button to cycle\nover the different plots"
        self.plot_widget = matplotlib_qt_widget.MatplotWidget(self, initial_message=msg)
        button = QtGui.QPushButton("Next Plot")
        button.clicked.connect(self.draw_next)

        layout.addWidget(self.plot_widget)
        layout.addWidget(button)

        self.current_plot = -1
        self.plot_funcs = ["draw_bars", "draw_group_bars",
                           "draw_coefficients_plot", "draw_scatter",
                           "draw_color_scatter", "draw_intercept",
                           "draw_residuals", "draw_message"]

    def draw_next(self):
        self.current_plot = (self.current_plot + 1) % len(self.plot_funcs)
        func_name = self.plot_funcs[self.current_plot]
        func = getattr(self, func_name)
        func()

    def draw_message(self):
        msg = "End of cycle\nUse the button to cycle again"
        self.plot_widget.draw_message(msg)

    def draw_bars(self):
        data = np.random.standard_exponential(10)
        df = pd.DataFrame({"exponential": data})
        self.plot_widget.draw_bars(df)

    def draw_group_bars(self):
        data = np.random.standard_exponential(10)
        groups = np.random.random_integers(0, 3, 10)
        df = pd.DataFrame({"exponential": data, "groups": groups})
        self.plot_widget.draw_bars(df, orientation="horizontal")

    def draw_coefficients_plot(self):
        centers = np.random.randn(10)
        std_errors = np.abs(np.random.randn(10))*2+0.2
        ci95_width = np.random.uniform(1, 2, size=10) * std_errors
        ci95 = [(c - w, c + w) for c, w in zip(centers, ci95_width)]
        names = ["(intecept)"]+ ["coef_%d" % i for i in xrange(1,10)]
        df = pd.DataFrame({"CI_95": ci95, "Std_error": std_errors, "Slope": centers},
                          index=names)
        self.plot_widget.draw_coefficients_plot(df)

    def draw_scatter(self):
        noise = np.random.randn(40) * 4
        x = np.random.uniform(0, 10, 40)
        y = 2 * x + 3 + noise
        df = pd.DataFrame({"x": x, "y": y})
        self.plot_widget.draw_scatter(df, "x", "y")

    def draw_color_scatter(self):
        noise = np.random.randn(40) * 4
        x = np.random.uniform(0, 10, 40)
        groups = np.random.randint(1, 4, 40)
        y = -2 * groups + 3 + noise
        df = pd.DataFrame({"x": x, "y": y, "groups": groups})
        self.plot_widget.draw_scatter(df, "x", "y", hue_var="groups")

    def draw_intercept(self):
        noise = np.random.randn(40)
        groups = np.random.randint(1,4,40)
        group_labels = dict([(k,"group %d"%k) for k in xrange(1,4)])
        data = groups*2 + noise
        df = pd.DataFrame({"data" : data, "groups" : groups})
        self.plot_widget.draw_intercept(df,"data","groups",group_labels=group_labels)

    def draw_residuals(self):
        residuals = np.random.randn(40)
        fitted = np.random.uniform(0,5,40)
        self.plot_widget.draw_residuals(residuals,fitted)

#-----------TestFrameEnd----------------------


# Launch as stand alone if directly executed
if __name__ == "__main__":
    app = QtGui.QApplication([])
    frame = TestFrame()
    frame.show()
    app.exec_()
