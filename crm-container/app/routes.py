from flask import Blueprint, request, jsonify
from app.services import create_customer_profile, log_interaction, recommend_products

crm_blueprint = Blueprint("crm", __name__)


@crm_blueprint.route("/profile", methods=["POST"])
def create_profile():
    data = request.json
    customer = create_customer_profile(data)
    return (
        jsonify(
            {"id": customer.id, "message": "Customer profile created successfully."}
        ),
        201,
    )


@crm_blueprint.route("/interaction", methods=["POST"])
def add_interaction():
    data = request.json
    interaction = log_interaction(
        data["customer_id"], data["interaction_type"], data.get("notes", "")
    )
    return (
        jsonify({"id": interaction.id, "message": "Interaction logged successfully."}),
        201,
    )


@crm_blueprint.route("/recommendations/<int:customer_id>", methods=["GET"])
def get_recommendations(customer_id):
    products = recommend_products(customer_id)
    return jsonify({"customer_id": customer_id, "recommended_products": products})
