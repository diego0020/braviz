
************************
Reading geometric data
************************

.. currentmodule:: braviz.readAndFilter.base_reader

In braviz scripts and applications should not have to deal with individual files or directory structures.
All access to this data should be done through to the functions and classes in the :mod:`braviz.readAndFilter` module.
The objective behind this is to isolate the applications code from the underlying file system. In this way it is
easy to adapt to different projects with different data structures.

Project readers should be derived from :class:`.BaseReader` , which describes the behaviour that they should provide.



BaseReader
===========

.. autoclass:: BaseReader

Constructors
------------

    .. automethod:: BaseReader.__init__(self,max_cache=100,**kwargs)
    .. automethod:: BaseReader.get_auto_reader(**kw_args)

The get method
--------------

    .. automethod:: BaseReader.get(self,data, subj_id=None, *args, **kwargs)

Coordinate systems
------------------

    .. automethod:: BaseReader.move_img_to_subject(self,img,source_space,subj,interpolate=False)
    .. automethod:: BaseReader.move_img_from_subject(self,img,target_space,subj,interpolate=False)
    .. automethod:: BaseReader.transform_points_to_space(self, point_set, space, subj, inverse=False)

Cache
-----

    .. automethod:: BaseReader.clear_mem_cache(self)
    .. automethod:: BaseReader.save_into_cache(self, key, data)
    .. automethod:: BaseReader.load_from_cache(self, key)
    .. automethod:: BaseReader.clear_cache_dir(self,last_word=False)

File System
-----------

    .. automethod:: BaseReader.get_data_root(self)
    .. automethod:: BaseReader.get_dyn_data_root(self)
    .. automethod:: BaseReader.get_auto_data_root()
    .. automethod:: BaseReader.get_auto_dyn_data_root()
    .. automethod:: BaseReader.initialize_dynamic_data_dir(dir_name=None)
    .. automethod:: BaseReader.clear_dynamic_data_dir(dir_name)

Custom Readers
==============

Custom readers should be subclasses of :class:`BaseReader`. They should be included in a module with the same name as
the project (in lowercase) and named after the project followed by ``"Reader"``. Look at the examples below



    .. autoclass:: braviz.readAndFilter.kmc40.Kmc40Reader
    .. autoclass:: braviz.readAndFilter.kmc400.Kmc400Reader



