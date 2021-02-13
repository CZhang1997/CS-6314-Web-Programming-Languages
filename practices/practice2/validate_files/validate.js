window.onload = function () {
  //there will be one span element for each input field
  // when the page is loaded, we create them and append them to corresponding input element
  // they are initially empty and hidden

  var span1 = document.createElement("span");
  var span2 = document.createElement("span");
  var span3 = document.createElement("span");
  span1.style.display = "none"; //hide the span element
  span2.style.display = "none"; //hide the span element
  span3.style.display = "none"; //hide the span element
  span1.innerText = "Please Enter a valid email address: abc@def.xyz";
  span2.innerText = "Password should have at least six characters";
  span3.innerText = "Passwords do not match";

  var email = document.getElementById("email");
  var pwd = document.getElementById("pwd");
  var confirm = document.getElementById("confirm");
  var form = document.getElementById("myForm");
  email.parentNode.appendChild(span1);
  pwd.parentNode.appendChild(span2);
  confirm.parentNode.appendChild(span3);

  function validateEmail() {
    return /[a-z0-9._%+-]+@[a-z0-9.-]+.[a-z]{2,}$/.test(email.value);
  }
  function validatePassword() {
    return pwd.value.length >= 6;
  }
  function validateConfirm() {
    return validatePassword() && pwd.value === confirm.value;
  }

  function reset() {
    email.classList.remove("error");
    pwd.classList.remove("error");
    confirm.classList.remove("error");
    span1.innerText = "Please Enter a valid email address: abc@def.xyz";
    span1.style.display = "none";
    span2.style.display = "none";
    span3.style.display = "none";
  }

  form.onsubmit = (e) => {
    var emailValidator = validateEmail();
    var pwdValidator = validatePassword();
    var confirmValidator = validateConfirm();

    if (!emailValidator) {
      email.classList.add("error");
      span1.innerText = "Not a valid email address. Please re-enter!";
      span1.style.display = "block";
    }
    if (!pwdValidator) {
      pwd.classList.add("error");
      span2.style.display = "block";
    }
    if (!confirmValidator) {
      span3.style.display = "block";
      confirm.classList.add("error");
    }
    if (!(emailValidator && pwdValidator && confirmValidator)) {
      e.preventDefault();
    }
  };

  email.onfocus = function () {
    reset();
    span1.style.display = "block";
  };
  pwd.onfocus = function () {
    reset();
    span2.style.display = "block";
  };
  confirm.onfocus = function () {
    reset();
    //   span3.style.display = "block";
  };

  email.onblur = function () {
    span1.style.display = "none";
  };
  pwd.onblur = function () {
    span2.style.display = "none";
  };
  //   confirm.onblur = function () {
  //     span3.style.display = "none";
  //   };
};
