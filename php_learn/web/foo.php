<?php
$db = new PDO('mysql:host=localhost;dbname=school','root','123456');
include 'models/FooModel.php';

$fooModel = new FooModel($db);
$fooList = $fooModel->getAllFoos();

include 'views/foo-list.php';
