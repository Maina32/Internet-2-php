<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $num1 = $_POST['num1'];
    $num2 = $_POST['num2'] ?? null;
    $operation = $_POST['operation'];
    $result = '';

    switch ($operation) {
        case 'add':
            $result = $num1 + $num2;
            break;
        case 'subtract':
            $result = $num1 - $num2;
            break;
        case 'multiply':
            $result = $num1 * $num2;
            break;
        case 'divide':
            $result = $num2 != 0 ? $num1 / $num2 : 'Error: Division by zero';
            break;
        case 'exponent':
            $result = pow($num1, $num2);
            break;
        case 'percentage':
            $result = ($num1 / 100) * $num2;
            break;
        case 'sqrt':
            $result = sqrt($num1);
            break;
        case 'log':
            $result = log($num1);
            break;
        default:
            $result = 'Invalid operation';
    }

    echo "<h1>Result: $result</h1>";
    echo '<a href="index.php">Back to Calculator</a>';
}
?>
