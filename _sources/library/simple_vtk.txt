.. module:: braviz.visualization.simple_vtk

Simple VTK Visualization
==========================

This module contains utilities for working with `VTK <vtk.org>`_  visualizations.

Simple VTK Viewer
-----------------

The simple vtk viewer is a limited viewer class that wraps most of the vtk boilerplate code. It is meant to
do simple tests or to use interactively from the python console.

.. autoclass:: SimpleVtkViewer
    :members:


VTK Widgets
--------------------

.. warning:: Sphinx bug, methods are not *static*

.. autoclass:: persistentImagePlane
    :members:

.. autoclass::  OutlineActor
    :members:

.. autoclass::  OrientationAxes
    :members:

.. autoclass:: cursors
    :members:

Other Utilities
-----------------

.. autofunction:: save_ren_win_picture

.. autofunction:: build_grid

.. autofunction:: remove_nan_from_grid

.. autofunction:: get_arrow

.. autofunction:: get_window_level


