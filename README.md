Install
=======

Install setuptools.
```bash
sudo apt-get install python-setuptools
```

Install virtualenv, to keep the environment isolated.
```bash
sudo easy_install virtualenv
```

Clone the repository.
```bash
git clone git@github.com:Teknologforeningen/traffpunk_aalto.git && cd traffpunk_aalto/
```

Install virtualenv to the project.
```bash
virtualenv --no-site-packages venv
```

To activate virtualenv:
```bash
source venv/bin/activate
```

PIL and Python requirements:
https://github.com/python-imaging/Pillow
```bash
# Ubuntu 12.04
$ sudo apt-get install python-dev python-setuptools libpq-dev
$ sudo apt-get install libtiff4-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms1-dev libwebp-dev
```

Install requirements:
```bash
pip install -r requirements.txt
```

Libraries
==========
- http://bootswatch.com/cosmo/
