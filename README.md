# Django Ecommerce
This project is a complete E-commerce web application built using the Django framework. It includes features like user registration, product management, shopping cart, checkout, payment gateway integration with Razorpay, and Google sign-in.

## Features
### User Registration and Authentication
- Users can sign up and log in to their accounts.
- Google sign-in allows users to log in using their Google accounts.

### Product Management
- Admin users can add, edit, and delete products.

### Shopping Cart
- Users can add products to their shopping cart and remove them.
- Users can view their shopping cart and update the quantity of products.

### Checkout
- Users can view their order summary and enter their shipping information.
- Users can select the payment method and proceed to the payment gateway.

### Payment Gateway Integration with Razorpay
- The application integrates with Razorpay to process payments.

### Order Management
- Admin users can view all orders and change their status.

## Installation
1. Clone the repository: `https://github.com/arizkyrahman/ecommerce-django.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Create a `.env` file in the root directory: 
`SECRET_KEY=<your_secret_key>
RAZORPAY_KEY_ID=<your_razorpay_key_id>
RAZORPAY_KEY_SECRET=<your_razorpay_key_secret>`
4. Run the database migrations: `python manage.py migrate`
5. Create a superuser account: `python manage.py createsuperuser`
6. Run the development server: `python manage.py runserver`
7. Open your web browser and navigate to `http://localhost:8000`

## Usage
1. To use the application, you will need to create a user account or sign in with your Google account.
2. Browse the products and add the desired products to your shopping cart.
3. View your shopping cart and proceed to checkout.
4. Enter your shipping information and select the payment method.
5. Complete the payment using the Razorpay payment gateway.
6. View your order summary and check your email for the order confirmation.

## Contributing
Contributions to this project are welcome. To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Write your code and tests.
4. Submit a pull request.
