from app import celsius_to_fahrenheit, fahrenheit_to_celsius

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(100) == 212.0
    assert celsius_to_fahrenheit(0) == 32.0

# NEW TEST ADDED FOR PUSH 2
def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(212) == 100.0
    assert fahrenheit_to_celsius(32) == 0.0
    print("Push 2 Tests Passed Successfully!")

if __name__ == '__main__':
    test_celsius_to_fahrenheit()
    test_fahrenheit_to_celsius()
# Push 2 Update