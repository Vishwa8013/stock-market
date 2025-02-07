const signUpButtom=document.getElementById('signUpButton');
const signInButtom=document.getElementById('signInButton');
const signInForm=document.getElementById('signIn');
const signUpForm=document.getElementById('signUp');

signUpButtom.addEventListener('click',function(){
    signInForm.style.display="none";
    signUpForm.style.display="block";
})

signInButtom.addEventListener('click',function(){
    signUpForm.style.display="none";
    signInForm.style.display="block";
})



