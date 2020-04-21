/**
 * Created by brunopiaggio on 4/17/20.
 */

$(document).ready(function () {

    $('.btn-default').click(function () {
        $('div').removeClass('btn-selected');
        $(this).addClass('btn-selected')
    })

})