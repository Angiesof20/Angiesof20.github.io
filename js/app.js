function validaCampos(){
    var formulario;
    formulario=document.formUser;
    //valida el campo usuario
    if (formulario.user.value != "Angie20"  ) {
        //valida si el campo esta vacio
        document.getElementById("validaUser").innerHTML="Favor escribir el usuario";
        //se posiciona en el campo user
        formulario.user.focus();
        return false;
        
    }else{
        document.getElementById("validaUser").innerHTML="";
    }
    // valida el campo password
    if (formulario.password.value != "1103739573") {
        //valida si el campo esta vacio
        document.getElementById("validaPassword").innerHTML="Favor escribir su contraseña";
        //se posiciona en el campo password
        formulario.password.focus();
        return false;
        
    }else{
        document.getElementById("validaPassword").innerHTML="";
    }

    

    formulario.submit();

}