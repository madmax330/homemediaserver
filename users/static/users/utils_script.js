/**
 * Created by maxencecoulibaly on 3/16/17.
 */


function display_message(msg, code){
    let msgs = $('.messages');

    let html = `<div class="alert alert-dismissable alert-${code}">
                    <a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>
                    <p>${msg}</p>
                </div>`;

    msgs.append(html);
    $('html, body').animate({
        scrollTop: $('body').offset().top
    }, 'fast');
}

$(function(){

    $('.edit-video').click(function( event ) {
        event.preventDefault();
        let parent = $(this).parents('.video-row');
        $('#edit-video-form').attr('action', $(this).attr('href'));
        $('#edit_video_name').val(parent.find('.name').html().toString().trim());
        $('#edit_video_type').val(parent.find('.type').html().toString().trim());
        $('#edit-video-modal').modal('show');
    });

    $('.edit-picture').click(function ( event ) {
        event.preventDefault();
        let parent = $(this).parents('.picture-row');
        $('#edit-picture-form').attr('action', $(this).attr('href'));
        $('#edit_picture_description').val(parent.find('.description').html().toString().trim());
        $('#edit-picture-modal').modal('show');
    });

    $('.edit-document').click(function ( event ) {
        event.preventDefault();
        let parent = $(this).parents('.document-row');
        $('#edit-document-form').attr('action', $(this).attr('href'));
        $('#edit_document_name').val(parent.find('.name').html().toString().trim());
        $('#edit_document_group').val(parent.find('.group').html().toString().trim());
        $('#edit-document-modal').modal('show');
    });

});


