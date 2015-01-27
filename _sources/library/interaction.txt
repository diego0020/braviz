.. module:: braviz.interaction

***********************************
Interaction
***********************************

The interaction module provides higher level tools that can facilitate building Braviz applications.
It also encapsulates data processing algorithms so that they can be shared across applications.


Qt Graphical User Interfaces
------------------------------

Most Braviz Applications use Qt as GUI engine. In this way applications can look familiar to the user in the supported
operating systems, and behave as they expect.

Graphical interfaces can be built by code, or using the `Qt Designer <http://doc.qt.io/qt-5/qtdesigner-manual.html>`_.
The second is preferred for large
applications as it gives you better feedback. You can even sit down with target users and design the interface together
using this tool. GUI generated using Qt Designer are stored as xml files with *.ui* extension, the ``qt_guis`` folder
contains all such used in braviz applications as well as images and other assets. This files are converted into python
modules using the function

.. autofunction:: braviz.interaction.generate_qt_guis.update_guis


.. toctree::
   :hidden:

   qt_dialogs
   qt_models
   qt_widgets


Dialogs
^^^^^^^^

The :mod:`~braviz.interaction.qt_dialogs` contains Braviz common dialogs which can be reused across applications.

See :doc:`qt_dialogs`

Models
^^^^^^^

The :mod:`~braviz.interaction.qt_models` contains qt models which can be used in the
`Model / View <http://qt-project.org/doc/qt-4.8/model-view-programming.html>`_ Qt pattern.

See :doc:`qt_models`

Widgets
^^^^^^^^

The :mod:`~braviz.interaction.qt_widgets` contains specific braviz widgets which can be reused across applications.
Notice that visualization related widgets are found inside the :mod:`~braviz.visualization` module.

See :doc:`qt_widgets`


Applications communication
----------------------------

All braviz applications share the same database, and the main way in which they communicate is through it.
However applications may also send and receive messages from all other running applications, in order to
coordinate the whole system.

See :doc:`communication`

.. toctree::
   :hidden:

   communication


R Statistical processing
-----------------------------------

Braviz connects with the R software using the `RPy2 <http://rpy.sourceforge.net/>` package.
These statistical functions are isolated in the module :mod:`~braviz.interaction.r_functions`

See :doc:`r_funcs`

.. toctree::
   :hidden:

   r_funcs


Structures processing
------------------------

Sometimes it is required to perform additional processing steps on the geometrical structure returned by braviz. For
example calculating scalar measure or descriptors. This module intends to group such functions. Notice that when the
intend of the processing is improving visualizations, functions should be located in :mod:`braviz.visualization`.

See :doc:`struc_proc`


.. toctree::
   :hidden:

   struc_proc