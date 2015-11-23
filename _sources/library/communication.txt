
.. module:: braviz.interaction.connection

Braviz Inter Application Communication
========================================

Braviz applications can share data because all of them work on the same database.
They may also send messages and listen to them. With this mechanism it is possible
to coordinate several applications and therefore enrich the analysis environment.

Messages are transmitted over TCP using the `0MQ <http://zeromq.org/>`_ protocol.
The current configuration has a message broker which retransmits messages to
all running applications. This broker usually runs on the menu application.

On one side, the broker acts as a publisher, and all applications subscribe to receive
messages from it. On the other side it acts as a sink receiving messages from all applications.
It has two addresses, one for publishing messages, to which applications should subscribe,
and a listening one, to which applications should send messages. These are the only two
well known addresses in the network.

The broker is implemented in :class:`~braviz.interaction.connection.MessageServer`,
and the client side is implement in :class:`~braviz.interaction.connection.MessageClient`.
Both of these classes generate PyQt-Signals when they receive a message, and therefore are easy
to connect to the rest of your application.

The protocol of the messages themselves is described in :doc:`communication_protocol`.


Message Broker
-----------------

.. autoclass:: MessageServer
    :members:


Message Client
----------------

.. autoclass:: MessageClient
    :members:

.. autoclass:: PassiveMessageClient
    :members:


.. autoclass:: GenericMessageClient
    :members:


.. module:: braviz.interaction.tornado_connection

Tornado Clients
^^^^^^^^^^^^^^^^^^^^^

This classes are meant to be used inside in tornado web servers to send and receive messages to the rest
of the system

.. autoclass:: MessageHandler

.. autoclass:: LongPollMessageHandler


