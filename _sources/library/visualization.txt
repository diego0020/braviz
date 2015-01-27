.. module:: braviz.visualization

***********************************
Visualization
***********************************


3D Geometry Visualization
---------------------------

Braviz relies on `VTK <vtk.org>`_ for 3D visualization. The classes and functions in this module are meant to wrap
common vtk tasks in order to make it easier to implement brain visualizations. The main modules used for this
purpose are:

- Simple VTK (:mod:`~braviz.visualization.simple_vtk`) : Several utilities that help displaying data in vtk. Includes
  the :class:`~braviz.visualization.simple_vtk.SimpleVtkViewer`, a lightweight viewer useful for testing.
  see :doc:`simple_vtk`

- Subject Viewer (:mod:`~braviz.visualization.subject_viewer`) : Implements a powerful viewer and Qt4 Widget which
  directly requests data, and handles subject and space changes.
  see :doc:`subject_viewer`

The module :mod:`~braviz.visualization.fmri_view` contains some low level utilities for displaying fMRI data.
The module :mod:`~braviz.visualization.checkerboard_view` implements a widget that shows two images in a checkboard
pattern. It is intended to check the registration between different modalities.

.. toctree::
    :hidden:

    simple_vtk
    subject_viewer
    fmri_view
    checkboard_view


Statistical Visualization
---------------------------

One of the strengths of braviz is combining scientific visualizations and statistical visualizations. For visualizing
tabular data the following options exist.

Matplotlib based visualization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The most direct way to visualize statistical data is using the
`seaborn <http://stanford.edu/~mwaskom/software/seaborn/>`_ library. The module
:mod:`~braviz.visualization.matplotlib_qt_widget` wraps several of seaborn plots into an interactive qt widget.

.. toctree::
    :hidden:

    matplotlib_widget

Experimental D3 based visualization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There is some experimental support for web-based visualizations using the `D3 <d3.org>`_ library, which
are served from a `tornado web server <http://www.tornadoweb.org/>`_ . These visualizations can be displayed in
Qt applications using a `QWebView <http://qt-project.org/doc/qt-4.8/qwebview.html>`_ but the performance is not optimal.
It is better to display them in a full browser. We are still working on tightening the integration between this kind
of visualizations with the rest of the system.

.. toctree::
    :hidden:

    d3_viz

See the module :mod:`~braviz.visualization.d3_visualizations`.

