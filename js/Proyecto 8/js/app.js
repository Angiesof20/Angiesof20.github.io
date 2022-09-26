function validaCampos(){
    var formulario;
    formulario=document.formUser;

    if(formulario.user.value==""){
    document.getElementById("validaUser").innerHTML="¡Por favor escriba su nombre!"
    formulario.user.focus();
    return false;
}
else{
    document.getElementById("validaUser").innerHTML=""
}
  if(formulario.email.value==""){
    document.getElementById("validaEmail").innerHTML="¡Por favor escriba su E-mail!"
    formulario.email.focus();
    return false;
  }
  else{
    document.getElementById("validaEmail").innerHTML=""
  }

  if(formulario.password.value==""){
    document.getElementById("validaPassword").innerHTML="¡Por favor Escriba su Contraseña!"
    formulario.password.focus();
    return false;
  }
  else{
    document.getElementById("validaPassword").innerHTML=""
  }

  if(formulario.passwordC.value==""){
    document.getElementById("validaPasswordC").innerHTML="¡Por favor Confirme su Contraseña"
    formulario.password.focus();
    return false;
  }
  else{
    document.getElementById("validaPasswordC").innerHTML=""
  }
  
formulario.submit();
}