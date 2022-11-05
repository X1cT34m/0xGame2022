<?php
error_reporting(1);
if('127.0.0.1'!=$_SERVER['REMOTE_ADDR']){
	die('Allow local only');
}
if('GET' === $_SERVER['REQUEST_METHOD']){
  highlight_file(__FILE__);
  die('Invalid request mode');
}
if(isset($_POST['c'])){
    $c=$_POST['c'];
    if(preg_match('/[^\W_]+\((?R)?\)/',$c)){
      eval($c);
    }
    else die('nonono');
}
