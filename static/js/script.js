const hamburger = document.querySelector('.hamburger input');
const nav = document.querySelector('nav ul');

hamburger.addEventListener('click', function(){
    nav.classList.toggle('slide');
});

function previewImageUpdate() {
    document.getElementById("image-preview-update").style.display = "block";
    document.getElementById("image-preview-update").style.margin = "auto";
    const oFReader = new FileReader();
    oFReader.readAsDataURL(document.getElementById("fileUpload").files[0]);

    oFReader.onload = function(oFREvent) {
      document.getElementById("image-preview-update").src = oFREvent.target.result;
    };
  };