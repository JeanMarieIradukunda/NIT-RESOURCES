
# Display special message depending on day entered

day = input("Enter the day name: ").strip().lower()

match day:
    case "christmas":
        print("🎄 Merry Christmas! A time for joy and celebration.")
    case "independence":
        print("🎆 Happy Independence Day! Celebrate your nation’s freedom.")
    case "easter":
        print("🕊️ Happy Easter! A day of hope and renewal.")
    case "new year" | "newyear":
        print("🌙 Happy New Year! Wishing you success and happiness.")
    case "labor":
        print("💪 Happy Labor Day! A tribute to workers everywhere.")
    case _:
        print("Not a special day.")
