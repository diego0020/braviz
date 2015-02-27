.. module:: braviz.interaction.qt_models


*************************************
Braviz Qt Models
*************************************

This module provides several classes that can be used in the
`Model / View <http://qt-project.org/doc/qt-4.8/model-view-programming.html>`_ Qt pattern,
so they inherit from :obj:`QAbstractItemModel`.
Only methods that are not part of the Qt interface are shown here.


Generic models
---------------

This models are designed to be generic, and they don't make any assumptions about the data.

.. autoclass:: SimpleSetModel
    :members:

.. autoclass:: SimpleCheckModel
    :members:

.. autoclass:: DataFrameModel
    :members:


Tabular Data Models
--------------------

These models are designed to work with the braviz database and to allow users to interact with the data stored
there through a graphical interface.

Variables
^^^^^^^^^^^^

.. autoclass:: VarListModel
    :members:

.. autoclass:: SubjectDetails
    :members:

.. autoclass:: ContextVariablesModel
    :members:

.. autoclass:: NewVariableValues
    :members:

.. autoclass:: NominalVariablesMeta
    :members:

Subjects and samples
^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: SampleTree
    :members:

.. autoclass:: SubjectsTable
    :members:

.. autoclass:: SubjectChecklist
    :members:

.. autoclass:: SubjectCheckTable
    :members:

.. autoclass:: SamplesSelectionModel
    :members:

.. autoclass:: SamplesFilterModel
    :members:


Statistics
^^^^^^^^^^^

.. autoclass:: VarAndGiniModel
    :members:

.. autoclass:: AnovaRegressorsModel
    :members:

.. autoclass:: AnovaResultsModel
    :members:


Bundles
-----------------------

.. autoclass:: SimpleBundlesList
    :members:

.. autoclass:: BundlesSelectionList
    :members:


Scenarios
-----------

.. autoclass:: ScenariosTableModel
    :members:


.. module:: braviz.interaction.qt_structures_model

Structures model
-----------------

.. autoclass:: StructureTreeModel
    :members:

Helper
^^^^^^^

.. autoclass:: StructureTreeNode
    :members:


.. module:: braviz.interaction.logic_bundle_model



Logic bundle model
-------------------

.. autoclass:: LogicBundleQtTree
    :members:

Helpers
^^^^^^^

.. autoclass:: LogicBundleNode
    :members:

.. autoclass:: LogicBundleNodeWithVTK
    :members:

