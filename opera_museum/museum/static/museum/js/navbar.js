$(document).ready(function () {
    $("#like").click(
        function () {
            alert("okok");
            var like = document.getElementById("like");
            var obj = like.nextElementSibling();
            var entryId = this.parents('div').attr("entryId");
            var myData = "entryId=" + entryId;

            $.ajax({
                type: "post",
                url: "/like_entry",
                dataType: "text",
                data: myData,
                success: function (result) {
                    var num = parseInt(obj.text());
                    obj.test(num + 1);
                    console.log(num + 1);
                }

            });

            var num = parseInt(obj.text());
            obj.text(num + 1);

        }
    );
    $("#category a").mouseover(function () {
        $(this).addClass("current");
    });
    $("#category a").mouseout(function () {
        $(this).removeClass("current");
    });
});
