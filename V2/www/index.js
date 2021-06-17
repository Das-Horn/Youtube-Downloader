var mp3State = false;
var currentTitle = "Random Song";
var currentThumbnailURL = "";

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

function download(){
    const queueBox = '<div class="queue-box"><p class="Text queue-text">'+currentTitle+'</p><p class="Text queue-Status">Downloading</p><div class="progress-cont"><div class="progress-bar"><p class="Text progress-text">0%</p></div></div></div>';
    const container = document.getElementById("queue-cont");
    container.innerHTML += queueBox;
}

function updateMeta(){
    const link = document.getElementById("link").value;
    getVidData(recieveMeta,link);
}
function recieveMeta(data){
    currentTitle = data[0];
    currentThumbnailURL = data[1];
}