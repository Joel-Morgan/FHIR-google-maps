$("#filterselect").change(function() {
    if ($(this).val() === "Address Range") {
        $("#latitude").show()
        $("#longitude").show()
        $("#latitude").attr('required','');
        $("#longitude").attr('required','');
        $("#latitude").attr('data-error', 'This field is required.');
        $("#longitude").attr('data-error', 'This field is required.');
    } else {
        $("#latitude").hide()
        $("#longitude").hide()
        $("#latitude").removeAttr('required','');
        $("#longitude").removeAttr('required','');
        $("#latitude").removeAttr('data-error');
        $("#longitude").removeAttr('data-error');

    }
});
$("#filterselect").trigger("change");