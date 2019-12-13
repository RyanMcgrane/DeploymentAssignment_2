const dbPromise = idb.open('feeds-db', 1, function (upgradeDb) {
    upgradeDb.createObjectStore('feeds', {keyPath: 'pk'});
});

fetch('http://127.0.0.1:5008/getdata').then(function(response){
  return response.json();
 }).then(function(jsondata){
  dbPromise.then(function(db){
   var tx = db.transaction('feeds', 'readwrite');
     var feedsStore = tx.objectStore('feeds');
     for(var key in jsondata){
      if (jsondata.hasOwnProperty(key)) {
        feedsStore.put(jsondata[key]);
      }
     }
  });
 });

//retrive data from idb and display on page
	var post="";
	dbPromise.then(function(db){
		var tx = db.transaction('feeds', 'readonly');
  		var feedsStore = tx.objectStore('feeds');
  		return feedsStore.openCursor();
	}).then(function logItems(cursor) {
		  if (!cursor) {
		  	document.getElementById('offlinedata').innerHTML=post;
		    return;
		  }
		  for (var field in cursor.value) {
		    	if(field=='fields'){
		    		feedsData=cursor.value[field];
		    		for(var key in feedsData){
		    			if(key =='name'){
		    				var name = '<h3>'+feedsData[key]+'</h3>';
		    			}
		    			if(key =='location'){
		    				var location = feedsData[key];
		    			}
		    			if(key == 'address'){
		    				var address = '<p>'+feedsData[key]+'</p>';
		    			}
		    		}
		    		post=post+'<br>'+name+'<br>'+location+'<br>'+address+'<br>';
		    	}
		    }
		  return cursor.continue().then(logItems);
		});