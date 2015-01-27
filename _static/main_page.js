function extend_link(){
//find the link
var a2=$(this).find("a.reference.internal").clone().empty();
$(this).find("a.reference.internal").children().unwrap();
$(this).wrap(a2);
}

$(function(){$("#profile div").each(extend_link)})