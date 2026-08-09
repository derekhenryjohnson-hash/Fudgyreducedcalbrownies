import os

# 1. Define your brownie recipe article content using plain Markdown/HTML text
blog_content = """
<h2>Fudgy Low-Calorie Brownies (Easy Keto-Friendly Recipe)</h2>
<p>If you are looking for a rich, decadent dessert that won’t derail your health goals, these brownies are a game changer.</p>
<h3>🔑 Key Ingredients</h3>
<ul>
<li><a href="YOUR_AFFILIATE_LINK">Navitas Organics Cacao Powder</a></li>
<li><a href="YOUR_AFFILIATE_LINK">Lakanto Monkfruit Sweetener</a></li>
</ul>
<h3>📥 The Recipe Card</h3>
<p><b>Calories:</b> 115 kcal | <b>Net Carbs:</b> 2g</p>
<p>Mix 1/2 cup butter, 1 cup monkfruit, 2 eggs, 1/2 cup Navitas cacao, and 3 tbsp flour. Bake at 325°F for 20 mins.</p>
"""

# 2. Define your master layout HTML template (No database required)
html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Healthy Baking Blog</title>
<style>
body {{ font-family: sans-serif; max-width: 800px; margin: 40px auto; padding: 0 20px; line-height: 1.6; color: #333; }}
h2 {{ color: #4A2c2a; }}
a {{ color: #d35400; font-weight: bold; text-decoration: none; }}
.ad-space {{ background: #f9f9f9; padding: 20px; border: 1px dashed #ccc; text-align: center; margin: 20px 0; }}
</style>
</head>
<body>
<header><h1>🌱 The Clean Baking Kitchen</h1></header>
<hr>
<main>
{blog_content}
<div class="ad-space">💡 [Future Display Ad Unit Placement Space]</div>
</main>
<footer><p>&copy; 2026 Healthy Baking Blog</p></footer>
</body>
</html>
"""

# 3. Output the raw data cleanly into a production-ready website file
os.makedirs("public", exist_ok=True)
with open("public/index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("Website generated successfully in the /public folder!")
