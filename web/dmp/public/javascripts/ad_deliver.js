$(function(){
  var adDeliver = {
    init: function(){
      this.fetchAd();
    },
    addModel: function(){
      
    },
    bindEvents: function(){

    },
    closeModal: function(){

    },
    showModal: function(){

    },
    fetchAd: function(){
       $.ajax({
         url: "/ad_deliver/fetch_ads",
         type: "POST",
         dataType: "json",
         data:{
           "text": this.fetchAllHeadline(),
           "authenticity_token": $("#authenticity_token").val()
         }
       });
    },
    fetchAllHeadline: function(){
      var $hTags = $("h1, h2, h3, h4, h5, h6"); 
      var $h = [];
      $.each($hTags, function(_, $hTag){
        $h.push($hTag.innerText);
      });
      return $h.join(" ");
    }
  }

  adDeliver.init();
});
