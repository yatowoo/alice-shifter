function getQcWorkflow(){

  // Env vars
  var tmp = document.getElementsByClassName("flex-row");
  var i = 0;
  for(;i<tmp.length-1;i++){
    if(tmp[i].innerText == 'Vars') break;
  }
  var runConfig = JSON.parse(tmp[i+1].innerText);
  
  // Env detectors
  var tmp = document.getElementsByTagName('tr');
  var i = 0;
  for(;i<tmp.length-1;i++){
    if(tmp[i].innerText.includes('Detectors')) break;
  }
  var detList = document.getElementsByTagName('td')[i];
  
  var detStr = '';
  for(k in runConfig ){
    if(k.includes('qc_remote_workflow')){
      var det = k.replaceAll('_qc_remote_workflow','').toUpperCase();
      console.log( det + ' - ' + runConfig[k]);
      if(runConfig[k] == 'none'){
        detStr = detStr + det + ' ';
      }else{detStr = detStr + '[' + det + '] ';}
    }
  }
  detList.innerText = detStr;
  }
  
  setTimeout(() => 
  {try{
    getQcWorkflow();
  }catch(e){;}}, 2000);
  
  document.addEventListener('change',function(){
    getQcWorkflow();
  });