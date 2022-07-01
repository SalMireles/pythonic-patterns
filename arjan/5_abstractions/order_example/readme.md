# Project Structure

📦 before
 ┣ 📂 pos
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜authorization.py
 ┃ ┣ 📜data.py
 ┃ ┣ 📜order.py
 ┃ ┗ 📜payment.py
 ┗ 📜main.py

 #### Overview
 ##### Abstracting The Authorizer 
 functions
- payment.py `PaymentProcessor` handles the processing of the payment + needs to
know about the type of authorizer from authorization.py
- Can pass in a function instead &rarr; strategy pattern (provides a behavior). 
Note: must define type.
- Hint: When you see if else statements you can use the  **Strategy Pattern**

##### Abstracting The Order Class
- Use protocols and again the strategy pattern to provide the `Order` instance
to the payment processor.

##### Abstracting The Payment Processor
- The bridge pattern allows you to have independent variation of two types that
still rely on each other.
- Check where you are patching things up. If it's in one single place then you
probably have a good design.