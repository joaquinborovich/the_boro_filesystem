var loader_event = (event) => {
    let file = event.target.files[0];

    let fileNameSpan = '<span>> Selected file: </span> <span class="path">' + file.name + '</span>';

    let fileInputLabel = document.getElementById("file-input-label");
    fileInputLabel.innerHTML = fileNameSpan;
    fileInputLabel.classList.add("active");

    let formUploadSubmit = document.getElementById("file-upload")
    formUploadSubmit.setAttribute("action", "/")
    formUploadSubmit.setAttribute("method", "POST")
    formUploadSubmit.setAttribute("enctype", "multipart/form-data")
};


let fileInput = document.getElementById("file-input");
fileInput.addEventListener('change', loader_event);


