// $(document).ready(function(){
// 		var quoteSource=[
// 		{
// 			quote: "Start by doing what's necessary; then do what's possible; and suddenly you are doing the impossible.",
// 			name:"Valentine AI"
// 	    },
// 	    {
// 	    	quote:"Believe you can and you're halfway there.",
// 	    	name:"Valentine AI"
// 	    }
// 	];
		
// 		$('#quoteButton').click(function(evt){
// 			//define the containers of the info we target
// 			var quote = $('#quoteContainer p').text();
// 			var quoteGenius = $('#quoteGenius').text();
// 			//prevent browser's default action
// 			evt.preventDefault();
// 			//getting a new random number to attach to a quote and setting a limit
// 			var sourceLength = quoteSource.length;
// 			var randomNumber= Math.floor(Math.random()*sourceLength);
// 			//set a new quote
// 			for(i=0;i<=sourceLength;i+=1){
// 			var newQuoteText = quoteSource[randomNumber].quote;
// 			var newQuoteGenius = quoteSource[randomNumber].name;
// 			//console.log(newQuoteText,newQuoteGenius);
//       var timeAnimation = 500;
//       var quoteContainer = $('#quoteContainer');
//       //fade out animation with callback
//       quoteContainer.fadeOut(timeAnimation, function(){
//         quoteContainer.html('');
// 				quoteContainer.append('<p>'+newQuoteText+'</p>'+'<p id="quoteGenius">'+'-								'+newQuoteGenius+'</p>');
//         //fadein animation.
//         quoteContainer.fadeIn(timeAnimation);
//       });  

// 			break;
// 		};//end for loop
	
// 	});//end quoteButton function
		
		
// });//end document ready


// // $(".submit").click(function(){
// // 	return false;

