<?php
function createSingleFileNav()
{
    $links = [
        "Dbcustomcard",
    ];
    foreach ($links as $link) {
        echo "<a href='single-file/{$link}.php'>$link</a> ";
    }
}

function createMultiFileNav()
{
    $links = [
        "TBA",
    ];

    foreach ($links as $link) {
        echo "<a href='{$link}/'>$link</a> ";
    }
}

?>
<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Navigation</title>
</head>
<body>
<div>
    <p>To single file projects</p>
    <nav aria-label="singleFile"><?php createSingleFileNav() ?></nav>
</div>
<div>
    <p>To multi file projects</p>
    <nav aria-label="multiFile"><?php createMultiFileNav() ?></nav>
</div>
</body>
</html>
