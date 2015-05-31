$(document).ready(function () {
    $("#like").click(

    );
    $("#category a").mouseover(function () {
        $(this).addClass("current");
    });
    $("#category a").mouseout(function () {
        $(this).removeClass("current");
    });
});
