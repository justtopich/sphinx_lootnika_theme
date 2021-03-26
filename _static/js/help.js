
function sleep (time) {
  return new Promise((resolve) => setTimeout(resolve, time));
}

// тогл для плавающего загаловка
var header             = document.getElementsByClassName('header')[0],
    header_height      = getComputedStyle(header).height.split('px')[0],
    content_guid       = document.getElementsByClassName('main-content')[0],
    sidebar_guid       = document.getElementsByClassName('nav-sidebar')[0],
    fix_class          = 'header-fixed';
    anim_class          = 'header-animation';
	// screen_height		= window.innerHeight

function stickyScroll() {
  if ( window.pageYOffset > (header_height / 1.01 )) {
	  header.classList.add(fix_class);
      sidebar_guid.setAttribute('style', 'top: 0; position: fixed;');
  }else{
	  header.classList.remove(fix_class);
	  header.classList.remove(anim_class);
	  header.removeAttribute('style');
	  sidebar_guid.removeAttribute('style');
  }
	  
}

// показ заголовка
function headermouselog(event) {
  try{
	  header_fixed = document.getElementsByClassName('header-fixed')[0];
      // console.log(event);
	  if (event==0){
		  header_fixed.setAttribute('style', 'transform: translateY(-98%);');
	  }else{
		  header.classList.add(anim_class);
		  header_fixed.setAttribute('style', 'transform: translateY(0%);');
	  }
  }catch(e){}
}

content_guid.setAttribute('style', 'top: '+header_height+'px');
// sidebar_guid.setAttribute('style', 'height: 100vh');
window.addEventListener('scroll', stickyScroll, false);

// переход к элементам на других страницах
clickerFn = function(newHash) {
    var newPage = '';
    var curPage = document.location.hash.substr(1-document.location.hash.length);
    
    if (typeof newHash !== 'string') {
        // остальное - переход из результатов поиска
        var newHash = this.hash.substr(1-this.hash.length);
    }
    
    if (newHash.indexOf('#') !== -1){
		for (var i=0; i<newHash.length; i++){
			if (newHash[i] === '#'){
				newPage=newHash.substr(0,i);
				newHash = newHash.substr(i+1,newHash.length);
			}else{
				continue
			}
		}
	}else{
		newPage=newHash;
		newHash='';
	}
	if (newPage === '') newPage=newHash
    // console.log('!#curPage '+curPage);
    // console.log('!#newHash '+newHash);
    // console.log('!#newPage '+newPage);
	
	// элемент на этой же странице?
	if (curPage.startsWith(newPage) === true){
		console.log('this page');
	}else{
		console.log('another page');
		curPage=newPage
		// убираем маркер конца страницы, чтобы ждать окончания её загрузки
		let endPage = document.getElementById('vueBottomPage')
		if (endPage !== null) {
		    endPage.remove()
		}
	}
	setTimeout(function(){waitRouter(newHash);},200) // скорость анимации перерисовки страницы
}

// для всего класса ставит дозорного
var el = document.getElementsByClassName('nav-sidebar-link');
for (var i=0; i < el.length; i++) {
    el.item(i).onclick = clickerFn;
}

//scrollto проще вызвать через клик
function waitRouter(h) {
	if (h=='') h='goToTop' // нет хеша => к началу страницы
	// ждёт загрузки страницы
	if (document.getElementById('vueBottomPage') === null){
		console.log('!#sleep');
		sleep(200).then(() => {
			waitRouter(h)
		});
	}else{
        sleep(100).then(() => {
            try{
                 console.log('!#get el ' + h);
                let bb = document.getElementById(h)
				window.VueScrollTo.scrollTo(bb);
            }catch (err){
                console.log('lol ' + h);
            }
        });
	}

}
