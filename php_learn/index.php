<?php $this->insert('header',['title' => 'User Profile']) ?>
<h1> User Profile</h1>

<p>Hello,<?=$this->escape($name)?></p>

<?php $this->insert('footer')?>
