python get-pip.py
pip -V
pip install -r requirements.txt
python create_DB.py
set FLASK_APP=api
set FLASK_DEBUG=1
set FLASK_ENV=development
flask create_admin
print admin created!