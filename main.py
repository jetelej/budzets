import matplotlib.pyplot as plt

# Ievadām kategorijas
categories = ['Pārtika', 'Izklaide', 'Transporta izdevumi', 'Mājoklis', 'Citi']

# Izveidojam tukšu sarakstu, lai glabātu ievadītās summas
amounts = []

# Pieprasām lietotājam ievadīt summas par katru kategoriju
for category in categories:
    while True:
        try:
            amount = float(input(f"Lūdzu ievadiet, cik naudas iztērējāt kategorijā '{category}': "))
            amounts.append(amount)
            break
        except ValueError:
            print("Ievadītajai vērtībai jābūt skaitlim. Lūdzu mēģiniet vēlreiz.")

# Aprēķinām kopējo iztērēto naudu
total = sum(amounts)

# Ja kopējā summa ir 0, iznākums būtu nepareizs
if total == 0:
    print("Kopējā summa nevar būt 0. Lūdzu ievadiet derīgas vērtības.")
else:
    # Aprēķinām procentus no katras kategorijas
    percentages = [(amount / total) * 100 for amount in amounts]

    # Izveidojam pie chart
    plt.pie(percentages, labels=categories, autopct='%1.1f%%', startangle=90)
    plt.title('Izdevumu sadalījums pēc kategorijām')
    plt.axis('equal')  # Nodrošina, ka grafiks ir apļveida
    plt.show()
