## run with:
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
And in another terminal
```
cd website
npm install
npm start
```