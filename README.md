# flask-cheatsheet

## Comparison
| Framework | Flask | Django |
| --- | --- | --- |
| Type of Framework | WSGI | Fullstack |
| Difficulties | Easy to use | Higher learning curve |
| Best part | lightweight | built-in authentication system |
| ORM | SQLAlchemy or (Flask-SQLAlchemy) is needed | build-in ORM (default is sqlite) |
| Frontend Template Engine | Jinja2 (derived from DTL) | Django Template Language (DTL) |

# Database
## Flask-SQLAlchemy
* [Flask-SQLAlchemy vs SQLAlchemy](https://stackoverflow.com/questions/14343740/flask-sqlalchemy-or-sqlalchemy)
  * Flask-SQLAlchemy creates an additional layer you might not really need
  * Flask-SQLAlchemy has much smaller community than SQLAlchemy itself
* It officially supports `mysql`, `sqlite`, `postgresql`, `oracle` (Django officially support `mariadb`)

# Ref
## flask
https://stackoverflow.com/questions/19261833/what-is-an-endpoint-in-flask


