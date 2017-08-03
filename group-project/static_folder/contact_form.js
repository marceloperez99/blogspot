var submit;
var form;
  var link;
  var sujet;
  var nom;
  var email;
  var message;

document.addEventListener("DOMContentLoaded", function(event) {
  submit = document.getElementById('submit_link');

  submit.onclick = function () {

    sujet = document.getElementById('contact_sujet').value;
    nom = document.getElementById('contact_nom').value;
    email = document.getElementById('contact_email').value;
    message = document.getElementById('contact_message').value;
    link = "mailto:christiwright0@gmail.com";
    link += "?subject=" + sujet;
    link += "&cc=" + nom + " <" + email + ">";
    link += "&body=" + message;

    submit.href = link;
  }
})
