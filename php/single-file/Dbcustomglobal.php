<?php

function generateCard($pic, $picCode, $name, $oldScale,$newScale = 1) {
    echo" [src$=\"{$picCode}\"] { <br>";
    echo "content: url({$pic}); <br>";
    echo "height: 100%; <br>";
    echo "width: 100%; <br>";
    echo "} <br> <br>";

    echo"[src$=\"{$picCode}\"]~[style*=\"{$oldScale};\"] { <br>";
    echo "font-size: 0 !important; <br>";
    echo "{$newScale} !important; <br>";
    echo "} <br> <br>";

    echo "[src$=\"{$picCode}\"]~span[style*=\"{$oldScale};\"]::before { <br>";
    echo "content: \"{$name}\"; <br>";
    echo "font-size: 80.4px; <br>";
    echo "}";
}

?>

<!doctype html>
<html lang="nl">
<head>
    <meta charset="utf-8"/>
    <title>DB custom card global</title>
</head>
<body style="background-color: black; color: white;">
<form method="POST">
    <input type="text" placeholder="pic" id="pic" name="pic"><br>
    <input type="text" placeholder="piccode" id="piccode" name="piccode"><br>
    <input type="text" placeholder="name" id="name" name="name"><br>
    <input type="text" placeholder="old scale" id="oldscale" name="oldscale"><br>
    <input type="text" placeholder="new scale" id="newscale" name="newscale"><br>
    <input type="submit" value="bewaren">
</form>
<div style="padding-left: 30vw;">
    <?php
    if($_POST){
        generateCard($_POST['pic'], $_POST['piccode'], $_POST['name'], $_POST['oldscale'], $_POST['newscale']);
    }
    ?>
</div>
</body>
</html>
