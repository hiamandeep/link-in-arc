function ValidateSize(file) {
    var FileSize = file.files[0].size / 1024 / 1024; // in MB
    if (FileSize > 3) {
        alert('File size exceeds 3 MB');
        $(file).val(''); //for clearing with Jquery
    } else {

    }
}

document.getElementById("id_docfile").setAttribute("onchange", "ValidateSize(this)");