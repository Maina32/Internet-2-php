<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Calculator</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <form action="calculator.php" method="post">
        <label for="num1">Number 1:</label>
        <input type="number" name="num1" step="any" required><br>
        
        <label for="num2">Number 2:</label>
        <input type="number" name="num2" step="any"><br>
        
        <label for="operation">Operation:</label>
        <select name="operation" required>
            <option value="add">Addition</option>
            <option value="subtract">Subtraction</option>
            <option value="multiply">Multiplication</option>
            <option value="divide">Division</option>
            <option value="exponent">Exponentiation</option>
            <option value="percentage">Percentage</option>
            <option value="sqrt">Square Root</option>
            <option value="log">Logarithm</option>
        </select><br>
        
        <button type="submit">Calculate</button>
    </form>
</body>
</html>
