from webapp import db,dm
from .models.transaction import Transaction

# creates the table schema's if they do not already exist.
db.create_all()

#populate the database if the data isn't there.
if not Transaction.query.first():
    dm.load_data()
    dm.data.to_sql( name=Transaction.__tablename__, 
                    con=db.engine, 
                    if_exists = 'append', 
                    index=False
                    )

db.session.commit()