url = 'https://hellosalut.stefanbohacek.dev/?lang=fr'
$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
    $('#hello').text(data.hello);
});