
$(function () {

        var $button = $('#login-button-styled');

        $button.click(function(){
                $('#login-email').val($('#login-email-styled').val());
                $('#login-password').val($('#login-password-styled').val());
                console.log('button 1 click');
                $('.login-button').click(); 
                return false;
        });

});