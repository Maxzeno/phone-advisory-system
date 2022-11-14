

function footerShortLocation(h=24) {
document.querySelector('#footer-short').style.cssText = 'position:absolute; left:0; right:0; top:' + (document.body.clientHeight-h) + 'px;';
}


// FOR SENDING TO FAVOURITE
function getCookie(theCookie) {
  let cookies = document.cookie.split('; ');
  try{
    for ( i=0; i <= cookies.length; i++ ){
      if ( cookies[i].search(theCookie) >= 0 ){
        return JSON.parse(cookies[i].split('=')[1])
      }
    }
  }catch{
    return []
  }

}


function setCookie(name, value_key, overWrite=false, maxAge=60*60*24*30){
  if (overWrite==false){
  let favourite = getCookie(name);
    value = JSON.stringify(favourite.concat(value_key))
    document.cookie = name+'='+value+'; max-age=' + maxAge + ';path=/';
  }else{
    value = JSON.stringify(value_key)
    document.cookie = name+'='+value+'; max-age=' + maxAge + ';path=/';
  }
}


function deleteCookie(name, key, del_whole=false){

  if (del_whole){
    document.cookie = 'favourite=empty; max-age=' + 0;
  }else{
    let favourite = getCookie('favourite');
    indexKey = favourite.indexOf(key);

    if (indexKey < 0){

    }else{
      slice1 = favourite.slice(0, indexKey);
      slice2 = favourite.slice(indexKey+1);
      setCookie('favourite', slice1.concat(slice2), true)
    }
  }
}



 function dropNavBarElement() {
    let dis = document.querySelector('#drop-navbar-element').style.display;
    if (dis == 'block'){
      document.querySelector('#drop-navbar-element').style.display = 'none'
    }else{
      document.querySelector('#drop-navbar-element').style.display = 'block'
    }
  }

function closeDropNavBarElement() {
  let dis = document.querySelector('#drop-navbar-element').style.display;
    if (dis == 'block'){
    document.querySelector('#drop-navbar-element').style.display = 'none'
  }
  }



 
function filtersAprear() {
  let filters = document.querySelector('#filters');
  if (filters.className.search('d-lg-none') != -1){
    filters.setAttribute('class','d-none px-3 mb-2');
  }else if (filters.className.search('d-none') != -1){
    filters.setAttribute('class','d-lg-none px-3 mb-2');
  }
}


function emmaNavOpen() {
  document.getElementById('iconSideBar').style.display = 'block';
  document.getElementById('emmaNav').style.left = '0px';
  // document.getElementById('iconSideBar').style.transition = '1s';
  document.getElementById('mainNav').style.backgroundColor = '#0d0f10';
    // document.body.style.backgroundColor = "rgba(0,0,0,0.4)";


}

function emmaNavclose() {
  document.getElementById('iconSideBar').style.display = 'none';
  document.getElementById('emmaNav').style.left = '-250px';
    // document.body.style.backgroundColor = "rgb(255,255,255)";
  document.getElementById('mainNav').style.backgroundColor = '#1a1d20';

}