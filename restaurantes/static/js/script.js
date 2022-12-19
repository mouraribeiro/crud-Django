$(document).ready(function(){
    
    var deleteBtn = $('.delete-btn');
   
    

    $(deleteBtn).on('click', function(e){

        e.preventDefault();
        var result = confirm('Quer deletar esse restaurante? ');
        console.log(result)

        var delLink = $(this).attr('href');
        console.log(delLink)
        
        if(result){
            window.location.href = delLink;
        }
        
    });


    
});
     

    