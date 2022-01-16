
let title = document.getElementsByTagName('title')[0];
let title_text = title.innerText;
let underline = '~';
let lj = 0;
let rj = 10;
let direction = 1;

setInterval(()=>{

    if ( lj == 0 ){
        direction = 1;
    }else if (rj == 0){
        direction = -1;
    }

    title.innerText = `${underline.repeat(lj)}${title_text}${underline.repeat(rj)}`;
    
    lj = lj + direction;
    rj = rj - direction;

},1000);
