import os
import sys

db_user = os.environ.get('EMAIL_HOST_USER')
db_pwd = os.environ.get('EMAIL_HOST_PASSWORD')

print(db_user)
print(db_pwd)
