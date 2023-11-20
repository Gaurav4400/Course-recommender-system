function elemTarget(e) {
	e = e || window.event;
	/*e.preventDefault();*/
	return e.target;
}

  document.addEventListener("click", function(e) {
	let elem = elemTarget(e);
    
	if (elem.id == 'buttonDownload') {
    saveText();
	}
});

function saveText() {
	let data = document.querySelector('#texTareaI').value;
	let file = 'data-' + Date.now() + '.txt';

	let link = document.createElement('a');
	link.download = file;
	let blob = new Blob(['' + data + ''], {
		type: 'text/plain'
	});
	link.href = URL.createObjectURL(blob);
	link.click();
	URL.revokeObjectURL(link.href);
}