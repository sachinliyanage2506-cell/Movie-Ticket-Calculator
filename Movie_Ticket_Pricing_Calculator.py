"""
Movie Ticket Purchase Program
------------------------------
- Take ticket orders (title + quantity)
- Print a receipt with group discount (10% off if qty >= 4 on a line)
  and an optional member discount (5% off the whole order)
- Show a sales summary and simple analytics, all based on the
  ACTUAL (discounted) revenue that was charged
"""

movies = {
    "Dune": 12.5,
    "Barbie": 11.0,
    "Oppenheimer": 13.0,
    "Spirited Away": 10.0
}

purchases = []          # list of (title, qty, price_each)
running_subtotal = 0.0  # pre-discount running total, shown during input


# -------------------------
# Helper functions (Part D)
# -------------------------
def apply_group_discount(qty, price_each):
    """
    Compute the line total and apply a 10% discount if qty >= 4.
    Returns:
        discounted_line_total (float), discount_applied (bool)
    """
    line_total = qty * price_each
    if qty >= 4:
        return line_total * 0.90, True  # 10% off for groups
    return line_total, False


def apply_member_discount(total, is_member):
    """
    Apply an extra 5% discount on the grand total if the customer is a member.
    """
    return total * 0.95 if is_member else total


# -------------------------
# Input loop
# -------------------------
while True:
    title = input("Enter movie title (or 'done' to finish): ").strip()
    if title.lower() == "done":
        break

    if title not in movies:
        print("Title not found. Available titles:", ", ".join(movies.keys()))
        continue

    qty_str = input(f"Quantity for '{title}': ").strip()
    try:
        qty = int(qty_str)
        if qty <= 0:
            print("Please enter a positive integer for quantity.")
            continue
    except ValueError:
        print("Please enter a valid integer for quantity.")
        continue

    price_each = movies[title]
    purchases.append((title, qty, price_each))

    running_subtotal += qty * price_each
    print(f"Added: {qty} × {title} @ ${price_each:.2f}")
    print(f"Running subtotal (before discounts): ${running_subtotal:.2f}\n")


# -------------------------
# Receipt with discounts
# -------------------------
print("\n--- Receipt ---")

grand_total_before_member = 0.0
final_total = 0.0
is_member = False

if not purchases:
    print("No items purchased.")
    print("Grand Total: $0.00")
else:
    for title, qty, price_each in purchases:
        discounted_line_total, got_group_discount = apply_group_discount(qty, price_each)

        if got_group_discount:
            original = qty * price_each
            print(
                f"{qty} × {title} @ ${price_each:.2f} "
                f"= ${original:.2f}  →  -10% group = ${discounted_line_total:.2f}"
            )
        else:
            print(f"{qty} × {title} @ ${price_each:.2f} = ${discounted_line_total:.2f}")

        grand_total_before_member += discounted_line_total

    print(f"\nTotal (before member discount): ${grand_total_before_member:.2f}")

    # Ask for member code, with validation
    while True:
        resp = input("Does the customer have a member code? (y/n): ").strip().lower()
        if resp in ("y", "yes"):
            is_member = True
            break
        elif resp in ("n", "no"):
            is_member = False
            break
        else:
            print("Please enter y or n.")

    # This now runs exactly once, after a valid y/n was given
    final_total = apply_member_discount(grand_total_before_member, is_member)

    if is_member:
        savings = grand_total_before_member - final_total
        print(f"Member discount applied (-5%): -${savings:.2f}")

    print(f"Grand Total: ${final_total:.2f}")


# -------------------------
# Sales summary (Part C) — built from ACTUAL discounted revenue,
# so it always matches the receipt above
# -------------------------
tickets_by_movie = {}
revenue_by_movie = {}

for title, qty, price_each in purchases:
    discounted_line_total, _ = apply_group_discount(qty, price_each)
    tickets_by_movie[title] = tickets_by_movie.get(title, 0) + qty
    revenue_by_movie[title] = revenue_by_movie.get(title, 0.0) + discounted_line_total

print("\n--- Sales Summary (by movie) ---")
print(f"{'Title':30} | {'Tickets':7} | {'Revenue':>10}")
print("-" * 54)
for title in sorted(tickets_by_movie):
    tix = tickets_by_movie[title]
    rev = revenue_by_movie[title]
    print(f"{title:30} | {tix:7d} | ${rev:10.2f}")


# -------------------------
# Analytics (Part E)
# -------------------------
print("\n--- Analytics ---")

# Top-selling movie by tickets
if tickets_by_movie:
    top_title = None
    top_qty = -1
    for title, qty in tickets_by_movie.items():
        if qty > top_qty:
            top_title, top_qty = title, qty
    print(f"Top seller by tickets: {top_title} ({top_qty} tickets)")
else:
    print("Top seller by tickets: N/A (no sales)")

# Titles sorted by revenue (descending)
if revenue_by_movie:
    sorted_by_rev = sorted(revenue_by_movie.items(), key=lambda kv: kv[1], reverse=True)
    print("Titles sorted by revenue (desc):")
    for rank, (title, rev) in enumerate(sorted_by_rev, start=1):
        print(f"  {rank}. {title}: ${rev:.2f}")
else:
    print("Titles sorted by revenue (desc): N/A (no sales)")

# Average tickets per purchase line
if purchases:
    total_tickets = sum(qty for _, qty, _ in purchases)
    avg_tickets_per_purchase = total_tickets / len(purchases)
    print(f"Average tickets per purchase line: {avg_tickets_per_purchase:.2f}")
else:
    print("Average tickets per purchase line: N/A (no purchases)")
