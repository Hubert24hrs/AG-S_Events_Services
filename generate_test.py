import random

lagos_names = ["The Adeyemi Family", "Mrs. Funke Adeleke", "Folashade Ojo", "Adebowale & Yemisi", "Oluwaseun & Tobi", "Chief Olusegun", "Dr. Yinka Ayodeji", "The Balogun Family", "Tolulope & Dapo", "Mr. Babatunde"]
abuja_names = ["Senator Danladi", "Alhaji Tariq Danjuma", "Musa Ibrahim", "Amina & Yusuf", "Engr. Suleiman"]
enugu_names = ["Amara & Chidi Okonkwo", "Chioma Eze", "The Nnamdi Family"]
ph_names = ["Boma Briggs", "Tamuno & Ibi", "The Alaibo Family"]
imo_names = ["Chief Emeka Nwosu", "Kelechi & Nkiru"]
other_states = [
    ("Kano", "Aisha & Fatima Bello"), ("Kaduna", "Engr. Abubakar Musa"), ("Uyo", "Dr. Nsikak Akpan"), 
    ("Warri", "Oritseweyinmi & Efe"), ("Calabar", "Precious Edem"), ("Asaba", "The Okowa Family"), 
    ("Benin", "Osas & Nosakhare"), ("Jos", "Mr. Plateau Dawit"), ("Ibadan", "The Makinde Family"),
    ("Abeokuta", "Olawale & Simi"), ("Akure", "The Olatunji Family"), ("Osogbo", "Mr. & Mrs. Adeleke"),
    ("Ilorin", "Alhaji Abdulrahman"), ("Ado-Ekiti", "Dr. Fayemi"), ("Lokoja", "The Bello Family"),
    ("Minna", "Hajiya Zainab"), ("Awka", "The Okafor Family"), ("Umuahia", "Orji & Nkechi"),
    ("Yenagoa", "The Dickson Family"), ("Makurdi", "Mr. Terhemen"), ("Lafia", "The Al-Makura Family"),
    ("Sokoto", "Alhaji Tambuwal"), ("Bauchi", "The Mohammed Family"), ("Gombe", "Mr. Inuwa"),
    ("Yola", "The Fintiri Family"), ("Katsina", "Alhaji Masari"), ("Jalingo", "The Ishaku Family")
]

quotes = [
    "AG's Event Services transformed our event into something beyond our wildest dreams. Every detail was perfect.",
    "Our annual gala has never looked so impressive. The team understood exactly what our brand needed.",
    "I've worked with many event planners but none with the eye for luxury that this team brings.",
    "During such a difficult time, the team handled everything with grace and dignity. Truly remarkable.",
    "Their attention to detail during our dinner was spectacular. They brought a unique blend of elegance.",
    "The exquisite decor and seamless coordination made our celebration truly magical.",
    "Every single moment was captured and executed flawlessly. Hands down the best in the business.",
    "The conference they organized for us was seamless. From registration to the final gala night.",
    "I trusted them with my milestone celebration and they delivered beyond measure.",
    "Hosting an official meeting requires precision. They provided a secure, premium environment.",
    "My launch party was the talk of the town! The aesthetics were breathtaking.",
    "We wanted a mix of modern luxury and deep traditions. They effortlessly blended both worlds.",
    "Their event logistics are top-notch. Managing our large attendee list was handled with grace.",
    "Organizing our final rites was emotionally tasking, but the team stepped in beautifully.",
    "For our end-of-year dinner, we needed perfection. They gave us exactly that.",
    "The bespoke styling for my charity gala was magnificent. I was blown away by their creativity.",
    "Celebrating our anniversary with them was the best decision. They treated us like royalty.",
    "I wanted a vibrant, culturally rich yet modern bash. The result was a stunning event.",
    "We hired them for our executive retreat. The hospitality and dining arrangements were highly commendable.",
    "A truly world-class event management company. Their ability to deliver is simply outstanding.",
    "The venue transformation was unbelievable. They truly have a gift for spatial design.",
    "From the lighting to the sound, everything was orchestrated to perfection.",
    "Our guests are still talking about the incredible experience they had.",
    "They took our vision and elevated it to a level of sophistication we didn't think was possible.",
    "Professional, punctual, and profoundly talented. I won't use anyone else."
]

testimonials = []

def add_t(city, name):
    quote = random.choice(quotes)
    testimonials.append({
        "quote": quote,
        "name": name,
        "designation": f"Client · {city}"
    })

for n in lagos_names: add_t("Lagos", n)
for n in abuja_names: add_t("Abuja", n)
for n in enugu_names: add_t("Enugu", n)
for n in ph_names: add_t("Port Harcourt", n)
for n in imo_names: add_t("Imo", n)
for city, n in other_states: add_t(city, n)

# Shuffle with constraints: no consecutive Lagos
final_list = []
random.shuffle(testimonials)

lagos_items = [t for t in testimonials if "Lagos" in t["designation"]]
other_items = [t for t in testimonials if "Lagos" not in t["designation"]]

while lagos_items or other_items:
    if not final_list:
        if lagos_items and random.random() > 0.5:
            final_list.append(lagos_items.pop())
        else:
            final_list.append(other_items.pop())
    else:
        last_was_lagos = "Lagos" in final_list[-1]["designation"]
        
        if last_was_lagos:
            if other_items:
                final_list.append(other_items.pop())
            else:
                final_list.append(lagos_items.pop()) # Force it if only Lagos left
        else:
            if lagos_items and other_items:
                if random.random() > 0.6:
                    final_list.append(lagos_items.pop())
                else:
                    final_list.append(other_items.pop())
            elif lagos_items:
                final_list.append(lagos_items.pop())
            elif other_items:
                final_list.append(other_items.pop())

# Generate JS code
js_code = "  const testimonials = [\n"
for i, t in enumerate(final_list):
    q = t['quote'].replace('"', '\\"')
    n = t['name'].replace('"', '\\"')
    d = t['designation'].replace('"', '\\"')
    js_code += '    {\n'
    js_code += f'      quote: "{q}",\n'
    js_code += f'      name: "{n}",\n'
    js_code += f'      designation: "{d}"\n'
    js_code += '    }'
    if i < len(final_list) - 1:
        js_code += ','
    js_code += '\n'
js_code += "  ];"

with open("C:/Users/HP/.gemini/antigravity/scratch/ags_event_services/testimonials_output.txt", "w", encoding="utf-8") as f:
    f.write(js_code)

print("Generated successfully!")
