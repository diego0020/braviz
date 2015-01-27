.. module:: braviz.visualization.subject_viewer

Subject Viewer
=================

This module implements high level data viewers. They handle all VTK, and data access operations.
They are made of *data managers* which specialize on handling specific data types. They maintain its state, and
specially important, support changing subject or coordinate systems while keeping the other parameters constant. In
this way it is possible to compare two subjects.


These viewers are designed to be used as widgets it Qt applications. For that matter specific Widget wrappers
exist for each of them. This wrappers can send PyQt signals on certain events, like picking the screen.




Full Viewers
--------------

These classes combine different data managers to create integrated visualizations.

.. autoclass::  SubjectViewer
    :members:

.. autoclass::  fMRI_viewer
    :members:

.. autoclass::  OrthogonalPlanesViewer
    :members:

.. autoclass::  MeasurerViewer
    :members:

Data Managers
-------------

Managing the visualization state is simplified by the data managers, which focus on specific data types.

.. autoclass::  ImageManager
    :members:

.. autoclass::  ModelManager
    :members:

.. autoclass::  TractographyManager
    :members:

.. autoclass::  TraculaManager
    :members:

.. autoclass::  SurfaceManager
    :members:

.. autoclass::  SphereProp
    :members:

.. autoclass::  FmriContours
    :members:


PyQt Widgets
--------------

These classes wrap the viewers so that they can be connected into Qt applications, in theory such classes could
be built for other graphical interface libraries.

.. autoclass::  QSubjectViewerWidget
    :members:

.. autoclass::  QOrthogonalPlanesWidget
    :members:

.. autoclass::  QMeasurerWidget
    :members:

.. autoclass::  QFmriWidget
    :members:

Utilities
-----------

.. autofunction::  do_and_render

.. autoclass::  FilterArrows
    :members:

.. autoclass:: AdditionalCursors
    :members:

Examples
---------
