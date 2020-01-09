/**
 * Created by maxencecoulibaly on 6/12/17.
 */



$(function () {

    let p_jqXHR = [];

    $('.upload-picture').click(function () {
        $('#pictureupload').click();
    });

    $('#pictureupload').fileupload({
        dataType: 'json',

        start: function (e) {
            $('.picture-progress-container').removeClass('hidden');
        },

        stop: function (e) {
            $('.picture-progress-container').addClass('hidden');
        },

        progressall: function (e, data) {
            let progress = parseInt(data.loaded / data.total * 100, 10);
            let strProgress = progress + "%";
            let pb = $(".picture-progress-bar");
            pb.css({"width": strProgress});
            pb.text(strProgress);
        },

        done: function (e, data) {
            if (data.result.is_valid) {
                location.reload();
            }
            else {
                display_message('Upload failed, try again...', 'danger');
            }
        }
    }).bind('fileuploadsubmit', function (e, data) {
        let description = $('#picture_description').val();
        let csrf = $('input[name="csrfmiddlewaretoken"]').val();
        data.formData = {csrfmiddlewaretoken: csrf, occasion: description};
        if(!(data.formData.csrfmiddlewaretoken && data.formData.occasion)){
            display_message('Picture description cannot be left empty.', 'danger');
            return false
        }
        display_message('Starting upload...', 'info');
    }).on('fileuploadadd', function (e, data) {
        p_jqXHR.push(data);
    });

    /*
    *       MULTIPLE
     */

    $('.upload-multiple-pictures').click(function () {
        $('#multiplepictureupload').click();
    });

    $('#multiplepictureupload').fileupload({
        dataType: 'json',
        sequentialUploads: true,

        start: function (e) {
            $('.picture-progress-container').removeClass('hidden');
        },

        stop: function (e) {
            $('.picture-progress-container').addClass('hidden');
        },

        progressall: function (e, data) {
            let progress = parseInt(data.loaded / data.total * 100, 10);
            let strProgress = progress + "%";
            let pb = $(".picture-progress-bar");
            pb.css({"width": strProgress});
            pb.text(strProgress);
        },

        done: function (e, data) {
            if (data.result.is_valid) {
                display_message(data.result.name + ' uploaded successfully.', 'success');
            }
            else {
                display_message('Upload failed, try again...', 'danger');
            }
        }
    }).bind('fileuploadsubmit', function (e, data) {
        let description = $('#picture_description').val();
        let csrf = $('input[name="csrfmiddlewaretoken"]').val();
        data.formData = {csrfmiddlewaretoken: csrf, occasion: description};
        if(!(data.formData.csrfmiddlewaretoken && data.formData.occasion)){
            display_message('Picture description cannot be left empty.', 'danger');
            return false
        }
        display_message('Starting upload...', 'info');
    }).on('fileuploadadd', function (e, data) {
        p_jqXHR.push(data);
    });

    $('.cancel-picture-uploads').click(function () {
        for(let i=0; i<p_jqXHR.length; i++){
            p_jqXHR[i].abort();
        }
        let p = $('.picture-progress-container');
        if(!p.hasClass('hidden')){
            p.addClass('hidden');
        }
        display_message('All picture uploads have been canceled.', 'info');
    });

});



