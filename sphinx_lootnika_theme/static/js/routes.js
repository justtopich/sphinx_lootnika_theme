const NotFoundPage = {
  name: 'NotFoundPage',
  template: '#hgh'
}

const routes = get_routes()

const router = new VueRouter({
  base: '/',
  routes
})

new Vue({
  router,
  // рендер поиска
  data: {results: null},
  // под динамический шаблон
  // created: function () {
    // this.find();
  // },
  methods: {
  	find: function(){
		var loader=document.getElementsByClassName("cs-loader")[0]
  		loader.setAttribute('style', 'display: flex');
		query=document.getElementById("query").value
		self.results=index.search(query)
		document.getElementById("a-search").click();
		sleep(500).then(() => {
			sResult=document.getElementById("sResult")
			while(sResult.firstChild){
				sResult.removeChild(sResult.firstChild);
			}
			for (res in self.results){
				// console.log(results[res]['doc']);
				h=document.createElement('h3')
				a=document.createElement('a')
				a.setAttribute('href', 'action=help#'+results[res]['doc']['url0'])
				a.setAttribute('onclick', 'clickerFn("'+results[res]['doc']['url0']+'")')
				a.innerHTML=results[res]['doc']['head']
				h.appendChild(a)
				if (results[res]['doc']['title']!==''){
					h.innerHTML+=' > '
					a=document.createElement('a')
					// a.setAttribute('href', '#/search')
                    a.setAttribute('href', 'action=help#'+results[res]['doc']['url1'])
					a.setAttribute('url', results[res]['doc']['url1'])
					a.innerHTML=results[res]['doc']['title']
					h.appendChild(a)
				}
				sResult.appendChild(h)
				p=document.createElement('p')
				p.innerHTML=results[res]['doc']['body']
				sResult.appendChild(p)
			}
			loader.setAttribute('style', 'display: none');
		})
  	}
	// под динамический шаблон
	// find: function(){
		// var loader=document.getElementsByClassName("cs-loader")[0]
  		// loader.setAttribute('style', 'display: flex');
		// query=document.getElementById("query").value
		// self.results=index.search(query)
		// console.log(self.results);
		// }
	}
}).$mount('#app')

