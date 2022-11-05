<?php
header("Content-Type: text/html;charset=utf-8");

$username = isset($_POST['username']) ? $_POST['username'] : "";
$password = isset($_POST['password']) ? $_POST['password'] : "";


if ($username == '' || $password == '')
        {
            header("Location:login.php?err=2");
            die();}
if ($username != 'admin' || $password != '01234')
        header("Location:login.php?err=1");

else
    {
        session_start();
        $_SESSION['admin'] = true;
        $n=strval(mt_rand(1,5)); 
        header("Location:admin.php?f=dogs_diary/d".$n);
    }




?>