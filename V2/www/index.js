var mp3State = false;
var currentTitle = "Random Song";
var currentThumbnailURL = "";
var validDownload = false;

window.onload(setProgressionFunction)

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

function setProgressionFunction(){
    setProg(downloadProgress)
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
    validDownload = false;
    downloadButtonCheck();
    const queueBox = '<div class="queue-box"><p class="Text queue-text">'+currentTitle+'</p><p class="Text queue-Status">Downloading</p><div class="progress-cont"><div class="progress-bar"><p class="Text progress-text">0%</p></div></div></div>';
    const container = document.getElementById("queue-cont");
    container.innerHTML = queueBox + container.innerHTML;
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

function downloadProgress(prog){
    console.log("updating progress:\t"+prog);
    const container = document.getElementsByClassName("queue-box")[0];
    if(prog == 100){
        container.children[1].innerHTML = "Complete"; 
        validDownload = true;
        downloadButtonCheck();
    }else if(prog == 65){
        container.children[1].innerHTML = "Post processing Audio"; 
    }else if(prog == 75){
        container.children[1].innerHTML = "Downloading Video"; 
    }else if(prog == 80){
        container.children[1].innerHTML = "Post processing Video"; 
    }
    container.children[2].children[0].style.width = prog+"%";
    container.children[2].children[0].children[0].innerHTML = prog+"%";
}