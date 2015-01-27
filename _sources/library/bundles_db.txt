.. module:: braviz.readAndFilter.bundles_db

Bundles Database
=================

Fiber bundles definitions can be stored in the database. Bundles can be defined as a flat list of checkpoints, or more
general logical structures.

Notice these fibers can be accessed using the :meth:`~braviz.readAndFilter.base_reader.BaseReader.get` method, like
::

    reader.get("fibers",119,db-id=10)

Load
-----

.. autofunction:: get_bundle_ids_and_names
.. autofunction:: get_bundles_list
.. autofunction:: get_bundle_name
.. autofunction:: check_if_name_exists

.. autofunction:: get_logic_bundle_dict
.. autofunction:: get_bundle_details

Save
-----


.. autofunction:: save_checkpoints_bundle
.. autofunction:: save_logic_bundle
