
let radioButtons = document.getElementsByName("emotion");
let checkedButton = null;

console.log(radioButtons);
let angry = document.getElementById("id_emotion_2");
let angryDiv = (angry.parentNode).parentNode;
angryDiv.classList.add('angry-div')
angry.style.display = 'none';


let happy = document.getElementById("id_emotion_0");
let happyDiv = (happy.parentNode).parentNode;
happyDiv.classList.add('happy-div');
happy.style.display = 'none';

let excited = document.getElementById("id_emotion_1");
let excitedDiv = (excited.parentNode).parentNode;
excitedDiv.classList.add('excited-div');
excited.style.display = 'none';


let sad = document.getElementById("id_emotion_3");
let sadDiv = (sad.parentNode).parentNode;
sadDiv.classList.add('sad-div');
sad.style.display = 'none';




radioButtons.forEach((button)=>{
    button.style.display = 'none';
});

radioButtons.forEach(button =>{
   button.addEventListener('change', function(){
     if(button.checked == true){
           switch(button.value){
           case 'happy':
                (this.parentNode).parentNode.classList.add('happy-active');
                excitedDiv.classList = "radio-field excited-div";
                sadDiv.classList = "radio-field sad-div";
                angryDiv.classList = "radio-field angry-div";


                
                break;
            case 'excited':
                (this.parentNode).parentNode.classList.add('excited-active');
                happyDiv.classList = "radio-field happy-div";
                sadDiv.classList = "radio-field sad-div";
                angryDiv.classList = "radio-field angry-div";
                break;
            case 'angry':
                (this.parentNode).parentNode.classList.add('angry-active');
                excitedDiv.classList = "radio-field excited-div";
                sadDiv.classList = "radio-field sad-div";
                happyDiv.classList = "radio-field happy-div";
                break;
            case 'sad':
                (this.parentNode).parentNode.classList.add('sad-active');
                excitedDiv.classList = "radio-field excited-div";
                happyDiv.classList = "radio-field happy-div";
                angryDiv.classList = "radio-field angry-div";
                break;
       }
   }
   
});
})
