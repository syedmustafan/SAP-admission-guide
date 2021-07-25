
 $(document).ready(function() {
     $("#text").focus(function () {
         $(".cancel").attr("hidden",false);
         $(".ask").attr("hidden", false);


     });
     $(".cancel").click(function () {
         $("#text").val('');
          $(".cancel").attr("hidden",true);
         $(".ask").attr("hidden", true);
     });

      var date = new Date();

    var day = date.getDate();
    var month = date.getMonth() + 1;
    var year = date.getFullYear();

    if (month < 10) month = "0" + month;
    if (day < 10) day = "0" + day;

    var today = year + "-" + month + "-" + day;
    $("#theDate").attr("value", today);

    
    function showCommentSection(){
        $(".CommSec").attr("hidden",false)
    }
    
    
    
    
 });

