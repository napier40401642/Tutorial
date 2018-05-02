// $(function()
// {
// 	$('body').append('Hello World')
// })

$(function()
{
	var fr=$('<div/>');
	fr.append($('<div/>',{text:'France'}));
	fr.append($('<img/>',{src:'static/flags/fr.gif'}));
	$('body').append(fr);

	var br=$('<div/>');
	br.append($('<div/>',{text:'Brazil'}));
	br.append($('<img/>',{src:'static/flags/br.gif'}));
	$('body').append(br);

	var gr=$('<div/>');
	gr.append($('<div/>',{text:'Greece'}));
	gr.append($('<img/>',{src:'static/flags/gr.gif'}));
	$('body').append(gr);

	// var za=$('<div/>');
	// za.append($('<div/>',{text:'South Africa'}));
	// za.append($('<img/>',{src:'static/flags/za.gif'}));
	// $('body').append(za);

	// $('img').css({'border':'solid 3px gray',"width":200,"height":130})
	// $('div div').css('text-align','center');
	// $('body').css({'font-family':'arial','font-size':'x-large'});
	// $('body>div').css({'border':'solid 2px black',"width":210,'display':'inline-block','margin':'1ex','padding-left':'24px','padding-right':'24px'})

	var clist=[
	["br","Brazil"],
	["fr","France"],
	["gr","Greece"],
	["za","South Africa"]];

	$(function()
	{
		createOne();
	});

	function createOne()
	{
		var i=Math.floor(clist.length*Math.random());
		var code = clist[i][0];
		var name = clist[i][1];
		var qu = $('<div id="qu"/>');
		qu.append($('<div/>',{text:name,id:'ans'}));
		qu.append($('<img/>',{src:'static/flags/'+code+'.gif'}));
		qu.append($('<div/>',{text:name,id:'ans'}).hide());
		qu.append($('<input/>',{id:'response'}));
		$('body').append(qu);

		$('img').css({'border':'solid 3px gray',"width":200,"height":130})
		$('div div').css('text-align','center');
		$('body').css({'font-family':'arial','font-size':'x-large'});
		$('body>div').css({'border':'solid 2px black',"width":210,'display':'inline-block','margin':'1ex','padding':'24px'})


		$('#response').keyup(function(){
			if($('#response').val()==$('#ans').text())
			{
				alert("well Done");
			}
		});
	}
});





