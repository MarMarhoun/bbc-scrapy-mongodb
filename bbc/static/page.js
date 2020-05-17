function getUrlArgObject() {
  var args = new Object();
  var query = location.search.slice(1)
  var pairs = query.split("&")
  for (var i=0; i<pairs.length; i++) {
    var pos = pairs[i].indexOf('='); 
    if (pos == -1) { 
      continue;
    }
    var key = pairs[i].substring(0,pos); //Name
    var value = pairs[i].substring(pos+1); //value
    args[key] = decodeURI(value); 
  }
  return args;
};

/*$(function() {
  var $SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
  var args = getUrlArgObject();
  if (args.page !== 'undefined') {
    var p = parseInt(args.page)
    if (p-1 === 0) {
      $(".previous").attr("class", "previous disabled")
    } else {
      $("#prev").attr("href", $SCRIPT_ROOT+"/search?key="+args.key+"&page="+(p-1))
    }
    if ($("li.row").length < 60) {
      $(".next").attr("class", "next disabled")
    } else {
      $("#next").attr("href", $SCRIPT_ROOT+"/search?key="+args.key+"&page="+(p+1))
    }
  }
}); */

$(document).ready(function() {
  var args = getUrlArgObject();
  window.page = parseInt(args.page)

  $("#next").click(function() {
    $.ajax({
      url: "search",
      type: "GET",
      dataType: "html",
      data: {"key":args.key, "catid": args.catid, "page": window.page+1},
      error: function(){alert('error');},
      success: function (data) {
        var wrappedObj = $("<code></code>").append($(data));
        var content = $("ul.entries", wrappedObj);
        $("ul.entries").html(content.html());
        window.page += 1;
      }
    });
  });

  $("#prev").click(function() {
    $.ajax({
      url: "search",
      type: "GET",
      dataType: "html",
      data: {"key": args.key, "catid": args.catid, "page": window.page-1},
      error: function(){alert('error');},
      success: function (data) {
        var wrappedObj = $("<code></code>").append($(data));
        var content = $("ul.entries", wrappedObj);
        $("ul.entries").html(content.html());
        window.page -= 1;
      }
    });
  });
});
