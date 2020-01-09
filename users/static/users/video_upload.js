/**
 * Created by maxencecoulibaly on 6/12/17.
 */



$(function () {

    let jqXHR = [];

    $('.upload-video').click(function () {
        $('#videoupload').click();
    });

    $('#videoupload').fileupload({
        dataType: 'json',

        start: function (e) {
            $('.video-progress-container').removeClass('hidden');
        },

        stop: function (e) {
            $('.video-progress-container').addClass('hidden');
        },

        progressall: function (e, data) {
            let progress = parseInt(data.loaded / data.total * 100, 10);
            let strProgress = progress + "%";
            let pb = $(".video-progress-bar");
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
        let name = $('#video_name').val();
        let t = $('#video_type').val();
        let csrf = $('input[name="csrfmiddlewaretoken"]').val();
        data.formData = {csrfmiddlewaretoken: csrf, name: name, type: t};
        if(!(data.formData.csrfmiddlewaretoken && data.formData.type)){
            display_message('Video type cannot be left empty.', 'danger');
            return false
        }
        display_message('Starting upload...', 'info');
    }).on('fileuploadadd', function (e, data) {
        jqXHR.push(data);
    });

    /*
    *       MULTIPLE
     */

    $('.upload-multiple-videos').click(function () {
        $('#multiplevideoupload').click();
    });

    $('#multiplevideoupload').fileupload({
        dataType: 'json',
        sequentialUploads: true,

        start: function (e) {
            $('.video-progress-container').removeClass('hidden');
        },

        stop: function (e) {
            $('.video-progress-container').addClass('hidden');
        },

        progressall: function (e, data) {
            let progress = parseInt(data.loaded / data.total * 100, 10);
            let strProgress = progress + "%";
            let pb = $(".video-progress-bar");
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
        let t = $('#video_type').val();
        let csrf = $('input[name="csrfmiddlewaretoken"]').val();
        data.formData = {csrfmiddlewaretoken: csrf, type: t};
        if(!(data.formData.csrfmiddlewaretoken && data.formData.type)){
            display_message('Video type cannot be left empty.', 'danger');
            return false
        }
        display_message('Starting upload...', 'info');
    }).on('fileuploadadd', function (e, data) {
        jqXHR.push(data);
    });

    $('.cancel-video-uploads').click(function () {
        for(let i=0; i<jqXHR.length; i++){
            jqXHR[i].abort();
        }
        let v = $('.video-progress-container');
        if(!v.hasClass('hidden')){
            v.addClass('hidden');
        }
        display_message('All video uploads have been canceled.', 'info');
    });

});



