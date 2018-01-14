# juspay-django

Juspay is payment gateway and this is it's Python-Django implimentation.

## Setup

First clone the project, open your terminal and enter the command

    git clone https://github.com/dhavalsavalia/juspay-django.git

Now create a virtual environment

    virtualenv -p python3 juspay

Now activate the virtual environment

    source juspay/bin/activate

Now enter into the project folder

    cd juspay-django/

Now install the requirements

    pip install -r requirements.txt

Now go to payments -> views.py and enter your API KEY and your environment. If it's on production use 'production', if it's development/sandbox use 'sandbox' (There is a sandbox key already)

To get new creadentials for sandbox, visit https://sandbox.juspay.in

    juspayp3.api_key = 'your key here'
    juspayp3.environment = 'sandbox'

Now in terminal run the server and go to http://127.0.0.1:8910/ (port is 8910, if you want to change the port, also change "return_url" in views.py accordingly.)

	python manange.py runserver 8910