$(document).ready(function () {
    $.get("/api/v1.0/index", function (resp) {
        alert(resp.errno)
        if (resp.errno == "0") {
            var arts = resp.data;
            var html = template("art-tmpl", {arts: arts})
            $("#art-id").html(html)
        } else {
            alert(resp.errmsg);
        }
    })
})