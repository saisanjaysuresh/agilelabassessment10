def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# NEW FUNCTION ADDED FOR PUSH 2
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("\n--- Temperature Converter ---")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius") # Updated menu option text
    
    choice = input("Select an option (1-2): ")
    
    if choice == "1":
        c = float(input("Enter temperature in Celsius: "))
        f = celsius_to_fahrenheit(c)
        print(f"{c}°C is equal to {f}°F")
    elif choice == "2":
        # ACTIVATED FOR PUSH 2
        f = float(input("Enter temperature in Fahrenheit: "))
        c = fahrenheit_to_celsius(f)
        print(f"{f}°F is equal to {c:.2f}°C")
    else:
        print("Invalid choice.")

if __name__ == '__main__':
    main()
