********************
Braviz Data Base
********************

.. toctree::
    :hidden:

    tabular_data
    user_data
    geom_db
    bundles_db

Braviz uses a database to store analysis variables, data saved by users, and small geometric structures.
In the current implementation this database is `sqlite <slite.org>`_, but this may change in the future.
The database file is located on

``<dynaimc data root> / braviz_data / tabular_data.sqlite``

where dynamic data root is the path returned by

:func:`braviz.readAndFilter.braviz_auto_dynamic_data_root`


Variables
---------

The module :mod:`~braviz.readAndFilter.tabular_data` contains functions to save and retrieve

- Nominal and Numerical Variables
- Variables meta-data
- Subjects in the project

See :doc:`tabular_data`

User Data
----------

The module :mod:`~braviz.readAndFilter.user_data` contains functions to save and retrieve

- Application state (Scenarios)
- Sub-samples
- Comments on subjects

See :doc:`user_data`

Geometric Data
--------------

The module :mod:`~braviz.readAndFilter.geom_db` contains functions to save and retrieve geometric structures, currently:

- Lines
- Spheres

See :doc:`geom_db`

Fiber Bundles
----------------
The :mod:`~braviz.readAndFilter.bundles_db` contains functions to save and retrieve fiber bundles defined by the user

- With waypoints
- Logical trees

See :doc:`bundles_db`

Checking db completeness
--------------------------

.. module:: braviz.readAndFilter.check_db

The module mod:`~braviz.readAndFilter.check_db` contains the following function

.. autofunction:: braviz.readAndFilter.check_db.verify_db_completeness