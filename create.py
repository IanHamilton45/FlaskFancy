from application import db
from application.models import Users, Posts

db.create_all()




#TO RUN: docker exec app_container python3 create.py
