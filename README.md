
1. $ python manage.py -c prod.cfg db init -> initialize database
2. $ python manage.py -c prod.cfg db migrate -> create migrations
3. $ python manage.py -c prod.cfg db upgrade -> apply migration
4. $ python manage.py -c prod.cfg db --help
5. $ python manage.py -c prod.cfg runserver