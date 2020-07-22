from app import app, api
from resources.routes import initialize_routes
from database.db import initialize_db

initialize_db(app)
initialize_routes(api)

app.run()
