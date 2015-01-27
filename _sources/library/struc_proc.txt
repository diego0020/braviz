
Geometric Processing
=====================

The following modules group operations on geometric structures returned
by the :mod:`~braviz.readAndFilter` module. These operations are not intended
to improve visualization, but to produce data for the user which can be used
in statistical analyses or in other applications.

.. module:: braviz.interaction.structure_metrics

Structure metrics
------------------

Polydata metrics
^^^^^^^^^^^^^^^^^^^^^^

.. autofunction:: get_mult_struct_metric
.. autofunction:: get_struct_metric
.. autofunction:: get_fibers_metric
.. autofunction:: cached_get_struct_metric_col
.. autofunction:: get_scalar_from_fiber_ploydata
.. autofunction:: get_fiber_scalars_from_db
.. autofunction:: get_fiber_scalars_from_waypoints

Image metrics
^^^^^^^^^^^^^^^^^^

.. autofunction:: mean_inside
.. autofunction:: aggregate_in_roi

.. autoclass:: AggregateInRoi
    :members:


latearlity helpers
^^^^^^^^^^^^^^^^^^^^
.. autofunction:: get_right_or_left_hemisphere
.. autofunction:: solve_laterality

.. module:: braviz.interaction.descriptors

Geometric descriptors
------------------------

.. autofunction:: get_descriptors


.. module:: braviz.interaction.roi

Roi operations
----------------

.. autofunction:: generate_roi_image

.. autofunction:: export_roi
