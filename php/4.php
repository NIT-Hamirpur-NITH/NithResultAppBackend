<?php
$conn = new mysqli("localhost","username","password","dbname");
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
$name = $_POST['name'];
//$name="Mukesh";
//$sem = "14MI5421";
$query = "select * from students where name like '$name%'";
$result = $conn->query($query);

if($result){
	$count = 0;
	$res = array();
	while($row = $result->fetch_assoc()){
		$temp = array("Name" => $row['name'], "roll_no"=>$row['roll_no'], "CGPI"=>$row['cgpi']);
		array_push($res, $temp);
		$count++;
		
	}
	$f_res = array("result" => $res);
	echo json_encode($f_res);
	
} else{
	echo "error in fetching";
}

?>
