/**
 * Created by maxencecoulibaly on 6/27/17.
 */

$(function(){

    $('.video-row-link').click(function() {
        window.location = $(this).find('.link').attr('href');
    })

});



