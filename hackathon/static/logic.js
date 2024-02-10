let btnlog = document.querySelector(".login-btn");
let blkscn = document.querySelector(".overlay");
let btnsign =document.querySelector(".signup-btn");
let nxtbtn = document.querySelector(".next");
let sdOTPbtn =document.querySelector(".sendotp");

btnlog.addEventListener("click", showloginform);
blkscn.addEventListener("click", closeform);
btnsign.addEventListener("click", showsignupform);
// nxtbtn.addEventListener("click", shownextsignup);       removed this btn!

sdOTPbtn.addEventListener("click", () => {
    document.querySelector(".otp-popup").classList.add("otp-popup-hide");
    document.querySelector(".signup-form").classList.remove("signup-form-after-click")
});


function closeform(){
    document.querySelector(".overlay").classList.remove("overlay-nt");
    document.querySelector(".login-form").classList.remove("login-form-after-click");
    document.querySelector(".signup-form").classList.remove("signup-form-after-click");
    document.querySelector(".signup-form-nxt").classList.remove(".signup-form-after-click");
}

function showloginform(){
    document.querySelector(".overlay").classList.add("overlay-nt");
    document.querySelector(".login-form").classList.add("login-form-after-click");
}

 function showsignupform(){
     document.querySelector(".overlay").classList.add("overlay-nt");
    document.querySelector(".signup-form").classList.add("signup-form-after-click");
}

// function shownextsignup(){ //signup (not in use right now)
//     // document.querySelector(".signup-form").classList.remove(".first-page-signup-page");
//     document.querySelector(".first-page-signup-page").classList.add("first-page-aftr-clik");
//     // document.querySelector(".signup-form").classList.add(".sec-page-signup-form");
//     document.querySelector(".sec-page-signup-form").classList.add("signup-form-nxt-ka-nxt");
// }