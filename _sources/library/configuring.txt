Configuring
===========

Several Braviz parameters are available to end-users via a configuration file names `braviz.cfg` and located
in the :mod:`braviz.applications` directory. This files are parsed by the python :mod:`ConfigParser` module.

Configuration file
-------------------

The default config file is


.. literalinclude:: ../../../braviz/readAndFilter/braviz.cfg
    :language: cfg

Braviz
^^^^^^^

The ``project`` field defines the project that will be used in the following session. This defines the
:class:`~braviz.readAndFilter.base_reader.BaseReader` subclass that will be used, and according to it the location for
the database and cache files.

The ``server_port`` field contains the port in which the Braviz Web server will listen for http connections.

The ``logger`` field can take the values ``console``, ``file`` or ``web_logger``. In the first case all logging is done to the terminal,
in the second case it is stored in the ``logs`` directory inside
:meth:`~braviz.readAndFilter.base_reader.BaseReader.get_auto_dyn_data_root`
Finally, logging messages are sent ass HTTP requests to the address specified in the ``web_logger_server`` field of this section.




Default_Variables
^^^^^^^^^^^^^^^^^^

This variables are shown by default in several applications. The user may use this field to choose the variables which
are more important to them.

The ``laterality`` variable is used to solve which is the dominant hemisphere for each participant, it is assumed to be
the left side unless its value is ``left_handed_label``.

The ``reference_pop_var`` defines a reference population, where its value is equal to ``reference_pop_label``.
This is used in some applications to calculate a typical range for variable values.

Defaults
^^^^^^^^^

The ``default_subject`` field specifies the subject that will be loaded by default at the start of applications.

VTK
^^^^

.. deprecated:: 2.0
    It is recommended to use interaction style ``trackballCamera`` and a degraded gray background color.

The ``background`` field is used in legacy applications to select a background color for all vtk viewers.

The ``interaction_style`` is used in legacy applications to select a different
`interaction style <http://www.vtk.org/doc/nightly/html/classvtkInteractorStyle.html>`_
for vtk viewers.

Host Configuration
------------------

Host configuration files contain information for configuring auto readers (see :doc:`reader`). This files are named
after the project they belongs to. For example the file for the *kmc* project would be named *kmc_hosts.cfg*. This
files use the same syntax as the standard configuration files (:mod:`~braviz.readAndFilter.config_file`).

This file contains the parameters required to create a reader in specific hosts. This allows using the same installation
in different machines. When creating an autoreader the hostname is found using :func:`platform.node`, afterwards
a section with that name is located in the *_hosts.cfg* file. The options found in this section are returned as a
dictionary which may be used by :func:`~braviz.readAndFilter.base_reader.BaseReader.get_auto_reader`. A section
in such a file may look like this

.. code-block:: cfg

    [Echer]
    data root = H:/kmc400
    dynamic data root = H:/kmc400-braviz
    memory (mb) = 8000


Implementation
----------------

Configuration file access is implemented in the module :mod:`braviz.readAndFilter.config_file`

.. currentmodule:: braviz.readAndFilter.config_file

.. module:: braviz.readAndFilter.config_file
    :synopsis: Read Braviz Configuration files



BravizConfig Class
^^^^^^^^^^^^^^^^^^

.. autoclass:: BravizConfig()

    .. automethod:: get_default_variables
    .. automethod:: get_laterality
    .. automethod:: get_reference_population
    .. automethod:: get_default_subject
    .. automethod:: get_background
    .. automethod:: get_interaction_style

Read Configuration
^^^^^^^^^^^^^^^^^^^^^

.. autofunction:: get_config
.. autofunction:: get_apps_config
.. autofunction:: get_host_config

Create config
^^^^^^^^^^^^^^^^^^^^

.. autofunction:: make_default_config