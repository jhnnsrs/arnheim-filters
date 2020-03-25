Filters
=======

Filters is a django-driven Arnheim app providing simple image filters like edge-enhancing for the platform.
Each standalone filter provides a pure function that takes only a Xarray as input and adjust the data and metadata accordingly.


Detailed documentation is in the "docs" directory.

Quick start Arnheim
------------------

1. Add "filters" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'filters',
    ]


3. Run ``python manage.py migrate`` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/polls/ to participate in the poll.


