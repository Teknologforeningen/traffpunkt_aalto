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
git clone git@github.com:Teknologforeningen/traffpunk_aalto.git
'''

Install virtualenv to the project.
'''bash
virtualenv --no-site-packages venv
'''

To activate virtualenv:
'''bash
source venv/bin/activate
'''

Install requirements:
'''bash
pip install -r requirements.txt
'''
