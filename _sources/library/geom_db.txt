.. module:: braviz.readAndFilter.geom_db

Geometric Data
===============

The database can be used to store simple geometric structures, which are usually used as regions of interests. This
structures must be defined in a concrete coordinates system. There is one main table which stores general information
about the structure (roi), and a table for each roi type which stores its concrete data for each subject.


ROIs
-----

.. autofunction:: roi_name_exists
.. autofunction:: get_roi_id
.. autofunction:: get_roi_name
.. autofunction:: get_roi_type
.. autofunction:: get_roi_space

.. autofunction:: create_roi
.. autofunction:: recursive_delete_roi

Spheres
--------

Spheres are saved as a center ``(x,y,z)`` and a radius.

.. autofunction:: load_sphere
.. autofunction:: get_available_spheres_df
.. autofunction:: get_all_spheres
.. autofunction:: subjects_with_sphere
.. autofunction:: save_sphere
.. autofunction:: copy_spheres


Lines
------

Lines are saved as a starting point ``(xo,yo,zo)`` and an end point ``(xf,yf,zf)``

.. autofunction:: load_line
.. autofunction:: get_available_lines_df
.. autofunction:: subjects_with_line
.. autofunction:: save_line
