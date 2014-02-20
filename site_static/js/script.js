$(document).ready(function () {

    $(".side-nav-in ul li a").click(function () {
        $(this).parent().find('ul').slideToggle(500);

        $(".side-nav-in ul li a").removeClass("active");
        $(this).addClass("active");

    });
    $(".side-nav-in ul li ul a").click(function () {
        $(this).parents('ul').prev().addClass("active");

    });


    $(".calendar:visible").find(".next").click(function () {
        var par = $(this).parents(".calendar");
        var month = par.find(".month li"),
            monthWidth = month.outerWidth(true),
            monthSize = month.size(),
            sliderWidth = monthSize * monthWidth ,
            wrpWidth = par.width(),
            visible = -(sliderWidth - wrpWidth),
            monthRow = par.find('.month');
        var S = $(".calendar").width() / 6;
        monthRow.css("width", sliderWidth);
        if (!monthRow.is(":animated")) {
            if (monthRow.position().left > visible) {
                monthRow.animate({
                    left: '-=' + monthWidth
                });
                par.find(".prev").fadeIn();
            }
            else {
                par.find(".next").fadeOut();
            }
        }
    });
    $(".calendar:visible").find(".prev").click(function () {
        var par = $(this).parents(".calendar");
        var month = par.find("li"),
            monthWidth = month.outerWidth(true),
            monthSize = month.size(),
            sliderWidth = monthSize * monthWidth ,
            monthRow = par.find('.month');
        var S = $(".calendar").width() / 6;
        monthRow.css("width", sliderWidth);
        if (!monthRow.is(":animated")) {
            if (monthRow.position().left < 0) {
                monthRow.animate({
                    left: '+=' + monthWidth
                });
                par.find(".next").fadeIn();
            }
            else {
                par.find(".prev").fadeOut();
            }
        }
    });

    var i;
    var month = $(".news-block .calendar").find("li");

    function setDays() {

        var monthSize = month.size();

        for (var m = 0; m < monthSize; m++) {
            $(".news-block .days").eq(0).clone().appendTo($(".news-block .calendar"));
        }
        $(".news-block .days").find("li").html("");
        month.each(function () {
                var monthInd = $(this).index();
                var n = monthInd % 2;
                switch (n) {
                    case 0:
                        i = 31;

                        for (var k = 1; k <= i; k++) {
                            $(".news-block .days").eq(monthInd).find("li").eq(k - 1).html(k);
                        }

                    case 1:
                        i = 30;
                        if (monthInd === 1) {
                            i = 28;
                        }
                        for (var k = 1; k <= i; k++) {
                            $(".news-block .days").eq(monthInd).find("li").eq(k - 1).html(k);
                        }

                }
            }
        )

        var cur = $(".month").find('li.active').index();
        $(".news-block .days").hide();
        $(".news-block .days").eq(cur).show();

    }

    setDays();
    var month = $(".calendar .month").find("li");
    month.click(function () {
        var par = $(this).parents(".calendar");
        par.find(".month li").removeClass("active");
        $(this).addClass("active");
        var cur = par.find('.month li.active').index();
        $(".news-block .days").hide();
        $(".news-block .days").eq(cur).show();
    });
    $('.days').find("li").click(function () {
        $(this).toggleClass("active");
    });

    $('body').on('mousever', function () {
        $(".menu li ul").slideUp();
    });
    $(".menu li a").mouseenter(function (e) {
        var menuInner = $(this).parent().find('ul');
        if (menuInner.is(":animated")) {
            return false;
        }
        else {

            menuInner.slideDown()
        }

    });

    $('body').on('mouseleave', '.menu li', function (e) {
        var menuInner = $(this).find('ul');
        menuInner.slideUp()
    });


    $(".menu li ul li a").click(function () {
        $(".menu li ul li a").removeClass("active");
        $(this).addClass("active")
    })
})
;

  $(document).ready(function () {
        $(".gallery").each(function (index, v) {
            $(this).find('.gallery__item').colorbox({rel: 'gallery' + index });
        });
        
    });