$('.cell input').focusin(function() {
    $(this).hide();
    $('.cell textarea').show();
    setTimeout(function(){
        $('.cell textarea').focus();
    }, 0);
});​