import pytest
from unittest.mock import patch
from main import calculate_bmi

def test_underweight():
    with patch('builtins.input', side_effect=[101.5, 5.3]):  
        bmi, category = calculate_bmi(float(input()), float(input()))  
    assert bmi == 18.4
    assert category == "Underweight"

def test_normal_weight():
    with patch('builtins.input', side_effect=[102, 5.3]):  
        bmi, category = calculate_bmi(float(input()), float(input()))  
    assert bmi == 18.5
    assert category == "Normal Weight"

def test_overweight():
    with patch('builtins.input', side_effect=[151.5, 5.5]): 
        bmi, category = calculate_bmi(float(input()), float(input()))  
    assert bmi == 25
    assert category == "Overweight"

def test_obese():
    with patch('builtins.input', side_effect=[182, 5.5]):  
        bmi, category = calculate_bmi(float(input()), float(input()))  
    assert bmi == 30
    assert category == "Obese"
