let btnlog = document.querySelector(".login-btn");
let blkscn = document.querySelector(".overlay");
let btnsign =document.querySelector(".signup-btn");
let nxtbtn = document.querySelector(".next");

btnlog.addEventListener("click", showloginform);
blkscn.addEventListener("click", closeform);
btnsign.addEventListener("click", showsignupform);
nxtbtn.addEventListener("click", shownextsignup);



function closeform(){
    document.querySelector(".overlay").classList.remove("overlay-nt");
    document.querySelector(".login-form").classList.remove("login-form-after-click");
    document.querySelector(".signup-form").classList.remove("signup-form-after-click");
    document.querySelector(".signup-form-nxt").classList.remove("signup-form-nxt-ka-nxt");
}

function showloginform(){
    document.querySelector(".overlay").classList.add("overlay-nt");
    document.querySelector(".login-form").classList.add("login-form-after-click");
}

 function showsignupform(){
    document.querySelector(".overlay").classList.add("overlay-nt");
    document.querySelector(".signup-form").classList.add("signup-form-after-click");
}

function shownextsignup(){ //signup
    document.querySelector(".signup-form").classList.remove("signup-form-after-click");
    document.querySelector(".signup-form-nxt").classList.add("signup-form-nxt-ka-nxt");
}