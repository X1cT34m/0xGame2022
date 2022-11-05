<!DOCTYPE html>
<html>
<head>
    <title>登录</title>
    <link rel="stylesheet" href="style.css">
    <meta name="content-type"; charset="UTF-8">
</head>
<body>
<div id="bigBox">
        <h1>LOGIN</h1>

        <form id="loginform" action="check4login.php" method="post">
            <div class="inputBox">

                    <div class="inputText">
                        <input type="text" id="name" name="username" placeholder="Username" value="">
                    </div>
                <div class="inputText">
                   <input type="password" id="password" name="password" placeholder="五位密码很安全辣">
                </div>
                <br >
                <div style="color: white;font-size: 12px" >
                <div>
               <input type="submit" id="login" value="登录" class="loginButton m-left" >
           </div>
           <?php
                    $err = isset($_GET["err"]) ? $_GET["err"] : "";
                    
                    switch ($err) {
                        case 1:
                            echo "用户名或密码错误！";
                            break;

                        case 2:
                            echo "用户名或密码不能为空！";
                            break;
                    } ?>

                </div>
            </div>

</div>
</div>
</form>
</body>
</html>

