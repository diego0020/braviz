.. module:: braviz.readAndFilter.user_data

User Data
=========

The database can store data generated during the analysis which could enrich further steps of the analysis or recall
past analyses.

Scenarios
---------

Scenarios are application states, which should be written into a python dictionary. Additionally, scenarios are stored
with a name, a description, creation date, and current application.

To ease retrieving the scenario an screen-shot should also be generated. It should be saved at

``<dyn_data_root>/braviz_data/scenarios/scenario_<scn_id>.png``

Where ``<dyn_data_root>`` is the value returned by :func:`~braviz.readAndFilter.braviz_auto_dynamic_data_root` and
``<scn_id>`` is the database id for the scenario.

Scenarios can also be linked with variables. For example when creating a variable, the application state at that point can be
saved as a scenario and linked to the new variable. This will allow the user to recall the conditions in which the
variable was created.

Read
^^^^

.. autofunction:: get_scenario_data_dict
.. autofunction:: get_scenarios_data_frame

Write
^^^^^

.. autofunction:: save_scenario
.. autofunction:: update_scenario
.. autofunction:: delete_scenario

Link with variables
^^^^^^^^^^^^^^^^^^^

.. autofunction:: link_var_scenario
.. autofunction:: get_variable_scenarios
.. autofunction:: count_variable_scenarios


Subsamples
-----------

Subsamples are subsets from the population. This are useful for testing hypotheses only in an group of interest. They
are stored as python sets together with a name, a description and the size.

Read
^^^^

.. autofunction:: get_sample_data
.. autofunction:: get_samples_df
.. autofunction:: sample_name_existst


Write
^^^^^

.. autofunction:: save_sub_sample
.. autofunction:: delete_sample

Comments
---------

It is possible to save textual comments about particular subjects, which can remind the analysts of important
information about the subject in future analyzes. This is still very primitive.

.. autofunction:: get_comment
.. autofunction:: update_comment
