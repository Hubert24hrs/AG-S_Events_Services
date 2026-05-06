import re

with open("C:/Users/HP/.gemini/antigravity/scratch/ags_event_services/testimonials_output.txt", "r", encoding="utf-8") as f:
    replacement = f.read()

with open("C:/Users/HP/.gemini/antigravity/scratch/ags_event_services/index.html", "r", encoding="utf-8") as f:
    content = f.read()

new_content = re.sub(r'  const testimonials = \[.*?  \];', replacement, content, flags=re.DOTALL)

with open("C:/Users/HP/.gemini/antigravity/scratch/ags_event_services/index.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Replacement successful!")
