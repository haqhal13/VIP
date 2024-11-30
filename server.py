from flask import Flask, jsonify, request
import stripe
import os

# Initialize Flask app
app = Flask(__name__)

# Set your Stripe secret key
stripe.api_key = "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"

# Stripe route for creating payment intent
@app.route('/create-payment-intent', methods=['POST'])
def create_payment_intent():
    try:
        # Get the request data
        data = request.json

        # Create a payment intent with the specified amount and currency
        intent = stripe.PaymentIntent.create(
            amount=data['amount'],  # Amount in cents (e.g., $10.00 = 1000)
            currency=data['currency'],  # e.g., 'usd'
            payment_method_types=['card'],  # Supported payment methods
        )

        # Respond with the client secret for frontend use
        return jsonify({
            'clientSecret': intent['client_secret']
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Home route to check if the server is running
@app.route('/')
def home():
    return "Stripe backend is running!"

if __name__ == '__main__':
    # Use Render's dynamically assigned port, defaulting to 10000 for local testing
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
