<?php
highlight_file(__FILE__);



class Apple{
    public  $var;

    public function __wakeup(){
        $this->var->value;
    }

    public function __invoke(){
        echo $this->var;
    }
}

class Banana{
    public $source="pop.php";
    public $str;

    public function __toString(){
        echo file_get_contents($this->source);
        return 'do u like pop?';
    }
 
    public function __construct(){
        $this->source = "flag in flag.php";
        echo 123;
    }
}

class Cherry{
    public $p;
    public $o;

    public function __construct(){
        $this->o = 'pop song';
    }

    public function __get($key){
        ($this->p)();
    }
}


if(isset($_GET['pop'])){
    @unserialize($_GET['pop']);
}