from app.models import db, CustomerProfile, CustomerInteraction
from datetime import datetime


def create_customer_profile(data):
    customer = CustomerProfile(
        name=data["name"],
        email=data["email"],
        phone=data.get("phone"),
        total_spent=data.get("total_spent", 0.0),
        last_interaction=datetime.utcnow(),
    )
    db.session.add(customer)
    db.session.commit()
    return customer


def log_interaction(customer_id, interaction_type, notes=""):
    interaction = CustomerInteraction(
        customer_id=customer_id,
        interaction_type=interaction_type,
        interaction_date=datetime.utcnow(),
        notes=notes,
    )
    db.session.add(interaction)
    db.session.commit()
    return interaction


def recommend_products(customer_id):
    # Placeholder logic for product recommendations
    return ["Credit Card", "Savings Account", "Business Loan"]
