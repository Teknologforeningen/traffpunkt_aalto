Install
=======

Install setuptools.
'''bash
sudo apt-get install python-setuptools
'''

Install virtualenv, to keep the environment isolated.
'''bash
sudo easy_install virtualenv
'''

Clone the repository.
'''bash
git clone git@github.com:Teknologforeningen/traffpunk_aalto.git && cd traffpunk_aalto/
'''

Install virtualenv to the project.
'''bash
virtualenv --no-site-packages venv
'''

To activate virtualenv:
'''bash
source venv/bin/activate
'''

PIL requirements:
https://github.com/python-imaging/Pillow
'''bash
# Ubuntu 12.04
$ sudo apt-get install python-dev python-setuptools
$ sudo apt-get install libtiff4-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms1-dev libwebp-dev
'''

Install requirements:
'''bash
pip install -r requirements.txt
'''

Heroku
======

Pushing heroku-branch to heroku:
```bash
$ git push -f heroku heroku:master
```

Check if database is configured and ready:
```bash
$ heroku config | grep DATABASE_URL
```

If the DATABASE_URL variable is set the db is ready and should work with the default heroku settings.

If the DATABASE_URL is not set you may need to add a db and promote it.

Check if there is a database available already:
```bash
$ heroku addons | grep POSTGRES
```
Add a database:
```bash
$ heroku addons:add heroku-postgresql:dev
```
Promote the database so the settings pick it up:
```bash
$ heroku config | grep HEROKU_POSTGRESQL
$ heroku pg:promote <output of previous command>
```

More information here: https://devcenter.heroku.com/articles/heroku-postgresql#provisioning-the-add-on

Libraries
==========
- http://bootswatch.com/cosmo/
