//TODO: Code for folding class definitions in documentation

var hash = window.location.hash.replace(/\./g, "\\.");

function hide_all(){
$("span.fold_control a.hide_methods").click()
}

function show_all(){
$("span.fold_control a.show_methods").click()
}

function fold_one_class(){

    var methods = $(this).find("dl.attribute, dl.method");
    if (methods.length>0){
        class_folded = true;
        var controls = '<div class="fold_control"><span class="fold_control"> <a href="javascript:void(0)" class="show_methods">[show methods]</a> <a href="javascript:void(0)" class="hide_methods">[hide methods]</a> </span>';
        controls += '<span class="fold_global_control"> <a href="javascript:void(0)" class="show_all_methods">[show all methods]</a> <a href="javascript:void(0)" class="hide_all_methods">[hide all methods]</a> </span></div>';
        methods.first().before(controls);

        $(this).find("a.show_methods").click(function (){methods.show()});
        $(this).find("a.hide_methods").click(function (){methods.hide()});

        $(this).find("a.show_all_methods").click(show_all);
        $(this).find("a.hide_all_methods").click(hide_all);

        if ($(this).find(hash).length == 0){
            methods.hide();
        }
    }
}



function fold_all_classes(){
$(".bodywrapper dl.class").each(fold_one_class);
}
$(fold_all_classes);