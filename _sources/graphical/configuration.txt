Configuring Braviz
===================

Braviz uses a configuration file to load initial settings. The configuration file is located
at the braviz applications directory and can be opened in any text editor.

The file will look like this

.. literalinclude:: ../../../braviz/readAndFilter/braviz.cfg
    :language: cfg


Braviz
--------

The first field in this section contains the name of the current project. If you have several projects you may
select one by changing this field.

The *logger* field is used to select where program output is stored. It can be the terminal, or it can be stored
in a file. The valid values are ``console`` and ``log``.

Default variables
------------------

In this section you can specify the names of the variables which you want to be displayed by default on the applications
There are two nominal variables and two real variables.

Here you also need to specify the variable which is used for selecting the dominant and non-dominant hemisphere of
each subject. This should be a nominal variable. The *left_handed_label* is the value the variable takes when the
subject is left handed, and therefore the dominant hemisphere is the right hemisphere. In all other cases
the dominant hemisphere will be the left.

Finally you can specify another nominal variable which defines a control population. The *reference_var_label* is
the value that the variable takes on subjects from the reference population.

Defaults
---------

Here you can specify the default subject, which is the one that will appear when you first open applications.


Changing file location (advanced)
-----------------------------------

There is another configuration file associated to each project. For a project called *kmc400* this file
will be called ``kmc400_hosts.cfg``. This file contains a list of entries like this one

.. code-block:: cfg

    [Echer]
    data root = H:/kmc400
    dynamic data root = H:/kmc400-braviz
    memory (mb) = 8000

The section name represents the name of a machine. You should first of all search for a section named
after your machine. The *data root* field contains the root path to the project data; the
*dynamic data root* contains the path for the directory in which braviz stores its data; and finally the
*memory (mb)* field contains the maximum amount of memory that braviz will try to use in a single process.