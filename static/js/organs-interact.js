// Quick feature detection
function isTouchEnabled() {
	return (('ontouchstart' in window)
		|| (navigator.MaxTouchPoints > 0)
		|| (navigator.msMaxTouchPoints > 0));
}
jQuery(function () {
	addEvent('APPENDIX'); addEvent('TRACHEA'); addEvent('THYROID'); addEvent('VESSELS');
	addEvent('STOMACH'); addEvent('SPLEEN'); addEvent('SMALL_INTESTINE'); addEvent('PANCREAS'); addEvent('URETERS');
	addEvent('LIVER'); addEvent('LARYNX'); addEvent('LARGE'); addEvent('BLADDER'); addEvent('DIAPHRAGM');
	addEvent('GALLBLADDER'); addEvent('HEART'); addEvent('KIDNEYS'); addEvent('LUNGS'); addEvent('HYPOTHALAMUS');
	 addEvent('PITUITARY'); addEvent('OVARIES'); addEvent('TESTES'); addEvent('ADRENALS'); addEvent('PARATHYROID');
});
function addEvent(id, relationId) {
	var _obj = jQuery('#' + id);
	_obj.attr({ 'fill': organs_config[id]['upColor'], 'fill-opacity': organs_config[id]['upOpacity'], 'stroke': organs_config[id]['outlineUpColor'], 'stroke-opacity': organs_config[id]['outlineUpOpacity'] });
	_obj.attr({ 'cursor': 'default' });
	if (organs_config[id]['enable'] == true) {
		if (isTouchEnabled()) {
			_obj.on('touchstart', function (e) {
				var touch = e.originalEvent.touches[0];
				var x = touch.pageX + 10, y = touch.pageY + 15;
				var tipw = jQuery('#organs-tip').outerWidth(), tiph = jQuery('#organs-tip').outerHeight(),
					x = (x + tipw > jQuery(document).scrollLeft() + jQuery(window).width()) ? x - tipw - (20 * 2) : x
				y = (y + tiph > jQuery(document).scrollTop() + jQuery(window).height()) ? jQuery(document).scrollTop() + jQuery(window).height() - tiph - 10 : y
				jQuery('#' + id).css({ 'fill': organs_config[id]['overColor'], 'fill-opacity': organs_config[id]['downOpacity'], 'stroke': organs_config[id]['outlineDownColor'], 'stroke-opacity': organs_config[id]['outlineDownOpacity'] });
				jQuery('#organs-tip').show().html(organs_config[id]['hover']);
				jQuery('#organs-tip').css({ left: x, top: y })
			})
			_obj.on('touchend', function () {
				jQuery('#' + id).css({ 'fill': organs_config[id]['upColor'], 'fill-opacity': organs_config[id]['upOpacity'], 'stroke': organs_config[id]['outlineUpColor'], 'stroke-opacity': organs_config[id]['outlineUpOpacity'] });
				if (organs_config[id]['target'] == 'new_window') {
					window.open(organs_config[id]['url']);
				} else if (organs_config[id]['target'] == 'same_window') {
					window.parent.location.href = organs_config[id]['url'];
				}
			})
		}
		_obj.attr({ 'cursor': 'pointer' });
		_obj.hover(function () {
			jQuery('#organs-tip').show().html(organs_config[id]['hover']);
			_obj.css({ 'fill': organs_config[id]['overColor'], 'fill-opacity': organs_config[id]['overOpacity'], 'stroke': organs_config[id]['outlineOverColor'], 'stroke-opacity': organs_config[id]['outlineOverOpacity'] })
		}, function () {
			jQuery('#organs-tip').hide();
			jQuery('#' + id).css({ 'fill': organs_config[id]['upColor'], 'fill-opacity': organs_config[id]['upOpacity'], 'stroke': organs_config[id]['outlineUpColor'], 'stroke-opacity': organs_config[id]['outlineUpOpacity'] });
		})
		_obj.mousedown(function () {
			jQuery('#' + id).css({ 'fill': organs_config[id]['downColor'], 'fill-opacity': organs_config[id]['downOpacity'], 'stroke': organs_config[id]['outlineDownColor'], 'stroke-opacity': organs_config[id]['outlineDownOpacity'] });
		})
		_obj.mouseup(function () {
			jQuery('#' + id).css({ 'fill': organs_config[id]['overColor'], 'fill-opacity': organs_config[id]['overOpacity'], 'stroke': organs_config[id]['outlineOverColor'], 'stroke-opacity': organs_config[id]['outlineOverOpacity'] });
			if (organs_config[id]['target'] == 'new_window') {
				window.open(organs_config[id]['url']);
			} else if (organs_config[id]['target'] == 'same_window') {
				window.parent.location.href = organs_config[id]['url'];
			}
		})
		_obj.mousemove(function (e) {
			var x = e.pageX + 10, y = e.pageY + 15;
			var tipw = jQuery('#organs-tip').outerWidth(), tiph = jQuery('#organs-tip').outerHeight(),
				x = (x + tipw > jQuery(document).scrollLeft() + jQuery(window).width()) ? x - tipw - (20 * 2) : x
			y = (y + tiph > jQuery(document).scrollTop() + jQuery(window).height()) ? jQuery(document).scrollTop() + jQuery(window).height() - tiph - 10 : y
			jQuery('#organs-tip').css({ left: x, top: y })
		})
	}
}
//The hotspots code
// jQuery(function () {
	// var points_len = hotspots_config['hotspots'].length;
	// if (points_len > 0) {
		// var xmlns = "http://www.w3.org/2000/svg";
		// var tsvg_obj = document.getElementById("organs_hotspots");
		// var svg_circle;
		// for (var i = 0; i < points_len; i++) {
			// svg_circle = document.createElementNS(xmlns, "circle");
			// svg_circle.setAttributeNS(null, "cx", hotspots_config['hotspots'][i]['pos_X']);
			// svg_circle.setAttributeNS(null, "cy", hotspots_config['hotspots'][i]['pos_Y']);
			// svg_circle.setAttributeNS(null, "r", hotspots_config['hotspots'][i]['diameter'] / 2);
			// svg_circle.setAttributeNS(null, "fill", hotspots_config['hotspots'][i]['upColor']);
			// svg_circle.setAttributeNS(null, "fill-opacity", hotspots_config['hotspots'][i]['upOpacity']);
			// svg_circle.setAttributeNS(null, "stroke", hotspots_config['hotspots'][i]['outlineUpColor']);
			// svg_circle.setAttributeNS(null, "stroke-opacity", hotspots_config['hotspots'][i]['outlineUpOpacity']);
			// svg_circle.setAttributeNS(null, "id", 'organs_hotspots_' + i);
			// tsvg_obj.appendChild(svg_circle);
			// dynamicAddEvent(i);
		// }
	// }
// });
// function dynamicAddEvent(id) {
	// var obj = jQuery('#organs_hotspots_' + id);
// 
	// if (hotspots_config['hotspots'][id]['enable'] == true) {
		// if (isTouchEnabled()) {
			// obj.on('touchstart', function (e) {
				// var touch = e.originalEvent.touches[0];
				// var x = touch.pageX + 10, y = touch.pageY + 15;
				// var tipw = jQuery('#organs-tip').outerWidth(), tiph = jQuery('#organs-tip').outerHeight(),
					// x = (x + tipw > jQuery(document).scrollLeft() + jQuery(window).width()) ? x - tipw - (20 * 2) : x
				// y = (y + tiph > jQuery(document).scrollTop() + jQuery(window).height()) ? jQuery(document).scrollTop() + jQuery(window).height() - tiph - 10 : y
				// jQuery('#' + id).css({ 'fill': hotspots_config['hotspots'][id]['downColor'], 'fill-opacity': hotspots_config['hotspots'][id]['downOpacity'], 'stroke': hotspots_config['hotspots'][id]['outlineDownColor'], 'stroke-opacity': hotspots_config['hotspots'][id]['outlineDownOpacity'] });
				// jQuery('#organs-tip').show().html(hotspots_config['hotspots'][id]['hover']);
				// jQuery('#organs-tip').css({ left: x, top: y })
			// })
			// obj.on('touchend', function () {
				// jQuery('#' + id).css({ 'fill': hotspots_config['hotspots'][id]['upColor'], 'fill-opacity': hotspots_config['hotspots'][id]['upOpacity'], 'stroke': hotspots_config['hotspots'][id]['outlineUpColor'], 'stroke-opacity': hotspots_config['hotspots'][id]['outlineUpOpacity'] });
				// if (hotspots_config['hotspots'][id]['target'] == 'new_window') {
					// window.open(hotspots_config['hotspots'][id]['url']);
				// } else if (hotspots_config['hotspots'][id]['target'] == 'same_window') {
					// window.parent.location.href = hotspots_config['hotspots'][id]['url'];
				// }
			// })
		// }
		// obj.attr({ 'cursor': 'pointer' });
		// obj.hover(function () {
			// jQuery('#organs-tip').show().html(hotspots_config['hotspots'][id]['hover']);
			// obj.css({ 'fill': hotspots_config['hotspots'][id]['overColor'], 'fill-opacity': hotspots_config['hotspots'][id]['overOpacity'], 'stroke': hotspots_config['hotspots'][id]['outlineOverColor'], 'stroke-opacity': hotspots_config['hotspots'][id]['outlineOverOpacity'] })
		// }, function () {
			// jQuery('#organs-tip').hide();
			// obj.css({ 'fill': hotspots_config['hotspots'][id]['upColor'], 'fill-opacity': hotspots_config['hotspots'][id]['upOpacity'], 'stroke': hotspots_config['hotspots'][id]['outlineUpColor'], 'stroke-opacity': hotspots_config['hotspots'][id]['outlineUpOpacity'] });
		// })
		// obj.mousedown(function () {
			// obj.css({ 'fill': hotspots_config['hotspots'][id]['downColor'], 'fill-opacity': hotspots_config['hotspots'][id]['downOpacity'], 'stroke': hotspots_config['hotspots'][id]['outlineDownColor'], 'stroke-opacity': hotspots_config['hotspots'][id]['outlineDownOpacity'] });
		// })
		// obj.mouseup(function () {
			// obj.css({ 'fill': hotspots_config['hotspots'][id]['overColor'], 'fill-opacity': hotspots_config['hotspots'][id]['overOpacity'], 'stroke': hotspots_config['hotspots'][id]['outlineOverColor'], 'stroke-opacity': hotspots_config['hotspots'][id]['outlineOverOpacity'] });
			// if (hotspots_config['hotspots'][id]['target'] == 'new_window') {
				// window.open(hotspots_config['hotspots'][id]['url']);
			// } else if (hotspots_config['hotspots'][id]['target'] == 'same_window') {
				// window.parent.location.href = hotspots_config['hotspots'][id]['url'];
			// }
		// })
		// obj.mousemove(function (e) {
			// var x = e.pageX + 10, y = e.pageY + 15;
			// var tipw = jQuery('#organs-tip').outerWidth(), tiph = jQuery('#organs-tip').outerHeight(),
				// x = (x + tipw > jQuery(document).scrollLeft() + jQuery(window).width()) ? x - tipw - (20 * 2) : x
			// y = (y + tiph > jQuery(document).scrollTop() + jQuery(window).height()) ? jQuery(document).scrollTop() + jQuery(window).height() - tiph - 10 : y
			// jQuery('#organs-tip').css({ left: x, top: y })
		// })
	// }
// }
