#!/usr/bin/env python3


import ipdb

def plus_two(num):
 
    return num + 2

def calculate_total(items):
    
    subtotal = sum(item['price'] for item in items)
    ipdb.set_trace()  # Breakpoint here
    tax = subtotal * 0.08
    return subtotal + tax

def process_data(data):
   
    ipdb.set_trace()
    cleaned = data.strip()
    ipdb.set_trace()
    normalized = cleaned.lower()
    ipdb.set_trace()
    return normalized

def format_name(first, last):
   
    full = f"{first} {last}"
    ipdb.set_trace()
    return full.title()

def complex_calculation():
  
    try:
        result = 10 / 0  # This will raise an error
    except Exception:
        ipdb.post_mortem()  # Debug after crash
    return result

def test_calculation():
    
    items = [{'price': 100}, {'price': 50}]
    result = calculate_total(items)
    ipdb.set_trace()
    assert result == 162  # Expected result with 8% tax


