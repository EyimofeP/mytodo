$(document).ready(function(){
     // Init Carousel
     $('.carousel').carousel();

     // Init Carousel Slider
     $('.carousel.carousel-slider').carousel({fullWidth:true});

     // Fire off toast
     //Materialize.toast('Hello World', 3000);

     // Init Slider
     $('.slider').slider();

     // Init Modal
     $('.modal').modal();

     // Init Sidenav  
     $('.sidenav').sidenav();
});

/*
var setTheme = localStorage.getItem('theme')
console.log('theme:', setTheme)

if (setTheme == null) {
    swapStyle('style.css')
} else {
    swapStyle(setTheme)
}

function swapStyle(sheet) {
    document.getElementById('mystylesheet').href = sheet
    localStorage.setItem('theme', sheet)
}
*/

function toggle(){
     var el = document.getElementById("mystylesheet");
     if (el.href.match("style.css")) {
          el.href = "dark.css";
     }
     else {
          el.href = "style.css"
     }
}