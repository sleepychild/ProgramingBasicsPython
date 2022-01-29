let wiki_frame = document.getElementsByName("wiki_frame")[0];
let learn_more = document.getElementById("learn_more");

wiki_frame.onload = ()=>{
    wiki_frame.hidden = false;
    learn_more.remove();
}
