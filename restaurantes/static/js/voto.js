
let likebtn = document.querySelector('#likebtn')


 var voto = 0;
  function votou() {
      voto += 1;
     document.getElementById("clicks").innerHTML = voto;
 }



 





/*
se a pessoa clicar, excluir botao de votar - 1 voto por pessoa

se o dia é igual ao dia atual adiciona o voto a lista
se o dia é diferente, lista deve ser vazia

$(document).ready(function(){
  $("#vote-End").click(function(){
    $(this).fadeOut();
  });
});

*/
$(document).ready(function(){
  horas = new Date().getHours()
  hora_limite = 11
 



   
  console.log(horas)
});
horas = new Date().getHours()
  hora_limite = 11
  if (horas < hora_limite){
    document.getElementById('vote-end').innerText = "Votação aberta"
  }else{
    document.getElementById('vote-end')}