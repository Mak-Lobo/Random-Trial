<?php 
$fname = $_POST['fname'];
$lname = $_POST['lname'];
$id = $_POST['id'];
$email = $_POST['email'];
$dob = $_POST['dob'];
$phone = $_POST['phone'];
$sex = $_POST['sex'];
$address = $_POST['address'];

echo "Thank you for registering with Laundreal Auto!!";

$servername = "localhost";
$username = "root";
$password = "";
$dbname = "laundromat";

// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);
// Check connection
if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}

$sql = "INSERT INTO registration (first_name, last_name, id_no, date_of_birth,email,phone,sex, address_home,date_registration)
VALUES ('$fname', '$lname', '$id','$dob','$email','$phone','$sex','$address',now())";

if (mysqli_query($conn, $sql)) {
  echo "New record created successfully";
} else {
  echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}

mysqli_close($conn);
?>
