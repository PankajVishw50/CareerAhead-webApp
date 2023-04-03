// This script sets the width of password field equal to other fields in form

element1 = $('#username-input');
element2 = $('#password-input');
element1Width = element1.outerWidth( true );
element2.css('width', `${element1Width}px`);

console.log(element1Width)
console.log(element2.outerWidth( true ))
