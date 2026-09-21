
### `SPEC.md`

```md
# Specification

## Feature: Order discount

Implement:

calculate_total(price, quantity, customer_type)

## Requirements

REQ-001:
The total before discount is:

price * quantity

REQ-002:
Regular customers receive no discount.

REQ-003:
Premium customers receive a 10% discount.

REQ-004:
VIP customers receive a 20% discount.

REQ-005:
Quantity must be at least 1.

If quantity is less than 1, raise ValueError.

REQ-006:
Price must be greater than 0.

If price is 0 or negative, raise ValueError.

## Acceptance criteria

All tests in `test_app.py` must pass.

Do not add unrelated functionality.