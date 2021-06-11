var vidid = "HSvoF8IfzRY";
function getYouTubeInfo() {
$.ajax({
url: "http://gdata.youtube.com/feeds/api/videos/"+vidid+"?v=2&alt=json&orderby=published&prettyprint=true",
dataType: "jsonp",
success: function (data) {parseresults(data)}
});
}
function parseresults(data) {
var ytvtit = data.entry.title.$t;
var ytvcat = data.entry.media$group.media$category[0].label;
var ytvpub = data.entry.published.$t.substr( 0, 10 );
var ytvath = data.entry.author[0].name.$t;
var ytvatl = data.entry.media$group.media$credit[0].$t;
var ytvdur = data.entry.media$group.yt$duration.seconds;
var ytvrta = data.entry.gd$rating.average.toFixed(1);
var ytvrtm = data.entry.gd$rating.max;
var ytvrtc = data.entry.gd$rating.numRaters;
var ytvlks = data.entry.yt$rating.numLikes;
var ytvdlk = data.entry.yt$rating.numDislikes;
var ytvvwc = data.entry.yt$statistics.viewCount;
var ytvfav = data.entry.yt$statistics.favoriteCount;
var ytvcmc = data.entry.gd$comments.gd$feedLink.countHint;
var ytvdes = data.entry.media$group.media$description.$t;
var ytvurl = 'https://www.youtube.com/watch?v='+vidid;
var ytvtmb0 = data.entry.media$group.media$thumbnail[0].url;
$('#ytvtitle').html(ytvtit);
$('#ytvcatgry').html(ytvcat);
$('#ytvpublish').html(ytvpub);
$('#ytvauthr').html('ytvath');
$('#ytvduration').html(ytvdur + ' Seconds' );
$('#ytvrtngavrg').html(ytvrta);
$('#ytvrtngmax').html(ytvrtm);
$('#ytvrtngcnt').html(ytvrtc);
$('#ytvlks').html(ytvlks);
$('#ytvdislks').html(ytvdlk);
$('#ytvviewcount').html(ytvvwc);
$('#ytvfavcount').html(ytvfav);
$('#ytvthumb').html('');
$('#ytvcomment').html(ytvcmc);
$('#ytvdescription').html(ytvdes);
$('#ytvurl').html('Watch on YouTube');
$('#ytvply').html('');
}
$(document).ready(function () {
getYouTubeInfo();
});