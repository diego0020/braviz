.. module:: braviz.visualization.d3_visualizations

D3 based visualizations
=========================

The Java Script library `D3 <d3.org>`_ allows to create rich interactive graphics. It is of course targeted at
web visualizations, and is meant to run on a web browser. In order to integrate this with the rest of braviz, which
is written in python, we will use the `twister <twisterweb.org>`_ web server to send appropriate html to the browser,
and to receive messages (requests). We are still missing a mechanism to send further messages to the browser once the
page is loaded. This could be done by polling at a particular address and keeping track of message numbers

Parallel Coordinates
----------------------

.. image:: images/parallel_coords.png
    :alt: Parallel coordinates example
    :align: center
    :width: 90%

.. autoclass:: ParallelCoordinatesHandler


.. autoclass:: IndexHandler