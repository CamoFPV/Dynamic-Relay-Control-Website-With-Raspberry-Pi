<?php
$output = shell_exec('sudo python ../PY/10off.py 2>&1');
echo "<pre>$output</pre>";
header("Location: ../index.php");
exit;
?>
