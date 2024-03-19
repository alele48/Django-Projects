var enButton= document.querySelector("#en");
var mhButton= document.querySelector("#mh");
var textEng = document.querySelectorAll(".en");
var textMar = document.querySelectorAll(".mh");
var aShadow = document.querySelector("#a-shadow");
var aHeading = document.querySelector("#a-heading");

mhButton.addEventListener("click", function(){

  for(i=0;i<textEng.length;i++){
    textEng[i].style.display = 'none';
  }

  for(i=0;i<textMar.length;i++){
    textMar[i].style.display = "block";
  }

  aShadow.textContent = "Kojjela";
  aHeading.textContent = "Kojjela";

})

enButton.addEventListener("click", function(){

  for(i=0;i<textMar.length;i++){
    textMar[i].style.display = "none";
  }

  for(i=0;i<textMar.length;i++){
    textEng[i].style.display = "block";
  }

  aShadow.textContent = "Announcement";
  aHeading.textContent = "Announcement";

})
