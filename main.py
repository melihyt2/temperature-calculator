def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def choose_language():
    print("Choose your language:")
    print("1. English")
    print("2. Turkish")
    print("3. Spanish")
    print("4. French")
    print("5. German")
    choice = input("Select your language (1/2/3/4/5): ")
    if choice == '1':
        return 'English'
    elif choice == '2':
        return 'Turkish'
    elif choice == '3':
        return 'Spanish'
    elif choice == '4':
        return 'French'
    elif choice == '5':
        return 'German'
    else:
        print("Invalid choice")
        return choose_language()

def main():
    language = choose_language()
    if language == 'English':
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. Fahrenheit to Kelvin")
        print("6. Kelvin to Fahrenheit")
        choice = input("Choose conversion (1/2/3/4/5/6): ")

        if choice in ['1', '2', '3', '4', '5', '6']:
            if choice == '1':
                celsius = float(input("Enter temperature in Celsius: "))
                print("Temperature converted to Fahrenheit:", celsius_to_fahrenheit(celsius))
            elif choice == '2':
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                print("Temperature converted to Celsius:", fahrenheit_to_celsius(fahrenheit))
            elif choice == '3':
                celsius = float(input("Enter temperature in Celsius: "))
                print("Temperature converted to Kelvin:", celsius_to_kelvin(celsius))
            elif choice == '4':
                kelvin = float(input("Enter temperature in Kelvin: "))
                print("Temperature converted to Celsius:", kelvin_to_celsius(kelvin))
            elif choice == '5':
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                print("Temperature converted to Kelvin:", fahrenheit_to_kelvin(fahrenheit))
            elif choice == '6':
                kelvin = float(input("Enter temperature in Kelvin: "))
                print("Temperature converted to Fahrenheit:", kelvin_to_fahrenheit(kelvin))
        else:
            print("Invalid choice")
    elif language == 'Turkish':
        print("1. Celsius'tan Fahrenheit'a")
        print("2. Fahrenheit'tan Celsius'a")
        print("3. Celsius'tan Kelvin'e")
        print("4. Kelvin'den Celsius'a")
        print("5. Fahrenheit'tan Kelvin'e")
        print("6. Kelvin'den Fahrenheit'a")
        choice = input("Dönüşümü seçin (1/2/3/4/5/6): ")

        if choice in ['1', '2', '3', '4', '5', '6']:
            if choice == '1':
                celsius = float(input("Celsius cinsinden sıcaklık girin: "))
                print("Sıcaklık Fahrenheit cinsine dönüştürüldü:", celsius_to_fahrenheit(celsius))
            elif choice == '2':
                fahrenheit = float(input("Fahrenheit cinsinden sıcaklık girin: "))
                print("Sıcaklık Celsius cinsine dönüştürüldü:", fahrenheit_to_celsius(fahrenheit))
            elif choice == '3':
                celsius = float(input("Celsius cinsinden sıcaklık girin: "))
                print("Sıcaklık Kelvin cinsine dönüştürüldü:", celsius_to_kelvin(celsius))
            elif choice == '4':
                kelvin = float(input("Kelvin cinsinden sıcaklık girin: "))
                print("Sıcaklık Celsius cinsine dönüştürüldü:", kelvin_to_celsius(kelvin))
            elif choice == '5':
                fahrenheit = float(input("Fahrenheit cinsinden sıcaklık girin: "))
                print("Sıcaklık Kelvin cinsine dönüştürüldü:", fahrenheit_to_kelvin(fahrenheit))
            elif choice == '6':
                kelvin = float(input("Kelvin cinsinden sıcaklık girin: "))
                print("Sıcaklık Fahrenheit cinsine dönüştürüldü:", kelvin_to_fahrenheit(kelvin))
        else:
            print("Geçersiz seçim")
    elif language == 'Spanish':
        print("1. Celsius a Fahrenheit")
        print("2. Fahrenheit a Celsius")
        print("3. Celsius a Kelvin")
        print("4. Kelvin a Celsius")
        print("5. Fahrenheit a Kelvin")
        print("6. Kelvin a Fahrenheit")
        choice = input("Elige la conversión (1/2/3/4/5/6): ")

        if choice in ['1', '2', '3', '4', '5', '6']:
            if choice == '1':
                celsius = float(input("Introduce la temperatura en Celsius: "))
                print("Temperatura convertida a Fahrenheit:", celsius_to_fahrenheit(celsius))
            elif choice == '2':
                fahrenheit = float(input("Introduce la temperatura en Fahrenheit: "))
                print("Temperatura convertida a Celsius:", fahrenheit_to_celsius(fahrenheit))
            elif choice == '3':
                celsius = float(input("Introduce la temperatura en Celsius: "))
                print("Temperatura convertida a Kelvin:", celsius_to_kelvin(celsius))
            elif choice == '4':
                kelvin = float(input("Introduce la temperatura en Kelvin: "))
                print("Temperatura convertida a Celsius:", kelvin_to_celsius(kelvin))
            elif choice == '5':
                fahrenheit = float(input("Introduce la temperatura en Fahrenheit: "))
                print("Temperatura convertida a Kelvin:", fahrenheit_to_kelvin(fahrenheit))
            elif choice == '6':
                kelvin = float(input("Introduce la temperatura en Kelvin: "))
                print("Temperatura convertida a Fahrenheit:", kelvin_to_fahrenheit(kelvin))
        else:
            print("Selección inválida")
    elif language == 'French':
        print("1. Celsius en Fahrenheit")
        print("2. Fahrenheit en Celsius")
        print("3. Celsius en Kelvin")
        print("4. Kelvin en Celsius")
        print("5. Fahrenheit en Kelvin")
        print("6. Kelvin en Fahrenheit")
        choice = input("Choisissez la conversion (1/2/3/4/5/6): ")

        if choice in ['1', '2', '3', '4', '5', '6']:
            if choice == '1':
                celsius = float(input("Entrez la température en Celsius: "))
                print("Température convertie en Fahrenheit:", celsius_to_fahrenheit(celsius))
            elif choice == '2':
                fahrenheit = float(input("Entrez la température en Fahrenheit: "))
                print("Température convertie en Celsius:", fahrenheit_to_celsius(fahrenheit))
            elif choice == '3':
                celsius = float(input("Entrez la température en Celsius: "))
                print("Température convertie en Kelvin:", celsius_to_kelvin(celsius))
            elif choice == '4':
                kelvin = float(input("Entrez la température en Kelvin: "))
                print("Température convertie en Celsius:", kelvin_to_celsius(kelvin))
            elif choice == '5':
                fahrenheit = float(input("Entrez la température en Fahrenheit: "))
                print("Température convertie en Kelvin:", fahrenheit_to_kelvin(fahrenheit))
            elif choice == '6':
                kelvin = float(input("Entrez la température en Kelvin: "))
                print("Température convertie en Fahrenheit:", kelvin_to_fahrenheit(kelvin))
        else:
            print("Choix invalide")
    elif language == 'German':
        print("1. Celsius zu Fahrenheit")
        print("2. Fahrenheit zu Celsius")
        print("3. Celsius zu Kelvin")
        print("4. Kelvin zu Celsius")
        print("5. Fahrenheit zu Kelvin")
        print("6. Kelvin zu Fahrenheit")
        choice = input("Wähle die Umwandlung (1/2/3/4/5/6): ")

        if choice in ['1', '2', '3', '4', '5', '6']:
            if choice == '1':
                celsius = float(input("Temperatur in Celsius eingeben: "))
                print("Temperatur in Fahrenheit umgerechnet:", celsius_to_fahrenheit(celsius))
            elif choice == '2':
                fahrenheit = float(input("Temperatur in Fahrenheit eingeben: "))
                print("Temperatur in Celsius umgerechnet:", fahrenheit_to_celsius(fahrenheit))
            elif choice == '3':
                celsius = float(input("Temperatur in Celsius eingeben: "))
                print("Temperatur in Kelvin umgerechnet:", celsius_to_kelvin(celsius))
            elif choice == '4':
                kelvin = float(input("Temperatur in Kelvin eingeben: "))
                print("Temperatur in Celsius umgerechnet:", kelvin_to_celsius(kelvin))
            elif choice == '5':
                fahrenheit = float(input("Temperatur in Fahrenheit eingeben: "))
                print("Temperatur in Kelvin umgerechnet:", fahrenheit_to_kelvin(fahrenheit))
            elif choice == '6':
                kelvin = float(input("Temperatur in Kelvin eingeben: "))
                print("Temperatur in Fahrenheit umgerechnet:", kelvin_to_fahrenheit(kelvin))
        else:
            print("Ungültige Auswahl")
    else:
        print("Invalid language choice")

if __name__ == "__main__":
    main()
