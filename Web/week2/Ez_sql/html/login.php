<?php
error_reporting(0);

// session_start();
$servername = "mysql:3306";
$db_username = "root";
$db_password = "0xgame@7747";
$db_name="ctf"; 

// 创建连接
$conn = mysqli_connect($servername, $db_username, $db_password);
 
// 检测连接
if (!$conn) {
    die("#error:" . mysqli_connect_error());
}
mysqli_select_db($conn,$db_name) or die('Could not select database: ' . mysqli_error());


function query($conn,$sql) {
	$result = mysqli_query($conn,$sql);
	$rows = mysqli_fetch_assoc($result);
	return $rows;
}

$username = isset($_POST['username']) ? $_POST['username'] : "";
$password = isset($_POST['password']) ? addslashes($_POST['password']) : "";
if ($username == '' || $password == '')
        {
            header("Location:/?err=2");
            die();}
//$action = isset($_GET['action']) ? $_GET['action'] : "index";
//$user=$_SESSION['username'];
if(preg_match('/and|union|alter|order|by|join|ascii|\*|substr| |=|ctf|group|benchmark|get_lock|rlike|rpad|count|repeat/is',$username)){
   echo "Illegal Character Dectected";
    die();
}
// switch ($action) {
// case 'index':
//     header("Location: /");
//     exit;

// case 'login':
$res = query($conn,"select * from 0xgame where user='{$username}' and passwd='{$password}';");
mysqli_close($conn);
if (1==2) {
    echo "hello ".$res['user'].",your score is ".$res['score']."!";
    die();
}
else{
  // echo 'login failed';
    header("Location:/?err=1");
}


?>
