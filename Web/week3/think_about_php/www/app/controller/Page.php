<?php
namespace app\controller;

use app\BaseController;

class Page extends BaseController
{
    public function hello()
    {
        return '<style type="text/css">*{ padding: 0; margin: 0; } div{ padding: 4px 48px;} a{color:#2E5CD5;cursor: pointer;text-decoration: none} a:hover{text-decoration:underline; } body{ background: #fff; font-family: "Century Gothic","Microsoft yahei"; color: #333;font-size:18px;} h1{ font-size: 100px; font-weight: normal; margin-bottom: 12px; } p{ line-height: 1.6em; font-size: 42px }</style><div style="padding: 24px 48px;"> <h1>:) </h1><p> hello my friend!:)' .  '<br/><span style="font-size:30px;"><del>不记得几载了</del>初心不改 - 你值得信赖的新手入门比赛</span></p><span style="font-size:25px;">[ 由 <a href="https://0xgame.h4ck.fun/home" target="yisu">0xGame</a> 独家赞助发布 ]</span></div><think id="ee9b1aa918103c4fc"></think>';
    }


    public function evil()
    {   
        
        if(isset($_GET['f'])){
            $f=$_GET['f'];
            if(preg_match('/\(|\)/',$f)){
                return self::hello();
            }
            eval($f);
       }else return self::hello();
    }
        
}