var markInputs=document.getElementById("texts");//returns the new input fields that will be creating after getting the number of subjects from user
var finalMark=document.getElementById("Final mark");//returns the fianl grade
var totalSubs=document.getElementById("Num subjects");//Number of subjects
var number=0;
var total=0;


function NewField(){
  // Delete the old fields
  for(var i=0;i<number;i++){
    var input=document.getElementById(i);
    markInputs.removeChild(input);//returns the removed child node from the DOM but keeps it in the memory
    console.log("")
  }
  //reset number of fields to 0
  nummber=0;
  //create new fields
  for(var i=0;i<totalSubs.value;i++){
    var input = document.createElement("input");
    input.type = "number";
    input.name="mark";
    input.id=number;
    markInputs.appendChild(input);//add a node towards the end of the list
    number+=1;
  }


}
function gpa_calculate(){
  
  // deleting the previously displyed grade
  var final=document.getElementById('output')
  finalMark.removeChild(final);
  
  //flag variable to make sure that all values is less than 100
  var flag=-1;
  
  for(var i=0;i<number;i++){
    var texts=document.getElementById(i);
    total+=parseFloat(texts.value);
    if(parseFloat(texts.value)>100 || parseFloat(texts.value)<0 ){
      flag=0;
    }
  }
  Average=parseInt(total/number);
  var gpa;
  switch(parseInt((Average/10))*10){
    case 100:
      gpa='S';
      break;
    case 90:
      gpa='S';
      break;
    case 80:
      gpa='A';
      break;
    case 70:
      gpa='B';
      break;
    case 60:
      gpa='C';
      break;
    case 50:
      gpa='D';
      break;
    case 40:
      gpa='E';
      break;
    case 30:
      gpa='F';
      break;
    default:
      gpa='FAILED!';
      break;
  }
  if (flag==0){
    gpa='Invalid condition';
  }
  console.log(gpa);
  var final=document.createElement("P");
  final.innerText=gpa;
  final.id='output';
  finalMark.appendChild(final);
  total=0;


}