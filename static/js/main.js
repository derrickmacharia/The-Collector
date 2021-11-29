function shareImage(pic_url) {
    navigator.clipboard.writeText(pic_url)
        .then(function onSuccess() {
            alert('Successfully copied image url to clipboard');
        })
        .catch(function onError() {
            alert('unable to paste to clipboard')
        })
}