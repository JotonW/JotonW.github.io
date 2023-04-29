$(document).ready(function(){
    $(document).off('click.bs.dropdown.data-api');
});

$(document).ready(function(){
    dropdownOpen();//璋冪敤
});
/**
 * 榧犳爣鎮仠灏卞睍寮€瀛愯彍鍗�
 */
function dropdownOpen() {

    var $dropdownLi = $('li.dropdown');

    $dropdownLi.mouseover(function() {
        $(this).addClass('open');
    }).mouseout(function() {
        $(this).removeClass('open');
    });
}