<?php
error_reporting(0);
highlight_file(__FILE__);

$a=$_GET['param1'];
$b=$_POST['param2'];

$a=preg_replace('/system|eval|preg_replace|create_function|array_map|call_user_func|call_user_func_array|array_filter|usort|uasort|file|content|passthru|exec|shell_exec|popen|proc_open|pcntl_exec|assert/is','',$a);
$b=preg_replace('/cat|tac|tail|nl|more|less|head|flag/is','?Q__Q?',$b);


$a($b);
?>