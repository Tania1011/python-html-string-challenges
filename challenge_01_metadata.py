html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Page</title>
    <link rel="stylesheet" href="styles.css">
    <script src="app.js"></script>
</head>
<body>
</body>
    <h1>Welcome to My Page</h1>
    <p>My Page</p>
</html>"""

page_title="My Awesome Portfolio"
page_lang ="fr"
updatedHTML=html.replace("My Page", f"{page_title}",2) # 2 - Replace the two first occurrences of "My Page" with the value of page_title
updatedHTML=updatedHTML.replace('lang="en"', f'lang="{page_lang}"',1)# Replace the first occurrence of 'lang="en"' with 'lang="fr"' using the value of page_lang
print("\nUpdated HTML:\n", updatedHTML)
