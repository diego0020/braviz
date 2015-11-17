Tabular Data
=============
.. module:: braviz.readAndFilter.tabular_data

Tabular data is data usually stored in spreadsheets. It can contain important information about subject background
and performance. In large projects there may be several hundreds of variables, and a very wide spreadsheet would be
required to store them.

Data is stored in a structure that can be viewed as a table. The first column would contain the ids of the subjects
in the study, and the first row would contain the variable names. The values of the variables would be stored in the
rest of the table.

Real variables are stored as float numbers, and the metadata contains the minimum, maximum and optimal value for each
variable. This parameters can be modified by the subject, and it is not enforced that values lay in this range, however
applications may check this and give warnings if there is an inconsistency. This metadata is also useful for plotting.

Nominal variables are stored as numerical labels. Metadata contains a table that maps numerical labels to strings. Which
can be accessed with the function :func:`~.get_labels_dict`, for example

::

    >>> get_labels_dict(4)
    {
        1 : "male" ,
        2 : "female" ,
    }

Several of the functions in this module return instances of :class:`pandas.DataFrame`.

Subjects
---------

Read
^^^^^
.. autofunction:: get_subjects

Modify
^^^^^^

.. autofunction:: recursive_delete_subject

Variables
---------

Read
^^^^^

.. autofunction:: get_variables
.. autofunction:: get_var_idx
.. autofunction:: get_var_name
.. autofunction:: does_variable_name_exists

Modify
^^^^^^

.. autofunction:: register_new_variable
.. autofunction:: recursive_delete_variable

Special variables
^^^^^^^^^^^^^^^^^
.. autodata:: LATERALITY
.. autodata:: LEFT_HANDED
.. autodata:: UBICAC

Values
-------

Read
^^^^^

.. autofunction:: get_data_frame_by_index
.. autofunction:: get_data_frame_by_name
.. autofunction:: get_laterality
.. autofunction:: get_var_value
.. autofunction:: get_subject_variables

Modify
^^^^^^

.. autofunction:: update_variable_value
.. autofunction:: update_multiple_variable_values
.. autofunction:: update_variable_values
.. autofunction:: add_data_frame

Metadata
---------

Read
^^^^^

.. autofunction:: is_variable_real
.. autofunction:: is_variable_nominal
.. autofunction:: is_variable_name_real
.. autofunction:: is_variable_name_nominal
.. autofunction:: are_variables_real
.. autofunction:: are_variables_nominal
.. autofunction:: are_variables_names_real
.. autofunction:: are_variables_names_nominal
.. autofunction:: get_labels_dict
.. autofunction:: get_labels_dict_by_name
.. autofunction:: get_minimum_value
.. autofunction:: get_maximum_value
.. autofunction:: get_min_max_values
.. autofunction:: get_min_max_values_by_name
.. autofunction:: get_min_max_opt_values_by_name
.. autofunction:: get_var_description
.. autofunction:: get_var_description_by_name
.. autofunction:: get_variable_normal_range

Modify
^^^^^^

.. autofunction:: save_is_real
.. autofunction:: save_is_real_by_name
.. autofunction:: save_nominal_labels
.. autofunction:: save_nominal_labels_by_name
.. autofunction:: save_real_meta
.. autofunction:: save_real_meta_by_name
.. autofunction:: save_var_description
.. autofunction:: save_var_description_by_name

Create New Database
----------------------

.. autofunction:: initialize_database