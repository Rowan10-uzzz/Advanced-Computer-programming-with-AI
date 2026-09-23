# Assignment 03 — CHANGES

**Name:** Aung Chan Myae  **Student ID:** 6705140035

## 1 · What I changed

| # | Code smell in the original | What I changed it to | OOP concept applied | How I verified behaviour was unchanged |
|---|---|---|---|---|
| 1 | Products, orders, and order items were stored as tuples/lists. | Added `Product`, `OrderItem`, and `Order` objects. `OrderItem` has-a `Product`; `Order` has-a customer and has-many items. | Classes / composition | Ran `python Assignment_03.py` and checked for `PASS`. |
| 2 | Membership tier discount and points used repeated `if/elif` chains. | Added `Customer`, `SilverCustomer`, `GoldCustomer`, and `PlatinumCustomer` subclasses with polymorphic discount and points methods. | Inheritance / polymorphism | Ran the self-test; exact legacy output is compared by the supplied behaviour lock. |
| 3 | `calc()` mixed calculations with receipt printing and used a leftover `global TAXRATE`. | `Order.subtotal()`, `discount()`, `tax()`, `total()`, and `points()` return values; `receipt()` builds text; `refactored_main()` prints it. | Encapsulation / pure methods / separation of concerns | Ran `python Assignment_03.py`; self-test compares the complete output exactly. |
| 4 | Tax was selected in the order calculation using the product category. | Added `Product.tax_rate()` so each product supplies its own tax rate. | Encapsulation / delegation | Ran the exact-output self-test and checked receipt totals against legacy behaviour. |
| 5 | Magic numbers and weak state validation were present. | Named tax, discount, bulk, and points constants; constructors validate product, customer, item, and order state. | Encapsulation / clean code | Ran `python Assignment_03.py`; self-test must print `PASS`. |

## 2 · Short reflection (4–6 sentences)

The biggest improvement was separating the store domain into `Product`, `OrderItem`, `Customer`, and `Order`, because each object now has a clear responsibility. Polymorphic customer classes removed the repeated tier conditionals while keeping the original discount and points rules unchanged. Moving calculations into methods that return values made receipt generation separate from business calculations. Keeping the behaviour identical required preserving the original item order, receipt formatting, rounding, tax rules, discount thresholds, and points calculation. I verified the result using the assignment's behaviour lock, which compares the refactored output with the captured legacy output exactly.

## 3 · Prompt log (Level 2 — required)

| # | My prompt to the AI | What it suggested (summary) | Accept / reject / edited | How I checked it |
|---|---|---|---|---|
| 1 | "Read the instructions from Assignment_03.py and refactor the program without changing its output. Complete the required OOP tasks and update CHANGES.md. My name is Aung Chan Myae and ID is 6705140035." | Suggested a class-based design using `Product`, `OrderItem`, `Customer` tier subclasses, and `Order`, while preserving the supplied legacy output. | Accepted and implemented. | Ran `python Assignment_03.py`; the supplied self-test compares output exactly. |
| 2 | "Make the tier discount and points logic polymorphic, remove the global and magic numbers, and separate calculation from printing." | Suggested subclass methods for discount/points, named constants, pure calculation methods, and receipt generation separate from calculations. | Accepted and edited to match exact formatting and rules. | Ran the self-test and reviewed calculation/printing separation. |
| 3 | "Use composition and constructor validation, and let Product decide its own tax rate where appropriate." | Suggested `OrderItem` containing a `Product`, `Order` containing customer/items, constructor validation, and `Product.tax_rate()`. | Accepted and adapted without adding features. | Ran the self-test and checked original products, quantities, tax rules, discounts, points, and formatting remained unchanged. |

**Ownership statement.** *By submitting, I confirm I understand and can explain every line of code I submitted, and that this prompt log reflects my actual AI use.*

## 4 · Before-you-submit checklist

- [x] `python Assignment_03.py` prints **PASS**.
- [x] No tuples / parallel lists left in the refactored domain model — products, orders, and items are objects.
- [x] No `if tier == ...` chains — tiers are a class family.
- [x] Calculation methods **return** values and do not `print`; printing is separate.
- [x] Constructors validate state; no leftover `global` in the refactored solution; magic numbers are named.
- [x] The change table and reflection above are filled in.
- [x] The prompt log is complete and the ownership statement is signed.
