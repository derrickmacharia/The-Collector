$(document).ready(function(){
    $(".button1").click(function(){
        $(".photo-details").show();
        $(".disciple").css("opacity", "0.1");
        $(".phot").html('<img src="{{ pic.image.url }}" alt=""">');
    });
});