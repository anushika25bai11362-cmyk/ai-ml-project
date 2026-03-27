print("💇‍♀️ Welcome to Haircare Test 💇‍♂️\n")

score = {
    "oily": 0,
    "dry": 0,
    "normal": 0,
    "combination": 0
}

# Questions
print("Answer the following questions:\n")

# Q1
q1 = input("1. How often does your hair get oily?\n(a) Within 1 day\n(b) After 2-3 days\n(c) Rarely\n: ").lower()
if q1 == 'a':
    score["oily"] += 2
elif q1 == 'b':
    score["normal"] += 1
    score["combination"] += 1
else:
    score["dry"] += 2

# Q2
q2 = input("\n2. How does your scalp feel?\n(a) Greasy\n(b) Balanced\n(c) Tight or itchy\n: ").lower()
if q2 == 'a':
    score["oily"] += 2
elif q2 == 'b':
    score["normal"] += 2
else:
    score["dry"] += 2

# Q3
q3 = input("\n3. How do your hair ends feel?\n(a) Oily\n(b) Normal\n(c) Dry/split ends\n: ").lower()
if q3 == 'a':
    score["oily"] += 1
elif q3 == 'b':
    score["normal"] += 2
else:
    score["dry"] += 2
    score["combination"] += 1

# Q4
q4 = input("\n4. How often do you wash your hair?\n(a) Daily\n(b) 2-3 times a week\n(c) Once a week\n: ").lower()
if q4 == 'a':
    score["oily"] += 2
elif q4 == 'b':
    score["normal"] += 2
else:
    score["dry"] += 2

# Determine hair type
hair_type = max(score, key=score.get)

print("\n✨ Your Hair Type is:", hair_type.upper(), "✨\n")

# Suggestions
if hair_type == "oily":
    print("🧴 Haircare Tips:")
    print("- Wash hair frequently")
    print("- Use lightweight shampoo")
    print("- Avoid heavy oils")

    print("\n⚠️ Avoid Chemicals:")
    print("- Silicones")
    print("- Heavy oils (Mineral oil)")

    print("\n✅ Recommended Ingredients:")
    print("- Tea tree oil")
    print("- Salicylic acid")
    print("- Aloe vera")

elif hair_type == "dry":
    print("🧴 Haircare Tips:")
    print("- Use moisturizing shampoo")
    print("- Apply conditioner regularly")
    print("- Avoid excessive heat styling")

    print("\n⚠️ Avoid Chemicals:")
    print("- Sulfates (SLS/SLES)")
    print("- Alcohol-based products")

    print("\n✅ Recommended Ingredients:")
    print("- Argan oil")
    print("- Coconut oil")
    print("- Shea butter")

elif hair_type == "normal":
    print("🧴 Haircare Tips:")
    print("- Maintain regular washing routine")
    print("- Use mild shampoo")
    print("- Keep balanced hydration")

    print("\n⚠️ Avoid Chemicals:")
    print("- Harsh sulfates")
    print("- Excessive silicones")

    print("\n✅ Recommended Ingredients:")
    print("- Aloe vera")
    print("- Mild proteins")
    print("- Essential oils")

else:  # combination
    print("🧴 Haircare Tips:")
    print("- Use balancing shampoo")
    print("- Focus conditioner on ends")
    print("- Avoid over-washing")

    print("\n⚠️ Avoid Chemicals:")
    print("- Heavy silicones")
    print("- Strong sulfates")

    print("\n✅ Recommended Ingredients:")
    print("- Aloe vera")
    print("- Jojoba oil")
    print("- Tea tree oil")

print("\n💡 Thank you for taking the Haircare Test!")
