<!DOCTYPE html>
<html>
<head>
    <title>admin的日记</title>
    <meta name="content-type";
          charset="UTF-8">
</head>
<body>
<div>
    <?php
    error_reporting(0);
    session_start(); 
    if (!isset($_SESSION["admin"]) || $_SESSION['admin'] != true) 
    {   
        die('<h1>请先狠狠地登陆!!!</h1>') ;
    }
    else {
        if (isset($_GET['f']))
            {
            echo file_get_contents($_GET['f']);}
        else {
            $n=strval(mt_rand(1,5));
            echo file_get_contents('dogs_diary/d'.$n);
        }
    }

    ?> 
</body>
<!-- flag in /tmp/flag -->
</html>
