function Validation() {
    const inpObj = document.getElementById("email");
    const inpObj2 = document.getElementById("phone");
    if (!inpObj.checkValidity()) {
        document.getElementById("demo").innerHTML = "Your Email is not valid, please fill it again";
    }
    if (!inpObj2.checkValidity()) {
        document.getElementById("demo2").innerHTML = "Your Phone number is not valid, please fill it again";
    }
}
