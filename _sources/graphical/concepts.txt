Braviz Concepts
==================

This page definitions of the main braviz concepts. References to these terms inside Braviz and elsewhere in the
documentation should always be interpreted as indicated here.

Project
---------

Inside Braviz a project is a collection of brain data on a group of subjects, usually captured as part of a
study. All subjects of the project should ideally contain the same data. The data collected includes neuro-images
as well as clinical, demographic and neuro-psichological data encoded in tables.

Subjects
----------

Inside Braviz each participant of the study is called a subject. It has associated a group of neuro-images as well
as a row in each data table. Usually subjects are identified with a numerical id.

Variables
----------

A variable refers to a property which can be defined for each subject. In the tables mentioned above, each variable
would correspond to a column. For the moment Braviz can handle two types of variables:

    -   **Real Variables**: The values of the variable for each subject are real numbers. Examples of these are
        age, height, volume of skull or the time taken to answer a test.

    -   **Nominal Variables**: The values of the variable for each subject are a label that assigns him to one
        category. Some examples are: gender (male or female), categorized test results
        (average, below-average or above-average) or handedness (left-handed or right-handed).

For more information about manipulating variables in Braviz see :doc:`variables`.

Sub-samples
-------------

A sub-sample is a subset from the subjects in the project. They can be used to limit tests to a
group of interest, or to reduce the size of the search space.

For information on creating samples in braviz see :doc:`samples`.

Scenarios
----------

Braviz applications allows you to interactively explore the dataset and produce personalized visualizations. This
exploration can sometimes take a long time, and it should not have to be repeated. Scenarios are the way in which you
can save the state of the application (including the state of the 3d views, active variables and current subject), in
such a way that you can retake the analysis later or show it to a colleague.

Braviz Data Base
-----------------

Braviz has an internal database in which it saves variable values, variable meta data, scenarios, subsamples, and other.
In practice everything but neuro-images is saved inside the database. This database is shared by all applications
which provides them a way to collaborate. All modifications to the database are immediately saved to the disk, therefore
you don't need to worry about loosing power or not closing braviz in the right way.

Variables can be imported into the database  :doc:`from excel files <from_excel>` and
:doc:`exported to csv files <export_csv>`. In this way you can use Braviz together with your favorite statistical
program.

Coordinate system
------------------

Neuro-image data are samples from a participant's brain, and therefore it should be possible to match the data in the
image with the physical entity. However, due to several factors in the capture process, images from two subjects will
hardly be in the same position. Also brains from different participants differ in size and shape. To make it easier
to compare different participants it is sometimes useful to transform his brain into a common coordinate system. Using
a common coordinate system also provides you with a way for talking about positions in the brain. However there is a
cost associated to applying these transforms as it involves resampling the image, which in turn involves interpolation,
where there is always the risk of loosing important data. Typically in Braviz we will have the following coordinate
systems:

    -   **World** : The coordinate system from the anatomical MRI image as captured by the machine. One milimeter of
        an image in this space will match with one milimeter in the physical world.
    -   **Talairach** : Images are rotated and scaled in such a way that they best fit the
        `Talairach coordinate systems <http://en.wikipedia.org/wiki/Talairach_coordinates>`_. Because the image is
        scaled, it is no longer possible to relate measures taken here to the physical world. However because all
        brains are normalized in size, it could be useful to compare measures taken in this space.
    -   **Dartel** : Images are deformed in such a way that they match a template. This template represents the brain
        of an *average* subject in the study. Currently the templates and transforms are calculated using
        `SPM Dartel <http://www.fil.ion.ucl.ac.uk/spm/doc/>`_ . Brains warped in this way will look very similar to
        one another, but there will be little correspondance with the physical world. This kind of transforms are the
        basis of second level fmri analyses or VBM.
    -   **Other** : Diffusion images are acquired in a different space usually called *diff*, calculations involving
        tensors and gradient data are more precise if done in this native space. fMRI sequences are also captured
        in its own space. The SPM pipeline register these images to the anatomical images and afterwards the whole set
        to a template space, typically MNI. Statistical maps are calculated in this space. Notice this final coordinate
        system is not necessarily equal to the dartel system.

