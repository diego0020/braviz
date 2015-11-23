Set-up Braviz on a New Data-Set
===============================

This guide shows hot to prepare data, and how to configure Braviz
in order to work with new data-sets.

.. toctree::


Process Spatial Data
--------------------

In order to take full advantage of Braviz, it is recommended to run the
following programs on your data

 * FreeSurfer segmentation, surface reconstructions and parcellation
 * Model reconstruction of freeSurfer segmentations
 * Tracula
 * Fitting tensors, and creating FA, MD and DTI images
 * Deterministic tractography
 * SPM first level analysis of functional paradigms
 * SPM-Dartel registration

In the currently configured projects deterministic tractography and tensor fitting
was done using Camino. All of the items in the above list are mandatory except the
FreeSurfer pipeline. The scripts used during the kmc400 project are available
on `github <https://github.com/imaginebog/kmc_proc>`_ as a reference, however for large
projects it is worth using a pipeline framework as Loni or NiPype.

Create a data reader
--------------------

All access to spatial data goes through Braviz, data readers, in this way the
system can be isolated from the underlying file structure. By building an appropriate
reader it is even possible to have data on a remote system. All readers should
inherit from :class:`~braviz.readAndFilter.base_reader.BaseReader`, and implement the abstract methods.

These readers should be located on the :mod:`braviz.readAndFilter` module, in a module named
as the project, in lowercase. For example the reader for a project called *foobar* the module should be called
*braviz.readAndFilter.foobar*, and inside the module there should be a class named *FooBarReader*.

Two full readers are already implemented. The first one (:mod:`braviz.readAndFilter.kmc40`) was for the KMC pilot study.
The file system in this reader was organized first by subject and then by data type. In other words, all of the data
belonging to a subject was contained in the same folder. Additionally the braviz cache and dynamic data was written to
the same folder that contains the spatial data.

The  (:mod:`braviz.readAndFilter.kmc400`) module contains the reader for the full KMC. This study contains images from
about 250 subjects, and therefore it was not practical to copy spatial data to all machines. Therefore usually
data is shared through *samba* as read only, and dynamic data and cache are kept locally on each machine. In this case,
data is tored first by data type, and then by subject, so that the Freesurfer's *SUBJECTS_DIR* can be used directly.

Both of these readers operate in a similar way, the main difference is in the routes required to load files from disk.
The common operations are coded in the :mod:`braviz.readAndFilter.kmc400.kmc_abstract` module. Feel free to use any of these modules as a basis
for your new reader.

The important areas that must be modified are:

* The indices of available fMRI pardigms and images
* The locations of files
* The transformations between coordinate systems
* If required, custom functions to read files and convert to numpy or  vtk.

Remember that the end objective is having a reader that conforms to the :class:`~braviz.readAndFilter.base_reader.BaseReader`
interface. Also
notice that there are several static methods that need to be implemented. Inside these methods it may be
useful to use the hosts configuration file, which can be accessed using the function
:func:`~braviz.readAndFilter.config_file.get_host_config`.

Create directory for dynamic data
---------------------------------

Braviz will generate the database file and cache directory automatically. The only requirement is
to create a directory with a folder called *braviz_data* inside. Please make sure you have write permissions on
these two directories.

Create configuration files
--------------------------

To run braviz with using the new project you need to specify it in the *braviz.cfg* configuration file, which
is located in the *braviz.applications* folder. For example, to run Braviz using the *FooBar* data set, the configuration
file should look like this

.. code-block:: cfg

    [Braviz]
    project = foobar

Also remember to set the *Default_Variables* and *default_subject* fields appropriately (see :doc:`configuring`).

A new *_hosts* configuration file can be added to enter configuration parameters unique to each host.
For the sample projecct
*foobar* this file would need to be named *foobar_hosts.cfg*,
and located in the *braviz.applications* folder (see :doc:`configuring`)


Import tabular data
-------------------

The final step is importing some tabular data into the system. This can be done via the
import variables dialog (see :doc:`../graphical/from_excel`), or by using the :mod:`~braviz.applications.parse_spss_file`
command line applicetion.

Notice that only subjects with tabular data will appear in braviz.

