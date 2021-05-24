$(document).ready(function () {
  $('article img').each(function (index, item) {
    if (
      $(item).attr('data-src') &&
      $(item).attr('data-src').indexOf('download') === -1 &&
      $(item).attr('src').indexOf('coupang') === -1
    ) {
      $(item).css('cursor', 'pointer');
      $(item).click(function () {
        var loc = $(item).attr('data-src');
        window.open(loc, '_blank');
      });
    } else if (
      $(item).attr('src') &&
      $(item).attr('src').indexOf('download') === -1 &&
      $(item).attr('src').indexOf('coupang') === -1
    ) {
      $(item).css('cursor', 'pointer');
      $(item).click(function () {
        var loc = $(item).attr('src');
        window.open(loc, '_blank');
      });
    }
  });
});
