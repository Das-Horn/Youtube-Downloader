var mp3State = false;
var currentTitle = "Random Song";
var currentThumbnailURL = "";
var validDownload = false;

function mp3toggle(){
    const tgl = document.getElementById("MP3-button");
    if(mp3State){
        mp3State = false;
        tgl.style.backgroundColor = "var(--deactive-color)";
    }else {
        mp3State = true;
        tgl.style.backgroundColor = "var(--active-color)";
    }
}

function downloadButtonCheck(){
    const dlButton = document.getElementById('down-button');
    if(validDownload){
        dlButton.style.backgroundColor = "var(--deactive-color)";
        dlButton.disabled = false;
    }else{
        dlButton.style.backgroundColor = "var(--NA-color)";
        dlButton.disabled = true;
    }
}

function download(){
    const queueBox = '<div class="queue-box"><p class="Text queue-text">'+currentTitle+'</p><p class="Text queue-Status">Downloading</p><div class="progress-cont"><div class="progress-bar"><p class="Text progress-text">0%</p></div></div></div>';
    const container = document.getElementById("queue-cont");
    container.innerHTML += queueBox;
    downloadVideo(NaN,mp3State);
}

function updateMeta(){
    const link = document.getElementById("link").value;
    getVidData(recieveMeta,link);
}

function recieveMeta(data){
    if(data[0] != 0){
        currentTitle = data[0];
        currentThumbnailURL = data[1];
        document.getElementById("thumbnail").src = currentThumbnailURL;
        document.getElementById("video-title").innerHTML = currentTitle;
        validDownload = true;
        downloadButtonCheck();
    }else {
        validDownload = false;
        downloadButtonCheck();
    }
}