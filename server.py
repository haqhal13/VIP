from flask import Flask, jsonify, request
import stripe

# Set up Stripe secret key
stripe.api_key = "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"

# Initialize Flask app
app = Flask(__name__)

# Route to create a checkout session
@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        # Get the data from the request
        data = request.json
        price = data.get("price", 2000)  # Default price is $20.00 in cents.

        # Create a checkout session
        session = stripe.checkout.Session.create(
            payment_method_types=['card', 'apple_pay', 'google_pay'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'VIP Subscription',
                    },
                    'unit_amount': price,  # Price is passed in cents
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url="https://t.me/BADDIESFACTORY_BOT?start=success",
            cancel_url="https://t.me/BADDIESFACTORY_BOT?start=cancel",
        )
        return jsonify({'url': session.url})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Health check endpoint (optional but helpful)
@app.route('/')
def index():
    return "Server is running!"

# Run the server (for local testing)
if __name__ == '__main__':
    app.run(port=4242)