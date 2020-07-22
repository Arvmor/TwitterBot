<?php
$account = $_POST['account'];
$retweet = $_POST['retweet'];
$follow = $_POST['follow'];
$errorText = $_POST['errorText'];
$command = escapeshellcmd("./../UpdateCredentials.py $account EndAccounts $retweet EndRetweet $follow EndFollow $errorText EndError");
shell_exec($command);
header("location:javascript://history.go(-1)");
?>