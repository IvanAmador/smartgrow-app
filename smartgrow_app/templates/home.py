<!-- templates/home.html -->
<!DOCTYPE html>
<html>
<head>
    <title>SmartGrow</title>
</head>
<body>
    <h1>SmartGrow</h1>
    <ul>
        {% for crop in crops %}
            <li>{{ crop.name }} ({{ crop.description }})</li>
        {% endfor %}
    </ul>
</body>
</html>