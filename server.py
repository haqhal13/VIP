import stripe
from flask import Flask, request, jsonify

# Set up Flask
app = Flask(__name__)

# Your Stripe secret key (get this from your Stripe dashboard)
stripe.api_key = "sk_test_YourSecretKey"

# Create a route to generate a Stripe payment link dynamically
@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        # Create a Stripe Checkout session
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],  # Accept credit/debit cards
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',  # Change to your currency (e.g., gbp for pounds)
                        'product_data': {
                            'name': '1-Month Subscription',
                        },
                        'unit_amount': 2000,  # Amount in cents (2000 = $20.00)
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='https://your-website.com/success',  # Redirect here after payment
            cancel_url='https://your-website.com/cancel',   # Redirect here if payment is cancelled
        )
        return jsonify({'url': session.url})  # Return the Stripe Checkout link
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Run the server
if __name__ == '__main__':
    app.run(port=4242)