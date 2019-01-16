(function($){
    $(function(){
      $(document).ready(function(){
        $('select').material_select();
        //$('select').attr("class", "browser-default")

      });
      
      $(document).ready(function(){
        $('.sidenav').sidenav();
      });

     
    }); // end of document ready

    document.getElementById("uploadBtn").onchange = function () {
      document.getElementById("uploadFile").value = this.value;
    };
  
  
  })(jQuery); // end of jQuery name space