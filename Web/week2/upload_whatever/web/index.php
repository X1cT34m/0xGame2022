<!DOCTYPE html>
<html>
<head>
    <title>UPLOAD</title>
    <link rel="stylesheet" href="style.css">
    <meta name="content-type"; charset="UTF-8">
</head>
<body>
<div id="bigBox">
        <h1>UPLOAD</h1>

        <form id="loginform" action="" method="post" enctype="multipart/form-data">
            <div class="inputBox">

                    <div class="inputText">
                        <input type="file" id="uploadfile" name="file"  value="">
                    </div>
                <br >
                <div style="color: white;font-size: 12px" >
                <div>
               <input type="submit" name="upload" value="GO" class="loginButton m-left" >
           </div>
           <?php
           error_reporting(0);
    if($_POST['upload'])
    {
        if($_FILES['file']['error']>0)
            echo "<center>"."upload error"."</center>";
        else
        {
            if($_FILES['file']['size']>0 && $_FILES['file']['size']<1024*1024*2 )
            {
                $dir='images';
                if(!is_dir($dir)) mkdir($dir);
                $tmp_filename=$_FILES['file']['tmp_name'];
                $filename=$_FILES['file']['name'];
                if(preg_match('/ph|\.\.|ini/i',$filename)){
                    echo '<br></br>what\'s this?';
                    die();
                }

                if(is_uploaded_file($tmp_filename))
                {
                    if(move_uploaded_file($tmp_filename,$dir."/".$filename))
                    {
                        if(!getimagesize($dir."/".$filename))
                        {
                            unlink($dir."/".$filename);
                            echo '<br></br>what\'s this?';
                            die();
                        }
                        echo "<br></br><center>"."SUCCESS!"."</center>";
                        echo "<center>"."文件大小:".($_FILES['file']['size']/1024)."KB"."</center>";
                        echo "<center>"."文件位置:".$dir."/".$filename."</center>";
                    }
                    else
                        echo "<center>"."upload failed!"."</center>";
                }
            }
            else
                echo "<br></br><center>"."what's this?"."</center>";
        }
    }
?>

                </div>
            </div>

</div>
</div>
</form>
</body>
</html>

