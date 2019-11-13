document.getElementById("cameraTakePicture").addEventListener 
   ("click", cameraTakePicture); 

// var name = document.getElemntById("name").value ;
// var email = document.getElementById("email").value ;

   function cameraTakePicture() { 
   navigator.camera.getPicture(onSuccess, onFail, {  
      quality: 50, 
      saveToPhotoAlbum: 1,
      destinationType: Camera.DestinationType.DATA_URL 
   });  
   
   function onSuccess(imageData) { 
      var name = document.getElementById("name").value ;
      var email = document.getElementById("email").value ;
      var image = document.getElementById('myImage'); 
      image.src = "data:image/jpeg;base64," + imageData; 
      console.log(imageData);
      console.log("\n");
      console.log("data:image/jpeg;base64," + imageData);

      $.post("https://shellkore.serveo.net/", { data : imageData },function(output, status){
      
   
    console.log(output);
    console.log(typeof(output));


      document.getElementById("id-d").innerHTML = output;


     
   

    });


    
   }  
   
   function onFail(message) { 
      alert('Failed because: ' + message); 
   } 
}


function submit() {

onSuccess() ;

  console.log(name);
  console.log(email);
}