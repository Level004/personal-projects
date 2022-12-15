<!DOCTYPE html>
<html lang="en">
<head>
    <title>Font scramble</title>
</head>
<body>
<h1>font scramble</h1>

<form method="post">
    <input type="text" id="text" name="text">
    <button type="submit">submit</button>
</form>

<div id="results">
    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $text = $_POST["text"];

        $fonts = ["Arial", "Verdana", "Helvetica", "Times New Roman", "Courier", "Comic Sans MS", "Papyrus"];
        $output = "";

        for ($i = 0; $i < strlen($text); $i++) {
            $font = $fonts[array_rand($fonts)];
            $output .= "<span style='font-family: $font;'>$text[$i]</span>";
        }

        echo $output;
    }

    ?>
</div>

</body>
</html>
