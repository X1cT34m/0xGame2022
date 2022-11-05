<?php 
error_reporting(1);
highlight_file(__FILE__);
$url=$_GET['url'];
if(preg_match('/127|dict|file|ftp|localhost|0.0.0.0/',$url)){
  die('想都别想');
}//evil.php
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_HEADER, 0);
$output = curl_exec($ch);
curl_close($ch);
echo $output;
