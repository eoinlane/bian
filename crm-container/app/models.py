from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class CustomerProfile(db.Model):
    __tablename__ = "customer_profiles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    total_spent = db.Column(db.Float, default=0.0)
    last_interaction = db.Column(db.DateTime)


class CustomerInteraction(db.Model):
    __tablename__ = "customer_interactions"
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(
        db.Integer, db.ForeignKey("customer_profiles.id"), nullable=False
    )
    interaction_type = db.Column(db.String(50))
    interaction_date = db.Column(db.DateTime)
    notes = db.Column(db.Text)
