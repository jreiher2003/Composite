from app import db
from app.models import AsciiArt

db.drop_all()
print "just dropped table"
db.create_all()


one = AsciiArt(title = "Test Title", art = "This is test art")
one.lat =  42.363633
one.lon = -87.844794
db.session.add(one)
db.session.commit()

print "Successful import"