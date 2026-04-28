import pytest
from app.discounts import apply_discount


def test_apply_discount_success():
    assert apply_discount(100, 10) == 90


def test_apply_discount_invalid_price():
    with pytest.raises(ValueError):
        apply_discount(-10, 10)


def test_apply_discount_edge_case_100_percent():
    assert apply_discount(100, 100) == 0
