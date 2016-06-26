<?php

$pdo = new PDO('mysql:host=localhost;dbname=school','root','123456');
$statement = $pdo->query("SELECT no from student");
$rows = $statement->fetchAll(PDO::FETCH_ASSOC);
foreach( $rows as $row) {
    echo $row['name'] ."\n";
}


?>

