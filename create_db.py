# from website import db, create_app
# app = create_app()
# ctx = app.app_context()
# ctx.push()
# db.create_all()
# quit()

# create_db.py

from website import db, create_app

app = create_app()
ctx = app.app_context()
ctx.push()

# Drop all tables (DANGER: removes all data)
db.drop_all()

# Create all tables based on current models
db.create_all()

print("Database reset and tables created.")
quit()
