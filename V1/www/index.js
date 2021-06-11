var Theme = 1


function LoadingChecks(TxtStr, Fin){
    const Screens = document.getElementsByClassName('Screen-Div');
    if (Fin == true) {
        Screens[0].style.top = "-100%";
        Screens[1].style.visibility = "visible";

        return;
    }
    LDTxt = document.getElementById('Loading-Text');
    LDTxt.innerHTML = TxtStr;
    return;
}

function TestChange(){
    Target = document.getElementById('VidTitle')
    Title = getVideoID();
    if(Title != 'Please enter a valid Url'){
        getVidTitle(Title);
        setThumbnail(Title);
    }
}

function getVideoID(){
    var url = document.getElementById("URL-Input").value;
    console.log(url)
    var regExp = /^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*/;
    var match = url.match(regExp);
    return (match&&match[7].length==11)? match[7] : "Please enter a valid Url";
}

function setThumbnail(VidID){
    Div = document.getElementById('Thumbnail');
    imgURL = 'https://img.youtube.com/vi/'+VidID+'/0.jpg'
    Div.style.backgroundImage = 'url('+imgURL+')';
    return;
}

async function getVidTitle(){
    var url = document.getElementById("URL-Input").value;
    var Title = await eel.getYTTitle(url)();
    console.log(Title)
    document.getElementById('VidTitle').innerHTML = Title;
    return;
}

function DLVideo(mp3){
    var url = document.getElementById("URL-Input").value;
    var Vid = document.getElementById("Vid-Del-Check").checked;
    if(Vid == true){
        var Vnum = 1;
    }else{
        var Vnum = 0;
    }
    if(mp3 == true){
        eel.setUrl(url,1,Vnum);
    }else{
        eel.setUrl(url,0,Vnum);
    }
}

function CSSVarChange(){
    const r = document.querySelector(':root');
    if(Theme == 0){
        r.style.setProperty('--Text-Color', '#ffffff');
        r.style.setProperty('--Background-Gradient', 'linear-gradient(0deg, rgba(0,0,0,1) 0%, rgba(51,51,51,1) 54%, rgba(79,79,79,1) 100%)');
        Theme = 1;
    }else{
        r.style.setProperty('--Text-Color', '#ffffff');
        r.style.setProperty('--Background-Gradient', 'linear-gradient(0deg, rgba(255,105,97,1) 0%, rgba(200,105,97,1) 54%, rgba(255,255,255,1) 100%)');
        Theme = 0;
    }
}

function LoadingScreen(state){
    const LS = document.getElementById("progress-background");
    if(state == 1){
        LS.style.bottom = "0%";
    } else {
        LS.style.bottom = "-100%";
    }
}

function setProgressBar(P){
    const PBar = document.getElementById("current-progress");
    const PText = document.getElementById("progress-text");

    console.log("Current Progress:"+P);
    PBar.style.width = P;
    PText.innerHTML = P;
}