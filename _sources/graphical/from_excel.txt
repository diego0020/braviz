Import variables
====================

.. image:: images/from_excel.png
    :align: center
    :alt: Import from excel dialog

This dialog lets you add variables to the database from an excel file.

Expected format
----------------

The first column of the file should contain subject ids as found in the database. The first row should contain
variable names. All other cells should contain variable values. Notice that nominal variable values should be entered
as integer labels. Missing values should be empty cells or the string ``#NULL!``.

Procedure
----------

First click on *Select file* and find the excel file in the dialog. A preview of the data as understood by the program
will be shown. Verify that everything looks ok. If the table contains existing variables their values will be
overwritten in the database. You may instead choose to ignore this variables by checking the box labeled
*Omit existent*.

.. hint::
    The terminal will show the progress of the import process.
