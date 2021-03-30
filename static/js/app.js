let container = document.querySelector(".container");
let text = document.getElementById("text");

let totalTime = 10000;
//found the formula in google

let breatheTime = (totalTime/5)*2
let holdTime = totalTime/5;

animateScreen()
function animateScreen(){
    text.innerHTML = "Breathe in";
    container.className = "container grow";
    setTimeout(()=> {
        text.innerText = "Hold"
        setTimeout(()=>{
            text.innerText = "Breathe out";
            container.className = "container shrink"
        },holdTime)


    },breatheTime)
}
setInterval(animateScreen,totalTime)