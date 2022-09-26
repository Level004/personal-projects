<?php

function DBcustomcard($deck, $replacePic, $originalPicCode, $name){
    echo ".card:not(.card[style*=\"-0.1485,\"]) .{$deck} img[src*=\"/{$originalPicCode}.jpg\"], <br>";
    echo ".preview .{$deck} img[src*=\"/{$originalPicCode}.jpg\"], <br>";
    echo ".cards .{$deck} img[src*=\"/{$originalPicCode}.jpg\"] { <br>";
    echo "content: url({$replacePic}); <br>";
    echo "} <br> <br>";

    echo ".{$deck} img[src*=\"/{$originalPicCode}.jpg\"]~.name_txt.selectable { <br>";
    echo "font-size: 0 !important; <br> transform: scaleX(1) !important; <br>";
    echo "} <br> <br>";

    echo ".{$deck} img[src*=\"/{$originalPicCode}.jpg\"]~.name_txt.selectable::before { <br>";
    echo "content: \"{$name}\"; <br> font-size: 80.4px; <br>";
    echo "}";
}

?>

<!doctype html>
<html lang="nl">
<head>
    <meta charset="utf-8"/>
    <title>DB custom card</title>
</head>
<body>
<form method="POST">
    <input type="text" placeholder="deck" id="deck" name="deck"><br>
    <input type="text" placeholder="pic" id="pic" name="pic"><br>
    <input type="text" placeholder="piccode" id="piccode" name="piccode"><br>
    <input type="text" placeholder="name" id="name" name="name"><br>
    <input type="submit" value="bewaren">
</form>
<div>
    <?php
    if($_POST){
     DBcustomcard($_POST['deck'], $_POST['pic'], $_POST['piccode'], $_POST['name']);
    }
    ?>
</div>
</body>
</html>
