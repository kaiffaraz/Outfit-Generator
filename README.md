# AI Formal Outfit Generator

The **AI Formal Outfit Generator** is a web-based application that helps users automatically generate stylish outfit combinations for the workweek.  
Users can upload their shirts and pants, and the system intelligently pairs them to form **professional, non-repetitive, and visually appealing formal outfits**.  
It also displays the combinations on a **3D mannequin model** for better visualization.

---

## Features

 Upload your **shirts** and **pants** easily  
 Generates **formal outfit combinations** for 6 working days  
 Ensures **no repeated clothes** in a week  
 Smart **color-based matching** (avoids uniform-style same-color matches)  
 Displays **outfit names** (e.g., “White Shirt with Black Pants”)  
 Integrated **3D mannequin** to visualize color combinations  
 **Attractive UI** with smooth buttons and progress animation  
 **Auto browser launch** when you run the app  

---

## Tech Stack

**Frontend:**
- HTML5, CSS3, JavaScript (Vanilla)
- Three.js / `<model-viewer>` for 3D mannequin

**Backend:**
- Python Flask
- Flask-CORS
- Threading + Webbrowser (for auto browser open)

**Other Tools:**
- Sketchfab (for downloading 3D mannequin `.glb` file)

---

## How It Works

- Upload your shirt and pant images.
- Click Generate Outfits.
- The model:
 -> Pairs the items to form stylish non-repetitive combinations
 -> Displays each combination with shirt + pant names
 -> Updates mannequin colors dynamically  
- You get a complete formal outfit plan for the week 

---

## Use Case: 

- Working professionals who want quick outfit suggestions
- Students preparing daily formal wear
- Anyone who wants to organize their wardrobe efficiently

---

## Conclusion

The AI Formal Outfit Generator saves time, avoids repetitive dressing, and gives you a stylish look every day.  
 It’s a perfect mix of AI + Fashion + Web Technology that enhances productivity and personal style.
