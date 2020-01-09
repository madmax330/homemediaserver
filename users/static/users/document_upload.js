/**
 * Created by maxencecoulibaly on 6/12/17.
 */



$(function () {

    $('.upload-document').click(function () {
        $('#documentupload').click();
    });

    $('#documentupload').bind('fileuploadsubmit', function (e, data) {
        let name = $('#document_name').val();
        let group = $('#document_group').val();
        let csrf = $('input[name="csrfmiddlewaretoken"]').val();
        data.formData = {csrfmiddlewaretoken: csrf, name: name, group: group};
        if(!(data.formData.csrfmiddlewaretoken && data.formData.group)){
            display_message('Document group cannot be left empty.', 'danger');
            return false
        }
    });

    $('#documentupload').fileupload({
        dataType: 'json',

        start: function (e) {
            $('.document-progress-container').removeClass('hidden');
        },

        stop: function (e) {
            $('.document-progress-container').addClass('hidden');
        },

        progressall: function (e, data) {
            let progress = parseInt(data.loaded / data.total * 100, 10);
            let strProgress = progress + "%";
            let pb = $(".document-progress-bar");
            pb.css({"width": strProgress});
            pb.text(strProgress);
        },

        done: function (e, data) {
            if (data.result.is_valid) {
                location.reload();
            }
            else {
                display_message(data.result.error, 'danger');
            }
        }
    });

});



