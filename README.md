# Movie-Ticket-Calculator

How to Run:
- Run the script in any Python editor or IDE. I used IDLE (Python 3.14).

Overview
A command-line Python program for purchasing movie tickets. It supports multiple titles per transaction, applies group and membership discounts automatically, prints a full receipt, and generates a sales summary with basic analytics.

Features
- Multi-Title Purchases - buy tickets for any number of movies in a single session, adding one title at a time until you type done.
- Live Running Subtotal - see your pre-discount update after every item added
- Input Validation - rejects unknown titles and invalid or non-positive quantities, prompting the user to try again rather than crashing
- Automatic Group Discount - any line with 4 or more tickets automatically receives 10% off
- Membership Discount - an optional extra 5% off the entire order for members, applied after group discounts.
- Sales Summary by Movie - a nearly formatted table of total tickets sold and revenue per title, calculated from actual discounted prices so it always matches the receipt.

Tech Stack
- Python


Potential improvements on the project
- To make it more easier for end users, make it like a GUI so to hide the coding components which can seem confusing for users with limited python knowledge.
- Could I add a feature that allows the user to quickly find the movie they want to watch without typing the exact name?

Authorship: Sachin Liyanage


