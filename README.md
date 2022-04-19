
# 📰 Blog as a Service

An installable django blog application.


![dynamo_blogger](https://user-images.githubusercontent.com/55067204/164105851-bc2cdd00-e208-43bc-a240-643443768ee1.png)


Requirements
---------------

* Python (3.6, 3.7, 3.8, 3.9, 3.10)
* Django (2.2, 3.0, 3.1, 3.2, 4.0)


Quick Start
-----------

1. Install using `pip`:
```
    pip install dynamo_blogger
```

2. Add "dynamo_blogger" to your INSTALLED_APPS setting:
```
    INSTALLED_APPS = [
        ...
        'dynamo_blogger',
    ]
```

3. Include the dynamo_blogger URLs in your project urls.py:
```
    path('blog/', include('dynamo_blogger.urls')),
```

4. Run ``python manage.py migrate`` to create the `dynamo_blogger` models.

5. Start the development server and visit http://127.0.0.1:8000/blog/


Documentation & Support
--------------------------

Full documentation for the project is available at [docs](https://dynamo-blogger.pandaware.tech/).

You may also want to follow the author on [twitter](https://twitter.com/israelabraham_).


License
---------
Disclaimer: Everything you see here is open and free to use as long as you comply with the [license](https://github.com/Pandaware-Tech/Dynamo-Blogger/blob/main/LICENSE). There are no hidden charges. We promise to do our best to fix bugs and improve the code.
