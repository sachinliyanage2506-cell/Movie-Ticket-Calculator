# Movie-Ticket-Calculator

A command-line Python program for purchasing movie tickets. It supports multiple titles per transaction, applies group and membership discounts automatically, prints a full receipt, and generates a sales summary with basic analytics.

Features
- Multi-Title Purchases - buy tickets for any number of movies in a single session, adding one title at a time until you type done.
- Live Running Subtotal - see your pre-discount update after every item added
- Input Validation - rejects unknown titles and invalid or non-positive quantities, prompting the user to try again rather than crashing
- Automatic Group Discount - any line with 4 or more tickets automatically receives 10% off
- Membership Discount - an optional extra 5% off the entire order for members, applied after group discounts.
Sales Summary by Movie - a nearly formatted table of total tickets sold and revenue per title, calculated from actual discounted prices so it always matches the receipt
Analytics - top-selling movie by ticket count, titles ranked by revenue (highest to lowest), and average ticket per purchase line
